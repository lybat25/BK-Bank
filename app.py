from flask import Flask, render_template_string, request, jsonify, session, send_from_directory
import sqlite3
import hashlib
import secrets
import os
import json
import re
import random
from datetime import timedelta, datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('png', exist_ok=True)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        phone TEXT,
        password TEXT NOT NULL,
        avatar TEXT,
        balance REAL DEFAULT 0,
        bktok_balance REAL DEFAULT 100,
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

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username', '').strip()
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '+70000000000').strip()
    password = data.get('password', '')
    
    if not all([username, name, password]):
        return jsonify({'success': False, 'message': 'Все поля обязательны'})
    
    if len(password) < 6:
        return jsonify({'success': False, 'message': 'Пароль должен быть не менее 6 символов'})
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT id FROM users WHERE username = ?', (username,))
    if c.fetchone():
        conn.close()
        return jsonify({'success': False, 'message': 'Пользователь с таким именем уже существует'})
    
    if email:
        c.execute('SELECT id FROM users WHERE email = ?', (email,))
        if c.fetchone():
            conn.close()
            return jsonify({'success': False, 'message': 'Email уже используется'})
    
    hashed_password = hash_password(password)
    c.execute('INSERT INTO users (username, name, email, phone, password, bktok_balance) VALUES (?, ?, ?, ?, ?, 100)',
              (username, name, email, phone, hashed_password))
    conn.commit()
    
    user_id = c.lastrowid
    session['user_id'] = user_id
    session['username'] = username
    session['name'] = name
    session.permanent = True
    
    conn.close()
    
    return jsonify({
        'success': True,
        'message': 'Регистрация успешна',
        'user': {
            'id': user_id,
            'username': username,
            'name': name,
            'email': email,
            'phone': phone,
            'bktok_balance': 100
        }
    })

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    login_input = data.get('username', '').strip()
    password = data.get('password', '')
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''SELECT id, username, name, email, phone, password, avatar, bktok_balance 
                 FROM users WHERE username = ? OR email = ? OR phone = ?''', 
              (login_input, login_input, login_input))
    user = c.fetchone()
    conn.close()
    
    if not user or user['password'] != hash_password(password):
        return jsonify({'success': False, 'message': 'Неверный логин или пароль'})
    
    session['user_id'] = user['id']
    session['username'] = user['username']
    session['name'] = user['name']
    session.permanent = True
    
    return jsonify({
        'success': True,
        'user': {
            'id': user['id'],
            'username': user['username'],
            'name': user['name'],
            'email': user['email'],
            'phone': user['phone'],
            'avatar': user['avatar'],
            'bktok_balance': user['bktok_balance']
        }
    })

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True})

@app.route('/api/check-session', methods=['GET'])
def check_session():
    if 'user_id' in session:
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT id, username, name, email, phone, avatar, bktok_balance FROM users WHERE id = ?', 
                  (session['user_id'],))
        user = c.fetchone()
        conn.close()
        
        if user:
            return jsonify({'success': True, 'user': dict(user)})
    return jsonify({'success': False})

@app.route('/api/profile', methods=['GET'])
@login_required
def get_profile():
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT id, username, name, email, phone, avatar, balance, bktok_balance, registration_date FROM users WHERE id = ?', 
              (session['user_id'],))
    user = c.fetchone()
    
    if not user:
        conn.close()
        return jsonify({'success': False, 'message': 'Пользователь не найден'})
    
    c.execute('''
        SELECT u.id, u.username, u.name, u.avatar FROM friends f
        JOIN users u ON f.friend_id = u.id
        WHERE f.user_id = ? AND f.status = 'accepted'
    ''', (session['user_id'],))
    friends = [dict(row) for row in c.fetchall()]
    
    c.execute('''
        SELECT u.id, u.username, u.name, u.avatar FROM friends f
        JOIN users u ON f.user_id = u.id
        WHERE f.friend_id = ? AND f.status = 'pending'
    ''', (session['user_id'],))
    friend_requests = [dict(row) for row in c.fetchall()]
    
    conn.close()
    
    return jsonify({
        'success': True,
        'user': dict(user),
        'friends': friends,
        'friendRequests': friend_requests
    })

@app.route('/api/profile/update', methods=['POST'])
@login_required
def update_profile():
    data = request.json
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    password = data.get('password', '')
    
    conn = get_db()
    c = conn.cursor()
    
    updates = []
    params = []
    
    if name:
        updates.append('name = ?')
        params.append(name)
        session['name'] = name
    
    if email:
        updates.append('email = ?')
        params.append(email)
    
    if phone:
        updates.append('phone = ?')
        params.append(phone)
    
    if password and len(password) >= 6:
        updates.append('password = ?')
        params.append(hash_password(password))
    
    if updates:
        params.append(session['user_id'])
        c.execute(f'UPDATE users SET {", ".join(updates)} WHERE id = ?', params)
        conn.commit()
    
    conn.close()
    return jsonify({'success': True, 'message': 'Профиль обновлен'})

@app.route('/api/profile/avatar', methods=['POST'])
@login_required
def upload_avatar():
    if 'avatar' not in request.files:
        return jsonify({'success': False, 'message': 'Файл не загружен'})
    
    file = request.files['avatar']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'Файл не выбран'})
    
    filename = f"avatar_{session['user_id']}_{secrets.token_hex(8)}.png"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    avatar_url = f'/uploads/{filename}'
    
    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE users SET avatar = ? WHERE id = ?', (avatar_url, session['user_id']))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'avatar': avatar_url})

@app.route('/api/bktok/balance', methods=['GET'])
@login_required
def get_bktok_balance():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT bktok_balance FROM users WHERE id = ?', (session['user_id'],))
    user = c.fetchone()
    conn.close()
    return jsonify({'success': True, 'balance': user['bktok_balance'] if user else 0})

@app.route('/api/bktok/orders', methods=['GET'])
@login_required
def get_orders():
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''
        SELECT o.*, u.username FROM bktok_orders o
        JOIN users u ON o.user_id = u.id
        WHERE o.remaining > 0
        ORDER BY o.created_at DESC
    ''')
    orders = [dict(row) for row in c.fetchall()]
    
    c.execute('SELECT * FROM bktok_orders WHERE user_id = ? AND remaining > 0', (session['user_id'],))
    my_orders = [dict(row) for row in c.fetchall()]
    
    conn.close()
    return jsonify({'success': True, 'orders': orders, 'my_orders': my_orders})

