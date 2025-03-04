<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БК-Банк - Ваш надежный банк</title>
    <meta name="description" content="БК-Банк - Ваш надежный банк, предлагающий услуги кредитования, депозиты и финансовые консультации.">
    <meta name="keywords" content="БК-Банк, банк, кредитование, депозиты, финансовые услуги">
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212;
            color: #ffffff;
        }
        header {
            background: #1f1f1f;
            color: #FFD700;
            padding: 10px 20px;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        nav a {
            margin: 0 15px;
            color: #FFD700;
            text-decoration: none;
        }
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
            background: #1e1e1e;
            border-radius: 12px;
        }
        .hidden {
            display: none;
        }
        .registration-form, .login-form, .friend-request-form, .edit-profile-form, .comment-form, .transaction-form, .edit-transaction-form {
            display: flex;
            flex-direction: column;
            background: #2a2a2a;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        .registration-form input, .login-form input, .friend-request-form input, .edit-profile-form input, .comment-form input, .transaction-form input, .edit-transaction-form input {
            margin-bottom: 10px;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
        }
        .registration-form button, .login-form button, .friend-request-form button, .edit-profile-form button, .comment-form button, .transaction-form button, .edit-transaction-form button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
        }
        .registration-form button:hover, .login-form button:hover, .friend-request-form button:hover, .edit-profile-form button:hover, .comment-form button:hover, .transaction-form button:hover, .edit-transaction-form button:hover {
            background: #ffcc00;
        }
        .transaction-history, .notification {
            margin-top: 20px;
            background: #2a2a2a;
            padding: 10px;
            border-radius: 8px;
        }
        .transaction, .notification-item {
            margin: 5px 0;
            padding: 5px;
            border: 1px solid #FFD700;
            border-radius: 4px;
            cursor: pointer;
        }
        .friend-list, .friend-requests {
            margin-top: 20px;
            background: #2a2a2a;
            padding: 10px;
            border-radius: 8px;
        }
        .friend {
            margin: 5px 0;
            padding: 5px;
            border: 1px solid #FFD700;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
        }
        .balance {
            margin-top: 20px;
            font-size: 1.2em;
            color: #FFD700;
        }
    </style>
</head>
<body>

<header>
    <h1>БК-Банк</h1>
    <nav>
        <a onclick="toggleSection('about')">Главная</a>
        <a onclick="toggleSection('services')">Услуги</a>
        <a onclick="toggleSection('cards')">Карты</a>
        <a onclick="toggleSection('contact')">Контакты</a>
        <a onclick="toggleSection('profile')">Кабинет</a>
    </nav>
</header>

