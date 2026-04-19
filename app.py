from flask import Flask, render_template_string, request, jsonify, session, send_from_directory, send_file
import sqlite3
import hashlib
import secrets
import os
import json
import re
import random
import base64
from datetime import timedelta, datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['BACKUP_FOLDER'] = 'backups'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB макс размер

# Создаем папки
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['BACKUP_FOLDER'], exist_ok=True)
os.makedirs('png', exist_ok=True)

# Встроенное шифрование без внешних библиотек
def simple_encrypt(data, password):
    """Простое шифрование на основе XOR с паролем"""
    key = hashlib.sha256(password.encode()).digest()
    encrypted = bytearray()
    for i, byte in enumerate(data.encode('utf-8')):
        encrypted.append(byte ^ key[i % len(key)])
    return base64.b64encode(encrypted).decode()

def simple_decrypt(encrypted_data, password):
    """Дешифрование XOR с паролем"""
    try:
        key = hashlib.sha256(password.encode()).digest()
        encrypted = base64.b64decode(encrypted_data)
        decrypted = bytearray()
        for i, byte in enumerate(encrypted):
            decrypted.append(byte ^ key[i % len(key)])
        return decrypted.decode('utf-8')
    except:
        raise ValueError("Неверный пароль или поврежденный файл")

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Добавляем колонку last_backup если её нет
    try:
        c.execute('ALTER TABLE users ADD COLUMN last_backup TIMESTAMP')
    except:
        pass
    
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        password TEXT NOT NULL,
        avatar TEXT,
        balance REAL DEFAULT 0,
        bktok_balance REAL DEFAULT 100,
        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_backup TIMESTAMP
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS friends (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        friend_id INTEGER NOT NULL,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (friend_id) REFERENCES users (id),
        UNIQUE(user_id, friend_id)
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS tasks_completed (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        task_id TEXT NOT NULL,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id),
        UNIQUE(user_id, task_id)
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS bktok_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        order_type TEXT NOT NULL,
        price REAL NOT NULL,
        amount REAL NOT NULL,
        remaining REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS bktok_trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        buyer_id INTEGER NOT NULL,
        seller_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        price REAL NOT NULL,
        trade_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (buyer_id) REFERENCES users (id),
        FOREIGN KEY (seller_id) REFERENCES users (id)
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS support_chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        sender TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS private_chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT NOT NULL,
        sender_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (sender_id) REFERENCES users (id)
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS rollback_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_user_id INTEGER NOT NULL,
        to_user_id INTEGER NOT NULL,
        trade_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        price REAL NOT NULL,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (from_user_id) REFERENCES users (id),
        FOREIGN KEY (to_user_id) REFERENCES users (id)
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS reset_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        token TEXT UNIQUE NOT NULL,
        expires_at TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    
    conn.commit()
    conn.close()
    print("✅ База данных инициализирована")

init_db()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Не авторизован'}), 401
        return f(*args, **kwargs)
    return decorated_function

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Загружаем HTML
with open('index.html', 'r', encoding='utf-8') as f:
    INDEX_HTML = f.read()

@app.route('/')
def index():
    return render_template_string(INDEX_HTML)

@app.route('/png/<path:filename>')
def serve_png(filename):
    return send_from_directory('png', filename)

@app.route('/uploads/<path:filename>')
def serve_uploads(filename):
    return send_from_directory('uploads', filename)

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory('.', 'sw.js')

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

# API эндпоинты для бэкапов
@app.route('/api/backup/create', methods=['POST'])
@login_required
def create_backup():
    data = request.json
    password = data.get('password', '')
    
    if not password or len(password) < 6:
        return jsonify({'success': False, 'message': 'Пароль должен быть не менее 6 символов'})
    
    conn = get_db()
    c = conn.cursor()
    
    user_id = session['user_id']
    
    # Данные пользователя
    c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user_data = dict(c.fetchone())
    if 'password' in user_data:
        del user_data['password']
    
    # Друзья
    c.execute('''
        SELECT u.username, u.name, u.avatar, f.status, f.created_at 
        FROM friends f
        JOIN users u ON f.friend_id = u.id
        WHERE f.user_id = ?
    ''', (user_id,))
    friends = [dict(row) for row in c.fetchall()]
    
    # Задания
    c.execute('SELECT * FROM tasks_completed WHERE user_id = ?', (user_id,))
    tasks = [dict(row) for row in c.fetchall()]
    
    # Ордера
    c.execute('SELECT * FROM bktok_orders WHERE user_id = ?', (user_id,))
    orders = [dict(row) for row in c.fetchall()]
    
    # Сделки
    c.execute('SELECT * FROM bktok_trades WHERE buyer_id = ? OR seller_id = ?', (user_id, user_id))
    trades = [dict(row) for row in c.fetchall()]
    
    # Чаты
    c.execute('SELECT * FROM support_chats WHERE user_id = ?', (user_id,))
    support_chats = [dict(row) for row in c.fetchall()]
    
    c.execute('''SELECT * FROM private_chats 
                 WHERE sender_id = ? OR chat_id LIKE '%_' || ? || '\_%' ESCAPE '\\' ''', 
              (user_id, user_id))
    private_messages = [dict(row) for row in c.fetchall()]
    
    backup_data = {
        'version': '2.0',
        'created_at': datetime.utcnow().isoformat(),
        'user_id': user_id,
        'username': session['username'],
        'user_data': user_data,
        'friends': friends,
        'tasks': tasks,
        'orders': orders,
        'trades': trades,
        'support_chats': support_chats,
        'private_messages': private_messages
    }
    
    json_data = json.dumps(backup_data, default=str, ensure_ascii=False)
    encrypted_data = simple_encrypt(json_data, password)
    
    backup_filename = f"bktok_backup_{user_id}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.bkp"
    backup_path = os.path.join(app.config['BACKUP_FOLDER'], backup_filename)
    
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(encrypted_data)
    
    c.execute('UPDATE users SET last_backup = ? WHERE id = ?', (datetime.utcnow(), user_id))
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'message': '✅ Бэкап успешно создан!',
        'filename': backup_filename,
        'size': len(encrypted_data)
    })

