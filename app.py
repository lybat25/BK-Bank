from flask import Flask, render_template, request, jsonify, session
import sqlite3
import hashlib
import secrets
from datetime import timedelta

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        balance REAL DEFAULT 0,
        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    
    c.execute('''CREATE TABLE IF NOT EXISTS reset_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        token TEXT UNIQUE NOT NULL,
        expires_at TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    
    conn.commit()
    conn.close()

init_db()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_by_username(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT id, username, name, email, password, balance, registration_date FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    conn.close()
    if user:
        return {
            'id': user[0],
            'username': user[1],
            'name': user[2],
            'email': user[3],
            'password': user[4],
            'balance': user[5],
            'registration_date': user[6]
        }
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username', '').strip()
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    
    if not all([username, name, email, password]):
        return jsonify({'success': False, 'message': 'Все поля обязательны'})
    
    if len(password) < 6:
        return jsonify({'success': False, 'message': 'Пароль должен быть не менее 6 символов'})
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('SELECT id FROM users WHERE username = ? OR email = ?', (username, email))
    if c.fetchone():
        conn.close()
        return jsonify({'success': False, 'message': 'Пользователь с таким именем или email уже существует'})
    
    hashed_password = hash_password(password)
    c.execute('INSERT INTO users (username, name, email, password) VALUES (?, ?, ?, ?)',
              (username, name, email, hashed_password))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Регистрация успешна'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    user = get_user_by_username(username)
    if not user or user['password'] != hash_password(password):
        return jsonify({'success': False, 'message': 'Неверный логин или пароль'})
    
    session['user_id'] = user['id']
    session['username'] = user['username']
    session['name'] = user['name']
    session.permanent = True
    
    return jsonify({
        'success': True,
        'user': {
            'username': user['username'],
            'name': user['name'],
            'email': user['email'],
            'balance': user['balance']
        }
    })

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True})

@app.route('/api/check-session', methods=['GET'])
def check_session():
    if 'user_id' in session:
        user = get_user_by_username(session['username'])
        if user:
            return jsonify({
                'success': True,
                'user': {
                    'username': user['username'],
                    'name': user['name'],
                    'email': user['email'],
                    'balance': user['balance']
                }
            })
    return jsonify({'success': False})

@app.route('/api/profile', methods=['GET'])
def get_profile():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Не авторизован'})
    
    user = get_user_by_username(session['username'])
    if not user:
        return jsonify({'success': False, 'message': 'Пользователь не найден'})
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT u.username, u.name FROM friends f
        JOIN users u ON f.friend_id = u.id
        WHERE f.user_id = ? AND f.status = 'accepted'
    ''', (user['id'],))
    friends = [{'username': row[0], 'name': row[1]} for row in c.fetchall()]
    
    c.execute('''
        SELECT u.username, u.name FROM friends f
        JOIN users u ON f.user_id = u.id
        WHERE f.friend_id = ? AND f.status = 'pending'
    ''', (user['id'],))
    friend_requests = [{'username': row[0], 'name': row[1]} for row in c.fetchall()]
    
    conn.close()
    
    return jsonify({
        'success': True,
        'user': {
            'username': user['username'],
            'name': user['name'],
            'email': user['email'],
            'balance': user['balance'],
            'registration_date': user['registration_date']
        },
        'friends': friends,
        'friendRequests': friend_requests
    })

@app.route('/api/friend-request', methods=['POST'])
def send_friend_request():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Не авторизован'})
    
    data = request.json
    friend_username = data.get('username', '').strip()
    
    friend = get_user_by_username(friend_username)
    if not friend:
        return jsonify({'success': False, 'message': 'Пользователь не найден'})
    
    if friend['id'] == session['user_id']:
        return jsonify({'success': False, 'message': 'Нельзя добавить себя в друзья'})
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''SELECT status FROM friends 
                 WHERE (user_id = ? AND friend_id = ?) OR (user_id = ? AND friend_id = ?)''',
              (session['user_id'], friend['id'], friend['id'], session['user_id']))
    existing = c.fetchone()
    
    if existing:
        conn.close()
        return jsonify({'success': False, 'message': 'Запрос уже существует или вы уже друзья'})
    
    c.execute('INSERT INTO friends (user_id, friend_id) VALUES (?, ?)',
              (session['user_id'], friend['id']))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Запрос отправлен'})

@app.route('/api/accept-friend', methods=['POST'])
def accept_friend():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Не авторизован'})
    
    data = request.json
    friend_username = data.get('username', '').strip()
    
    friend = get_user_by_username(friend_username)
    if not friend:
        return jsonify({'success': False, 'message': 'Пользователь не найден'})
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''UPDATE friends SET status = 'accepted' 
                 WHERE user_id = ? AND friend_id = ? AND status = 'pending' ''',
              (friend['id'], session['user_id']))
    
    if c.rowcount == 0:
        conn.close()
        return jsonify({'success': False, 'message': 'Запрос не найден'})
    
    c.execute('INSERT INTO friends (user_id, friend_id, status) VALUES (?, ?, ?)',
              (session['user_id'], friend['id'], 'accepted'))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Запрос принят'})

@app.route('/api/decline-friend', methods=['POST'])
def decline_friend():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Не авторизован'})
    
    data = request.json
    friend_username = data.get('username', '').strip()
    
    friend = get_user_by_username(friend_username)
    if not friend:
        return jsonify({'success': False, 'message': 'Пользователь не найден'})
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''DELETE FROM friends 
                 WHERE user_id = ? AND friend_id = ? AND status = 'pending' ''',
              (friend['id'], session['user_id']))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Запрос отклонен'})

@app.route('/api/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email', '').strip()
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT id, username FROM users WHERE email = ?', (email,))
    user = c.fetchone()
    
    if not user:
        conn.close()
        return jsonify({'success': False, 'message': 'Email не найден'})
    
    import secrets
    from datetime import datetime, timedelta
    
    token = secrets.token_urlsafe(32)
    expires_at = datetime.now() + timedelta(hours=1)
    
    c.execute('DELETE FROM reset_tokens WHERE user_id = ?', (user[0],))
    c.execute('INSERT INTO reset_tokens (user_id, token, expires_at) VALUES (?, ?, ?)',
              (user[0], token, expires_at))
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True, 
        'message': f'Ссылка для сброса: /reset-password?token={token}'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