<div class="container">
    <div id="about" class="about-bank">
        <h2>БК-Банк: Ваш надежный финансовый партнер</h2>
        <p>В БК-Банке мы понимаем, что каждая покупка — это не просто транзакция, а часть Вашей жизни.</p>
    </div>

    <div id="services" class="services hidden">
        <h2>Наши услуги</h2>
        <ul>
            <li>Кредитование</li>
            <li>Депозиты</li>
            <li>Инвестиционные услуги</li>
            <li>Консультации по финансовым вопросам</li>
            <li>Онлайн-банкинг</li>
        </ul>
    </div>

    <div id="cards" class="cards hidden">
        <h2>Наши карты</h2>
        <ul>
            <li>Карта "тень и свет"</li>
            <li>Карта "чёрно-жёлтая энергия"</li>
            <li>Карта "жёлтая стрела"</li>
        </ul>
    </div>

    <div id="contact" class="contact-info hidden">
        <h2>Контактная информация</h2>
        <p>Email: <a href="mailto:bkbank636@gmail.com">bkbank636@gmail.com</a></p>
    </div>

    <div id="profile" class="profile-section hidden">
        <h2>Ваш Кабинет</h2>
        <div class="user-profile hidden"></div>
        <div class="balance hidden">Баланс: <span id="balance">0</span> руб.</div>
        <div class="friend-request-form hidden">
            <h3>Отправить запрос в друзья</h3>
            <input type="text" id="friend-name" placeholder="Имя друга" required>
            <button onclick="sendFriendRequest()">Отправить запрос</button>
        </div>
        <div class="friend-list hidden">
            <h3>Список друзей</h3>
            <div id="friends"></div>
        </div>
        <div class="friend-requests hidden">
            <h3>Запросы в друзья</h3>
            <div id="friend-requests"></div>
        </div>
        <div class="transaction-history hidden">
            <h3>История транзакций</h3>
            <div id="transactions"></div>
            <div class="comment-form hidden">
                <h4>Добавить комментарий к транзакции</h4>
                <input type="text" id="transaction-comment" placeholder="Комментарий" required>
                <button onclick="addComment()">Добавить комментарий</button>
            </div>
            <div class="transaction-form hidden">
                <h4>Добавить транзакцию</h4>
                <input type="text" id="transaction-description" placeholder="Описание" required>
                <input type="number" id="transaction-amount" placeholder="Сумма" required>
                <select id="transaction-type">
                    <option value="incoming">Входящая</option>
                    <option value="outgoing">Исходящая</option>
                </select>
                <button onclick="addTransactionWithType()">Добавить транзакцию</button>
            </div>
        </div>
        <div class="notification hidden">
            <h3>Уведомления</h3>
            <div id="notifications"></div>
        </div>
        <button onclick="showEditProfileForm()">Редактировать профиль</button>
    </div>

    <div class="registration-form hidden">
        <h2>Регистрация</h2>
        <input type="text" id="reg-name" placeholder="Ваш никнейм" required>
        <input type="email" id="reg-email" placeholder="Ваша электронная почта" required>
        <input type="password" id="reg-password" placeholder="Пароль" required>
        <button onclick="register()">Зарегистрироваться</button>
    </div>

    <div class="login-form hidden">
        <h2>Вход</h2>
        <input type="email" id="login-email" placeholder="Ваша электронная почта" required>
        <input type="password" id="login-password" placeholder="Пароль" required>
        <button onclick="login()">Войти</button>
    </div>

    <div class="edit-profile-form hidden">
        <h2>Редактировать профиль</h2>
        <input type="text" id="edit-name" placeholder="Ваш никнейм" required>
        <input type="email" id="edit-email" placeholder="Ваша электронная почта" required>
        <button onclick="updateProfile()">Сохранить изменения</button>
    </div>

    <div class="edit-transaction-form hidden">
        <h2>Редактировать транзакцию</h2>
        <input type="text" id="edit-transaction-description" placeholder="Новое описание" required>
        <input type="number" id="edit-transaction-amount" placeholder="Новая сумма" required>
        <select id="edit-transaction-type">
            <option value="incoming">Входящая</option>
            <option value="outgoing">Исходящая</option>
        </select>
        <button onclick="updateTransaction()">Сохранить изменения</button>
    </div>
</div>