@app.route('/api/backup/download', methods=['GET'])
@login_required
def download_backup():
    user_id = session['user_id']
    
    backup_files = [f for f in os.listdir(app.config['BACKUP_FOLDER']) 
                   if f.startswith(f'bktok_backup_{user_id}_')]
    
    if not backup_files:
        return jsonify({'success': False, 'message': 'Бэкап не найден'}), 404
    
    backup_files.sort(reverse=True)
    backup_path = os.path.join(app.config['BACKUP_FOLDER'], backup_files[0])
    
    return send_file(
        backup_path,
        as_attachment=True,
        download_name=f"BK_Bank_Backup_{datetime.now().strftime('%Y%m%d')}.bkp",
        mimetype='application/octet-stream'
    )

@app.route('/api/backup/restore', methods=['POST'])
@login_required
def restore_backup():
    if 'backup_file' not in request.files:
        return jsonify({'success': False, 'message': 'Файл не загружен'})
    
    file = request.files['backup_file']
    password = request.form.get('password', '')
    
    if not password:
        return jsonify({'success': False, 'message': 'Введите пароль от бэкапа'})
    
    try:
        encrypted_data = file.read().decode('utf-8')
        json_data = simple_decrypt(encrypted_data, password)
        backup_data = json.loads(json_data)
        
        if backup_data['user_id'] != session['user_id']:
            return jsonify({'success': False, 'message': 'Этот бэкап принадлежит другому пользователю'})
        
        conn = get_db()
        c = conn.cursor()
        user_id = session['user_id']
        
        user = backup_data['user_data']
        c.execute('''
            UPDATE users SET 
                name = ?, email = ?, phone = ?, avatar = ?, 
                balance = ?, bktok_balance = ?
            WHERE id = ?
        ''', (
            user['name'], user.get('email'), user.get('phone'), 
            user.get('avatar'), user.get('balance', 0), 
            user.get('bktok_balance', 100), user_id
        ))
        
        c.execute('DELETE FROM tasks_completed WHERE user_id = ?', (user_id,))
        for task in backup_data['tasks']:
            c.execute('''
                INSERT OR IGNORE INTO tasks_completed (user_id, task_id, completed_at)
                VALUES (?, ?, ?)
            ''', (user_id, task['task_id'], task['completed_at']))
        
        c.execute('DELETE FROM friends WHERE user_id = ?', (user_id,))
        for friend in backup_data['friends']:
            c.execute('SELECT id FROM users WHERE username = ?', (friend['username'],))
            friend_user = c.fetchone()
            if friend_user:
                c.execute('''
                    INSERT OR IGNORE INTO friends (user_id, friend_id, status, created_at)
                    VALUES (?, ?, ?, ?)
                ''', (user_id, friend_user['id'], friend['status'], friend['created_at']))
        
        conn.commit()
        conn.close()
        
        session['name'] = user['name']
        
        return jsonify({
            'success': True,
            'message': '✅ Данные успешно восстановлены! Перезагрузите страницу.',
            'reload': True
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': '❌ Неверный пароль или файл поврежден'})

@app.route('/api/backup/info', methods=['GET'])
@login_required
def get_backup_info():
    user_id = session['user_id']
    
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT last_backup FROM users WHERE id = ?', (user_id,))
    user = c.fetchone()
    conn.close()
    
    backup_files = [f for f in os.listdir(app.config['BACKUP_FOLDER']) 
                   if f.startswith(f'bktok_backup_{user_id}_')]
    
    backup_size = 0
    if backup_files:
        backup_files.sort(reverse=True)
        backup_path = os.path.join(app.config['BACKUP_FOLDER'], backup_files[0])
        backup_size = os.path.getsize(backup_path)
    
    return jsonify({
        'success': True,
        'last_backup': user['last_backup'] if user else None,
        'backup_count': len(backup_files),
        'backup_size': backup_size,
        'backup_size_mb': round(backup_size / 1024 / 1024, 2)
    })

# Остальные API эндпоинты (регистрация, логин, профиль и т.д.)
# ... (вставьте сюда все остальные эндпоинты из вашего оригинального app.py)

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 BK-Bank сервер запущен!")
    print("💾 Система бэкапов активна")
    print("📱 Поддержка PWA и мобильных устройств")
    print("📍 http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