@app.route('/api/bktok/order', methods=['POST'])
@login_required
def create_order():
    data = request.json
    order_type = data.get('type')
    price = float(data.get('price', 0))
    amount = float(data.get('amount', 0))
    
    if order_type not in ['buy', 'sell']:
        return jsonify({'success': False, 'message': 'Неверный тип ордера'})
    
    if price <= 0 or amount <= 0:
        return jsonify({'success': False, 'message': 'Неверная цена или количество'})
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT bktok_balance FROM users WHERE id = ?', (session['user_id'],))
    user = c.fetchone()
    
    if order_type == 'buy':
        required = amount * price * 1.001
        if user['bktok_balance'] < required:
            conn.close()
            return jsonify({'success': False, 'message': 'Недостаточно средств'})
        c.execute('UPDATE users SET bktok_balance = bktok_balance - ? WHERE id = ?', 
                  (required, session['user_id']))
    else:
        if user['bktok_balance'] < amount:
            conn.close()
            return jsonify({'success': False, 'message': 'Недостаточно BK'})
        c.execute('UPDATE users SET bktok_balance = bktok_balance - ? WHERE id = ?', 
                  (amount, session['user_id']))
    
    c.execute('''INSERT INTO bktok_orders (user_id, order_type, price, amount, remaining)
                 VALUES (?, ?, ?, ?, ?)''',
              (session['user_id'], order_type, price, amount, amount))
    
    match_orders(conn)
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Ордер создан'})

