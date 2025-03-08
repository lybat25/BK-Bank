<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БК-Банк - Ваш надежный банк</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Стили для страницы */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212;
            color: #ffffff;
            overflow-y: auto;
        }
        header {
            background: #1f1f1f;
            color: #FFD700;
            padding: 10px 20px;
            box-shadow: 0 2px 10px rgba(255, 215, 0, 0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        nav a {
            margin: 0 15px;
            color: #FFD700;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease;
            cursor: pointer;
        }
        nav a:hover {
            color: #ffcc00;
        }
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
            background: #1e1e1e;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }
        .profile-section {
            display: none;
        }
        .registration-form, .edit-profile-form {
            display: flex;
            flex-direction: column;
            background: #2a2a2a;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 3000;
        }
        .registration-form input, .edit-profile-form input {
            margin-bottom: 10px;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
            font-weight: bold;
        }
        .registration-form button, .edit-profile-form button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
            font-weight: bold;
        }
        .registration-form button:hover, .edit-profile-form button:hover {
            background: #ffcc00;
        }
        .user-profile {
            display: flex;
            align-items: center;
            margin-top: 20px;
            padding: 10px;
            background: #2a2a2a;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        .logout-button {
            margin-left: 10px;
            padding: 5px 10px;
            background: #FFD700;
            color: #000;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }
        .logout-button:hover {
            background: #ffcc00;
        }
        .friend-list, .transaction-history, .notification-list {
            margin-top: 20px;
        }
        .friend-list ul, .transaction-history ul, .notification-list ul {
            list-style-type: none;
            padding: 0;
        }
        .friend-list li, .transaction-history li, .notification-list li {
            padding: 5px 0;
        }
        .add-friend {
            margin-top: 20px;
        }
        .add-friend input {
            margin-right: 10px;
        }
        .transaction-form {
            display: flex;
            flex-direction: column;
            margin-top: 20px;
        }
        .transaction-form input {
            margin-bottom: 10px;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
            font-weight: bold;
        }
        .transaction-form button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
            font-weight: bold;
        }
        .transaction-form button:hover {
            background: #ffcc00;
        }
        .friend-requests {
            margin-top: 20px;
        }
        .friend-requests ul {
            list-style-type: none;
            padding: 0;
        }
        .friend-requests li {
            padding: 5px 0;
        }
        .friend-requests button {
            margin-left: 10px;
            padding: 5px 10px;
            background: #FFD700;
            color: #000;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }
        .friend-requests button:hover {
            background: #ffcc00;
        }
        .notification-list {
            margin-top: 20px;
        }
        .notification-list ul {
            list-style-type: none;
            padding: 0;
        }
        .notification-list li {
            padding: 5px 0;
            color: #FFD700;
        }
        .search-friend {
            margin-top: 20px;
        }
        .search-friend input {
            margin-right: 10px;
        }
        .statistics {
            margin-top: 20px;
        }
        .filter-transactions {
            margin-top: 20px;
        }
        .filter-transactions select {
            margin-right: 10px;
        }
    </style>
</head>
<body>

<header>
    <h1><strong>БК-Банк</strong></h1>
    <nav>
        <a onclick="toggleSection('about')"><strong>Главная</strong></a>
        <a onclick="toggleSection('profile')"><strong>Кабинет</strong></a>
        <a onclick="toggleSection('transactions')"><strong>История транзакций</strong></a>
    </nav>
</header>

<div class="container">
    <div class="about-bank">
        <h2><strong>БК-Банк: Ваш надежный финансовый партнер</strong></h2>
        <p><strong>Мы стремимся сделать каждую Вашу финансовую операцию прозрачной и удобной.</strong></p>
        <button onclick="showRegistrationForm()">Зарегистрироваться</button>
    </div>

    <div class="profile-section"></div>
    <div class="transaction-history" style="display: none;"></div>
</div>

<script>
    window.onload = function() {
        const savedUser      = localStorage.getItem('user');
        if (savedUser     ) {
            const user = JSON.parse(savedUser     );
            showProfile(user.name, user.email);
        } else {
            showRegistrationForm();
        }
    };

    function showRegistrationForm() {
        const registrationForm = document.createElement('div');
        registrationForm.className = 'registration-form';
        registrationForm.innerHTML = 
            `<h2><strong>Регистрация</strong></h2>
            <input type="text" id="name" placeholder="Ваш никнейм" required>
            <input type="email" id="email" placeholder="Ваша электронная почта" required>
            <input type="password" id="password" placeholder="Пароль" required>
            <button onclick="register()">Зарегистрироваться</button>`;
        document.body.appendChild(registrationForm);
    }

    function register() {
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        if (!name || !email || !password) {
            alert("Пожалуйста, заполните все поля.");
            return;
        }

        const user = { name, email, balance: 0, friends: [], friendRequests: [], transactions: [], notifications: [] };
        localStorage.setItem('user', JSON.stringify(user));

        alert(`Добро пожаловать, ${name}!`);
        document.querySelector('.registration-form').remove();
        showProfile(name, email);
    }

    function showProfile(name, email) {
        const profileSection = document.querySelector('.profile-section');
        profileSection.innerHTML = 
            `<h2><strong>Ваш Кабинет</strong></h2>
            <div class="user-profile">
                <span><strong>${name}</strong></span>
                <button class="logout-button" onclick="logout()">Выйти</button>
                <button class="logout-button" onclick="showEditProfileForm()">Редактировать профиль</button>
            </div>
            <p><strong>Email: <a href="mailto:${email}" style="color: #FFD700;">${email}</a></strong></p>
            <p><strong>Баланс: <span id="balance">${getUser Balance()}</span> руб.</strong></p>
            <div class="search-friend">
                <h3><strong>Поиск друга:</strong></h3>
                <input type="text" id="searchFriendName" placeholder="Имя друга" required>
                <button onclick="searchFriend()">Найти</button>
            </div>
            <div class="friend-list">
                <h3><strong>Список друзей:</strong></h3>
                <ul id="friends"></ul>
                <div class="add-friend">
                    <input type="text" id="friendName" placeholder="Имя друга" required>
                    <button onclick="addFriend()">Добавить друга</button>
                </div>
            </div>
            <div class="friend-requests">
                <h3><strong>Запросы в друзья:</strong></h3>
                <ul id="friendRequests"></ul>
            </div>
            <div class="notification-list">
                <h3><strong>Уведомления:</strong></h3>
                <ul id="notifications"></ul>
            </div>
            <div class="transaction-form">
                <h3><strong>Добавить транзакцию:</strong></h3>
                <input type="number" id="transactionAmount" placeholder="Сумма" required>
                <input type="text" id="transactionDescription" placeholder="Описание" required>
                <button onclick="addTransaction()">Добавить транзакцию</button>
            </div>
            <div class="filter-transactions">
                <h3><strong>Фильтр транзакций:</strong></h3>
                <select id="transactionFilter" onchange="filterTransactions()">
                    <option value="all">Все</option>
                    <option value="income">Пополнение</option>
                    <option value="expense">Списание</option>
                </select>
            </div>
            <div class="statistics">
                <h3><strong>Статистика транзакций:</strong></h3>
                <p><strong>Общее количество транзакций: ${getTransactionCount()}</strong></p>
                <p><strong>Общий баланс: ${getTotalBalance()} руб.</strong></p>
            </div>`;
        profileSection.style.display = 'block';

        const user = JSON.parse(localStorage.getItem('user'));
        const friendsList = document.getElementById('friends');
        friendsList.innerHTML = ''; // Очистить список перед добавлением
        user.friends.forEach(friend => {
            const friendItem = document.createElement('li');
            friendItem.textContent = friend;
            const removeButton = document.createElement('button');
            removeButton.textContent = "Удалить";
            removeButton.onclick = () => removeFriend(friend);
            friendItem.appendChild(removeButton);
            friendsList.appendChild(friendItem);
        });

        const friendRequestsList = document.getElementById('friendRequests');
        friendRequestsList.innerHTML = ''; // Очистить список перед добавлением
        user.friendRequests.forEach(request => {
            const requestItem = document.createElement('li');
            requestItem.textContent = request;
            const acceptButton = document.createElement('button');
            acceptButton.textContent = "Принять";
            acceptButton.onclick = () => acceptFriendRequest(request);
            requestItem.appendChild(acceptButton);
            friendRequestsList.appendChild(requestItem);
        });

        const notificationsList = document.getElementById('notifications');
        notificationsList.innerHTML = ''; // Очистить список перед добавлением
        user.notifications.forEach(notification => {
            const notificationItem = document.createElement('li');
            notificationItem.textContent = notification;
            notificationsList.appendChild(notificationItem);
        });
    }

    function getUser Balance() {
        const user = JSON.parse(localStorage.getItem('user'));
        return user.balance;
    }

    function addFriend() {
        const friendName = document.getElementById('friendName').value.trim();
        const user = JSON.parse(localStorage.getItem('user'));

        if (friendName && !user.friends.includes(friendName)) {
            user.friendRequests.push(friendName);
            user.notifications.push(`Запрос в друзья отправлен пользователю ${friendName}.`);
            localStorage.setItem('user', JSON.stringify(user));
            showProfile(user.name, user.email);
            document.getElementById('friendName').value = ''; // Очистить поле ввода
        } else {
            alert("Пользователь уже в списке друзей или имя пустое.");
        }
    }

    function acceptFriendRequest(friendName) {
        const user = JSON.parse(localStorage.getItem('user'));
        user.friends.push(friendName);
        user.friendRequests = user.friendRequests.filter(request => request !== friendName);
        user.notifications.push(`Вы добавили ${friendName} в друзья.`);
        localStorage.setItem('user', JSON.stringify(user));
        showProfile(user.name, user.email);
    }

    function removeFriend(friendName) {
        const user = JSON.parse(localStorage.getItem('user'));
        user.friends = user.friends.filter(friend => friend !== friendName);
        user.notifications.push(`Вы удалили ${friendName} из друзей.`);
        localStorage.setItem('user', JSON.stringify(user));
        showProfile(user.name, user.email);
    }

    function showEditProfileForm() {
        const user = JSON.parse(localStorage.getItem('user'));
        const editProfileForm = document.createElement('div');
        editProfileForm.className = 'edit-profile-form';
        editProfileForm.innerHTML = 
            `<h2><strong>Редактировать профиль</strong></h2>
            <input type="text" id="editName" value="${user.name}" required>
            <input type="email" id="editEmail" value="${user.email}" required>
            <button onclick="saveProfileChanges()">Сохранить изменения</button>
            <button onclick="closeEditProfileForm()">Отмена</button>`;
        document.body.appendChild(editProfileForm);
    }

    function saveProfileChanges() {
        const user = JSON.parse(localStorage.getItem('user'));
        const newName = document.getElementById('editName').value.trim();
        const newEmail = document.getElementById('editEmail').value;

        if (newName && newEmail) {
            user.name = newName;
            user.email = newEmail;
            localStorage.setItem('user', JSON.stringify(user));
            showProfile(user.name, user.email);
            closeEditProfileForm();
        } else {
            alert("Пожалуйста, заполните все поля.");
        }
    }

    function closeEditProfileForm() {
        const editProfileForm = document.querySelector('.edit-profile-form');
        if (editProfileForm) {
            editProfileForm.remove();
        }
    }

    function searchFriend() {
        const searchName = document.getElementById('searchFriendName').value.trim();
        const user = JSON.parse(localStorage.getItem('user'));
        const friendsList = document.getElementById('friends');
        friendsList.innerHTML = ''; // Очистить список перед добавлением

        if (searchName) {
            const foundFriends = user.friends.filter(friend => friend.toLowerCase().includes(searchName.toLowerCase()));
            foundFriends.forEach(friend => {
                const friendItem = document.createElement('li');
                friendItem.textContent = friend;
                friendsList.appendChild(friendItem);
            });

            if (foundFriends.length === 0) {
                const noResultItem = document.createElement('li');
                noResultItem.textContent = "Друзья не найдены.";
                friendsList.appendChild(noResultItem);
            }
        } else {
            alert("Пожалуйста, введите имя для поиска.");
        }
    }

    function showTransactionHistory() {
        const transactionHistory = document.querySelector('.transaction-history');
        const user = JSON.parse(localStorage.getItem('user'));
        transactionHistory.innerHTML = `<h2><strong>История транзакций</strong></h2>`;
        
        if (user.transactions.length === 0) {
            transactionHistory.innerHTML += `<p>Нет транзакций.</p>`;
        } else {
            const ul = document.createElement('ul');
            user.transactions.forEach(transaction => {
                const li = document.createElement('li');
                li.textContent = `${transaction.date}: ${transaction.amount} - ${transaction.description}`;
                li.onclick = () => showTransactionDetails(transaction); // Добавляем обработчик для показа деталей
                ul.appendChild(li);
            });
            transactionHistory.appendChild(ul);
        }
        transactionHistory.style.display = 'block';
    }

    function showTransactionDetails(transaction) {
        alert(`Детали транзакции:\nДата: ${transaction.date}\nСумма: ${transaction.amount}\nОписание: ${transaction.description}`);
    }

    function addTransaction() {
        const amount = parseFloat(document.getElementById('transactionAmount').value);
        const description = document.getElementById('transactionDescription').value.trim();
        const user = JSON.parse(localStorage.getItem('user'));

        if (!isNaN(amount) && description) {
            const transaction = {
                date: new Date().toLocaleString(),
                amount: amount,
                description: description
            };
            user.transactions.push(transaction);
            user.balance += amount; // Обновляем баланс
            user.notifications.push(`Транзакция добавлена: ${description} на сумму ${amount} руб.`);
            localStorage.setItem('user', JSON.stringify(user));
            showProfile(user.name, user.email); // Обновляем профиль
            document.getElementById('transactionAmount').value = ''; // Очистить поле ввода
            document.getElementById('transactionDescription').value = ''; // Очистить поле ввода
        } else {
            alert("Пожалуйста, введите корректные данные для транзакции.");
        }
    }

    function getTransactionCount() {
        const user = JSON.parse(localStorage.getItem('user'));
        return user.transactions.length;
    }

    function getTotalBalance() {
        const user = JSON.parse(localStorage.getItem('user'));
        return user.transactions.reduce((total, transaction) => total + transaction.amount, 0);
    }

    // Пример добавления транзакций
    addTransaction(100, "Пополнение счета");
    addTransaction(-50, "Оплата услуг");
    addTransaction(-20, "Покупка в магазине");
    addTransaction(200, "Перевод от друга");
    addTransaction(-30, "Оплата подписки");

</script>

</body>
</html>