<script>
    let currentTransactionIndex = null; // Индекс текущей редактируемой транзакции

    window.onload = function() {
        const savedUser      = localStorage.getItem('user');
        if (savedUser     ) {
            const user = JSON.parse(savedUser     );
            showProfile(user.name, user.email);
        } else {
            showRegistrationForm();
        }
        toggleSection('about');
    };

    function toggleSection(section) {
        const sections = ['about', 'services', 'cards', 'contact', 'profile'];
        sections.forEach(sec => {
            document.getElementById(sec).classList.add('hidden');
        });
        document.getElementById(section).classList.remove('hidden');
    }

    function showRegistrationForm() {
        document.querySelector('.registration-form').classList.remove('hidden');
        document.querySelector('.login-form').classList.add('hidden');
    }

    function showLoginForm() {
        document.querySelector('.login-form').classList.remove('hidden');
        document.querySelector('.registration-form').classList.add('hidden');
    }

    function register() {
        const name = document.getElementById('reg-name').value.trim();
        const email = document.getElementById('reg-email').value;
        const password = document.getElementById('reg-password').value;

        if (name && email && password) {
            const user = { name, email, password, friends: [], friendRequests: [], transactions: [], balance: 0 };
            localStorage.setItem('user', JSON.stringify(user));
            alert('Регистрация успешна!');
            showProfile(name, email);
        } else {
            alert('Пожалуйста, заполните все поля.');
        }
    }

    function login() {
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        const savedUser      = localStorage.getItem('user');

        if (savedUser     ) {
            const user = JSON.parse(savedUser     );
            if (user.email === email && user.password === password) {
                alert('Вход успешен!');
                showProfile(user.name, user.email);
            } else {
                alert('Неверный email или пароль.');
            }
        } else {
            alert('Пользователь не найден. Пожалуйста, зарегистрируйтесь.');
        }
    }

    function showProfile(name, email) {
        const profileSection = document.querySelector('.profile-section');
        profileSection.innerHTML = `
            <h2>Ваш Кабинет</h2>
            <p>Имя: ${name}</p>
            <p>Email: ${email}</p>
            <p class="balance">Баланс: <span id="balance">0</span> руб.</p>
        `;
        profileSection.classList.remove('hidden');
        document.querySelector('.registration-form').classList.add('hidden');
        document.querySelector('.login-form').classList.add('hidden');
        document.querySelector('.friend-request-form').classList.remove('hidden');
        document.querySelector('.friend-list').classList.remove('hidden');
        document.querySelector('.friend-requests').classList.remove('hidden');
        document.querySelector('.transaction-history').classList.remove('hidden');
        document.querySelector('.notification').classList.remove('hidden');
        displayFriends();
        displayFriendRequests();
        displayTransactions();
        displayNotifications();
        updateBalance();
    }

    function updateBalance() {
        const user = JSON.parse(localStorage.getItem('user'));
        const balance = user.transactions.reduce((acc, transaction) => acc + transaction.amount, 0);
        user.balance = balance;
        localStorage.setItem('user', JSON.stringify(user));
        document.getElementById('balance').innerText = balance;
    }

    function sendFriendRequest() {
        const friendName = document.getElementById('friend-name').value.trim();
        const user = JSON.parse(localStorage.getItem('user'));

        if (friendName) {
            user.friendRequests.push(friendName);
            localStorage.setItem('user', JSON.stringify(user));
            alert(`Запрос в друзья отправлен пользователю ${friendName}`);
            document.getElementById('friend-name').value = '';
            displayFriendRequests();
            addNotification(`Запрос в друзья отправлен пользователю ${friendName}`);
        } else {
            alert("Пожалуйста, введите имя друга.");
        }
    }

    function displayFriends() {
        const user = JSON.parse(localStorage.getItem('user'));
        const friendsDiv = document.getElementById('friends');
        friendsDiv.innerHTML = '';

        if (user.friends.length === 0) {
            friendsDiv.innerHTML = '<p>Нет друзей.</p>';
            return;
        }

        user.friends.forEach(friend => {
            const friendDiv = document.createElement('div');
            friendDiv.className = 'friend';
            friendDiv.innerText = friend;
            const removeButton = document.createElement('button');
            removeButton.innerText = 'Удалить';
            removeButton.onclick = () => removeFriend(friend);
            friendDiv.appendChild(removeButton);
            friendsDiv.appendChild(friendDiv);
        });
    }

    function removeFriend(friendName) {
        const user = JSON.parse(localStorage.getItem('user'));
        user.friends = user.friends.filter(friend => friend !== friendName);
        localStorage.setItem('user', JSON.stringify(user));
        alert(`Вы удалили ${friendName} из друзей.`);
        displayFriends();
    }

    function displayFriendRequests() {
        const user = JSON.parse(localStorage.getItem('user'));
        const requestsDiv = document.getElementById('friend-requests');
        requestsDiv.innerHTML = '';

        if (user.friendRequests.length === 0) {
            requestsDiv.innerHTML = '<p>Нет запросов в друзья.</p>';
            return;
        }

        user.friendRequests.forEach(request => {
            const requestDiv = document.createElement('div');
            requestDiv.className = 'friend';
            requestDiv.innerText = request;
            const acceptButton = document.createElement('button');
            acceptButton.innerText = 'Принять';
            acceptButton.onclick = () => acceptFriendRequest(request);
            requestDiv.appendChild(acceptButton);
            requestsDiv.appendChild(requestDiv);
        });
    }

    function acceptFriendRequest(friendName) {
        const user = JSON.parse(localStorage.getItem('user'));
        user.friendRequests = user.friendRequests.filter(request => request !== friendName);
        user.friends.push(friendName);
        localStorage.setItem('user', JSON.stringify(user));
        alert(`Вы добавили ${friendName} в друзья!`);
        displayFriends();
        displayFriendRequests();
        addNotification(`Вы добавили ${friendName} в друзья!`);
    }

    function displayTransactions() {
        const user = JSON.parse(localStorage.getItem('user'));
        const transactionsDiv = document.getElementById('transactions');
        transactionsDiv.innerHTML = '';

        if (user.transactions.length === 0) {
            transactionsDiv.innerHTML = '<p>Нет транзакций.</p>';
            return;
        }

        user.transactions.forEach((transaction, index) => {
            const transactionDiv = document.createElement('div');
            transactionDiv.className = 'transaction';
            transactionDiv.innerText = `Транзакция: ${transaction.description}, Сумма: ${transaction.amount} руб.`;
            transactionDiv.onclick = () => showEditTransactionForm(index);
            transactionsDiv.appendChild(transactionDiv);
        });
    }

    function addTransactionWithType() {
        const description = document.getElementById('transaction-description').value.trim();
        const amount = parseFloat(document.getElementById('transaction-amount').value);
        const type = document.getElementById('transaction-type').value;
        const user = JSON.parse(localStorage.getItem('user'));

        if (description && !isNaN(amount)) {
            const transactionAmount = type === 'incoming' ? amount : -amount;
            user.transactions.push({ description, amount: transactionAmount });
            localStorage.setItem('user', JSON.stringify(user));
            alert('Транзакция добавлена!');
            displayTransactions();
            updateBalance();
            document.getElementById('transaction-description').value = '';
            document.getElementById('transaction-amount').value = '';
        } else {
            alert('Пожалуйста, заполните все поля корректно.');
        }
    }

    function showEditTransactionForm(index) {
        const user = JSON.parse(localStorage.getItem('user'));
        const transaction = user.transactions[index];
        currentTransactionIndex = index; // Сохраняем индекс редактируемой транзакции
        document.getElementById('edit-transaction-description').value = transaction.description;
        document.getElementById('edit-transaction-amount').value = Math.abs(transaction.amount);
        document.getElementById('edit-transaction-type').value = transaction.amount > 0 ? 'incoming' : 'outgoing';
        document.querySelector('.edit-transaction-form').classList.remove('hidden');
    }

    function updateTransaction() {
        const user = JSON.parse(localStorage.getItem('user'));
        const description = document.getElementById('edit-transaction-description').value.trim();
        const amount = parseFloat(document.getElementById('edit-transaction-amount').value);
        const type = document.getElementById('edit-transaction-type').value;
        
        if (description && !isNaN(amount)) {
            const transactionAmount = type === 'incoming' ? amount : -amount;
            user.transactions[currentTransactionIndex] = { description, amount: transactionAmount };
            localStorage.setItem('user', JSON.stringify(user));
            alert('Транзакция обновлена!');
            displayTransactions();
            updateBalance();
            document.querySelector('.edit-transaction-form').classList.add('hidden');
        } else {
            alert('Пожалуйста, заполните все поля корректно.');
        }
    }

    function addComment() {
        const comment = document.getElementById('transaction-comment').value.trim();
        const user = JSON.parse(localStorage.getItem('user'));
        if (comment) {
            addTransaction(comment, 0); // Добавляем транзакцию с комментарием
            document.getElementById('transaction-comment').value = '';
            alert('Комментарий добавлен!');
        } else {
            alert('Пожалуйста, введите комментарий.');
        }
    }

    function showEditProfileForm() {
        const user = JSON.parse(localStorage.getItem('user'));
        document.getElementById('edit-name').value = user.name;
        document.getElementById('edit-email').value = user.email;
        document.querySelector('.edit-profile-form').classList.remove('hidden');
    }

    function updateProfile() {
        const user = JSON.parse(localStorage.getItem('user'));
        user.name = document.getElementById('edit-name').value.trim();
        user.email = document.getElementById('edit-email').value;
        localStorage.setItem('user', JSON.stringify(user));
        alert('Профиль обновлен!');
        showProfile(user.name, user.email);
        document.querySelector('.edit-profile-form').classList.add('hidden');
    }

    function addNotification(message) {
        const notificationsDiv = document.getElementById('notifications');
        const notificationDiv = document.createElement('div');
        notificationDiv.className = 'notification-item';
        notificationDiv.innerText = message;
        notificationsDiv.appendChild(notificationDiv);
    }

    function displayNotifications() {
        const user = JSON.parse(localStorage.getItem('user'));
        const notificationsDiv = document.getElementById('notifications');
        notificationsDiv.innerHTML = '';

        if (user.notifications && user.notifications.length > 0) {
            user.notifications.forEach(notification => {
                const notificationDiv = document.createElement('div');
                notificationDiv.className = 'notification-item';
                notificationDiv.innerText = notification;
                notificationsDiv.appendChild(notificationDiv);
            });
        } else {
            notificationsDiv.innerHTML = '<p>Нет уведомлений.</p>';
        }
    }

    // Пример добавления транзакций
    addTransactionWithType('Пополнение счета', 1000, 'incoming');
    addTransactionWithType('Снятие наличных', -500, 'outgoing');
    addTransactionWithType('Перевод другу', -200, 'outgoing');
</script>

</body>
</html>