def match_orders(conn):
    c = conn.cursor()
    
    c.execute('''
        SELECT * FROM bktok_orders 
        WHERE order_type = 'buy' AND remaining > 0 
        ORDER BY price DESC, created_at ASC
    ''')
    buy_orders = [dict(row) for row in c.fetchall()]
    
    c.execute('''
        SELECT * FROM bktok_orders 
        WHERE order_type = 'sell' AND remaining > 0 
        ORDER BY price ASC, created_at ASC
    ''')
    sell_orders = [dict(row) for row in c.fetchall()]
    
    for buy in buy_orders:
        for sell in sell_orders:
            if buy['price'] >= sell['price'] and buy['user_id'] != sell['user_id']:
                trade_amount = min(buy['remaining'], sell['remaining'])
                trade_price = sell['price']
                fee = trade_amount * trade_price * 0.001
                
                c.execute('UPDATE users SET bktok_balance = bktok_balance + ? WHERE id = ?', 
                          (trade_amount, buy['user_id']))
                c.execute('UPDATE users SET bktok_balance = bktok_balance + ? WHERE id = ?', 
                          (trade_amount * trade_price - fee, sell['user_id']))
                c.execute('''INSERT INTO bktok_trades (buyer_id, seller_id, amount, price)
                             VALUES (?, ?, ?, ?)''',
                          (buy['user_id'], sell['user_id'], trade_amount, trade_price))
                c.execute('UPDATE bktok_orders SET remaining = remaining - ? WHERE id = ?',
                          (trade_amount, buy['id']))
                c.execute('UPDATE bktok_orders SET remaining = remaining - ? WHERE id = ?',
                          (trade_amount, sell['id']))
                
                buy['remaining'] -= trade_amount
                sell['remaining'] -= trade_amount

@app.route('/api/bktok/order/<int:order_id>/cancel', methods=['POST'])
@login_required
def cancel_order(order_id):
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT * FROM bktok_orders WHERE id = ? AND user_id = ?', 
              (order_id, session['user_id']))
    order = c.fetchone()
    
    if not order:
        conn.close()
        return jsonify({'success': False, 'message': 'Ордер не найден'})
    
    if order['order_type'] == 'buy':
        refund = order['remaining'] * order['price'] * 1.001
        c.execute('UPDATE users SET bktok_balance = bktok_balance + ? WHERE id = ?',
                  (refund, session['user_id']))
    else:
        c.execute('UPDATE users SET bktok_balance = bktok_balance + ? WHERE id = ?',
                  (order['remaining'], session['user_id']))
    
    c.execute('UPDATE bktok_orders SET remaining = 0 WHERE id = ?', (order_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Ордер отменен'})

@app.route('/api/bktok/trades', methods=['GET'])
@login_required
def get_trades():
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''
        SELECT t.*, 
               b.username as buyer_name, 
               s.username as seller_name
        FROM bktok_trades t
        JOIN users b ON t.buyer_id = b.id
        JOIN users s ON t.seller_id = s.id
        ORDER BY t.trade_time DESC
        LIMIT 100
    ''')
    trades = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify({'success': True, 'trades': trades})

@app.route('/api/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = [
        {'id': 'daily', 'name': 'Ежедневный вход', 'reward': 10, 'cooldown': 86400000},
        {'id': 'profile', 'name': 'Заполнить профиль', 'reward': 50, 'once': True},
        {'id': 'avatar', 'name': 'Установить аватар', 'reward': 30, 'once': True},
        {'id': 'trade', 'name': 'Совершить сделку', 'reward': 20, 'cooldown': 3600000}
    ]
    
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT task_id, completed_at FROM tasks_completed WHERE user_id = ?', 
              (session['user_id'],))
    completed = {row['task_id']: row['completed_at'] for row in c.fetchall()}
    conn.close()
    
    for task in tasks:
        task['completed'] = task['id'] in completed
        if task['id'] in completed:
            task['completed_at'] = completed[task['id']]
    
    return jsonify({'success': True, 'tasks': tasks})

@app.route('/api/tasks/<task_id>/complete', methods=['POST'])
@login_required
def complete_task(task_id):
    tasks_config = {
        'daily': {'reward': 10, 'cooldown': 86400000},
        'profile': {'reward': 50, 'once': True},
        'avatar': {'reward': 30, 'once': True},
        'trade': {'reward': 20, 'cooldown': 3600000}
    }
    
    if task_id not in tasks_config:
        return jsonify({'success': False, 'message': 'Задание не найдено'})
    
    task = tasks_config[task_id]
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT completed_at FROM tasks_completed WHERE user_id = ? AND task_id = ?',
              (session['user_id'], task_id))
    completed = c.fetchone()
    
    if completed:
        if 'once' in task:
            conn.close()
            return jsonify({'success': False, 'message': 'Задание уже выполнено'})
        
        if 'cooldown' in task:
            completed_time = datetime.fromisoformat(completed['completed_at'].replace('Z', '+00:00'))
            if (datetime.utcnow() - completed_time.replace(tzinfo=None)).total_seconds() * 1000 < task['cooldown']:
                conn.close()
                return jsonify({'success': False, 'message': 'Задание на кулдауне'})
    
    if task_id == 'profile':
        c.execute('SELECT email, phone FROM users WHERE id = ?', (session['user_id'],))
        user = c.fetchone()
        if not user['email'] or user['phone'] == '+70000000000':
            conn.close()
            return jsonify({'success': False, 'message': 'Заполните профиль'})
    
    if task_id == 'avatar':
        c.execute('SELECT avatar FROM users WHERE id = ?', (session['user_id'],))
        user = c.fetchone()
        if not user['avatar']:
            conn.close()
            return jsonify({'success': False, 'message': 'Установите аватар'})
    
    if task_id == 'trade':
        c.execute('SELECT COUNT(*) as count FROM bktok_trades WHERE buyer_id = ? OR seller_id = ?',
                  (session['user_id'], session['user_id']))
        if c.fetchone()['count'] == 0:
            conn.close()
            return jsonify({'success': False, 'message': 'Совершите сделку'})
    
    c.execute('UPDATE users SET bktok_balance = bktok_balance + ? WHERE id = ?',
              (task['reward'], session['user_id']))
    c.execute('''INSERT OR REPLACE INTO tasks_completed (user_id, task_id, completed_at)
                 VALUES (?, ?, ?)''',
              (session['user_id'], task_id, datetime.utcnow().isoformat()))
    conn.commit()
    
    c.execute('SELECT bktok_balance FROM users WHERE id = ?', (session['user_id'],))
    new_balance = c.fetchone()['bktok_balance']
    conn.close()
    
    return jsonify({
        'success': True, 
        'message': f'+{task["reward"]} BK',
        'reward': task['reward'],
        'new_balance': new_balance
    })

@app.route('/api/cases', methods=['GET'])
@login_required
def get_cases():
    cases = [
        {'id': 'common', 'name': 'Обычный', 'price': 50, 'rewards': [5, 10, 20, 30, 50, 100]},
        {'id': 'rare', 'name': 'Редкий', 'price': 200, 'rewards': [50, 100, 150, 250, 500, 1000]},
        {'id': 'legendary', 'name': 'Легендарный', 'price': 1000, 'rewards': [200, 500, 1000, 2000, 5000, 10000]}
    ]
    return jsonify({'success': True, 'cases': cases})

@app.route('/api/cases/<case_id>/open', methods=['POST'])
@login_required
def open_case(case_id):
    cases_config = {
        'common': {'price': 50, 'rewards': [5, 10, 20, 30, 50, 100]},
        'rare': {'price': 200, 'rewards': [50, 100, 150, 250, 500, 1000]},
        'legendary': {'price': 1000, 'rewards': [200, 500, 1000, 2000, 5000, 10000]}
    }
    
    if case_id not in cases_config:
        return jsonify({'success': False, 'message': 'Кейс не найден'})
    
    case = cases_config[case_id]
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT bktok_balance FROM users WHERE id = ?', (session['user_id'],))
    user = c.fetchone()
    
    if user['bktok_balance'] < case['price']:
        conn.close()
        return jsonify({'success': False, 'message': 'Недостаточно BK'})
    
    win_amount = random.choice(case['rewards'])
    net_change = win_amount - case['price']
    
    c.execute('UPDATE users SET bktok_balance = bktok_balance + ? WHERE id = ?',
              (net_change, session['user_id']))
    conn.commit()
    
    c.execute('SELECT bktok_balance FROM users WHERE id = ?', (session['user_id'],))
    new_balance = c.fetchone()['bktok_balance']
    conn.close()
    
    return jsonify({
        'success': True,
        'win_amount': win_amount,
        'net_change': net_change,
        'new_balance': new_balance,
        'message': f'Выигрыш: {win_amount} BK!'
    })

@app.route('/api/support/chat', methods=['GET'])
@login_required
def get_support_chat():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT sender, message, created_at FROM support_chats 
                 WHERE user_id = ? ORDER BY created_at ASC''', (session['user_id'],))
    messages = [dict(row) for row in c.fetchall()]
    
    if not messages:
        welcome = {'sender': 'ai', 'message': '👋 Здравствуйте! Я нейросеть BK-Bank. Чем могу помочь?', 
                   'created_at': datetime.utcnow().isoformat()}
        messages = [welcome]
    
    conn.close()
    return jsonify({'success': True, 'messages': messages})

@app.route('/api/support/chat', methods=['POST'])
@login_required
def send_support_message():
    data = request.json
    message = data.get('message', '').strip()
    
    if not message:
        return jsonify({'success': False, 'message': 'Сообщение пустое'})
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('INSERT INTO support_chats (user_id, sender, message) VALUES (?, ?, ?)',
              (session['user_id'], 'user', message))
    
    ai_response = "🤔 Я могу помочь с балансом, картами или токенами."
    msg_lower = message.lower()
    
    if 'баланс' in msg_lower:
        c.execute('SELECT bktok_balance FROM users WHERE id = ?', (session['user_id'],))
        balance = c.fetchone()['bktok_balance']
        ai_response = f"💰 Ваш баланс: {balance:.2f} BK."
    elif 'привет' in msg_lower or 'здрав' in msg_lower:
        ai_response = f"👋 Здравствуйте, {session.get('name', 'друг')}! Чем могу помочь?"
    elif 'откат' in msg_lower:
        trade_match = re.search(r'#?(\d+)', msg_lower)
        user_match = re.search(r'с (@?[\w\d]+)', msg_lower) or re.search(r'пользовател[ья] ([\w\d]+)', msg_lower)
        
        if trade_match and user_match:
            target_username = user_match[1].replace('@', '')
            c.execute('SELECT id FROM users WHERE username = ?', (target_username,))
            target = c.fetchone()
            
            if target:
                ai_response = f"✅ Запрос на откат сделки отправлен пользователю @{target_username}."
            else:
                ai_response = f"❌ Пользователь @{target_username} не найден."
        else:
            ai_response = "📝 Укажите: 'откат сделки #НОМЕР с @никнейм'"
    
    c.execute('INSERT INTO support_chats (user_id, sender, message) VALUES (?, ?, ?)',
              (session['user_id'], 'ai', ai_response))
    
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'user_message': {'sender': 'user', 'message': message},
        'ai_response': {'sender': 'ai', 'message': ai_response}
    })

@app.route('/api/users/search', methods=['GET'])
@login_required
def search_users():
    query = request.args.get('q', '').strip()
    
    if not query or len(query) < 2:
        return jsonify({'success': False, 'message': 'Введите минимум 2 символа'})
    
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT id, username, name, avatar FROM users 
                 WHERE (username LIKE ? OR name LIKE ?) AND id != ?
                 LIMIT 20''', 
              (f'%{query}%', f'%{query}%', session['user_id']))
    users = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return jsonify({'success': True, 'users': users})

@app.route('/api/friend-request', methods=['POST'])
@login_required
def send_friend_request():
    data = request.json
    friend_username = data.get('username', '').strip()
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT id FROM users WHERE username = ?', (friend_username,))
    friend = c.fetchone()
    
    if not friend:
        conn.close()
        return jsonify({'success': False, 'message': 'Пользователь не найден'})
    
    if friend['id'] == session['user_id']:
        conn.close()
        return jsonify({'success': False, 'message': 'Нельзя добавить себя в друзья'})
    
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
@login_required
def accept_friend():
    data = request.json
    friend_username = data.get('username', '').strip()
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT id FROM users WHERE username = ?', (friend_username,))
    friend = c.fetchone()
    
    if not friend:
        conn.close()
        return jsonify({'success': False, 'message': 'Пользователь не найден'})
    
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
@login_required
def decline_friend():
    data = request.json
    friend_username = data.get('username', '').strip()
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT id FROM users WHERE username = ?', (friend_username,))
    friend = c.fetchone()
    
    if not friend:
        conn.close()
        return jsonify({'success': False, 'message': 'Пользователь не найден'})
    
    c.execute('''DELETE FROM friends 
                 WHERE user_id = ? AND friend_id = ? AND status = 'pending' ''',
              (friend['id'], session['user_id']))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'message': 'Запрос отклонен'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
