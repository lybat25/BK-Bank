<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БК-Банк - Ваш надежный банк</title>
    <style>
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
            padding: 15px 30px;
            box-shadow: 0 2px 10px rgba(255, 215, 0, 0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        nav {
            margin: 0;
        }
        nav a {
            margin: 0 20px;
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
        .content {
            padding: 20px;
            margin-bottom: 20px;
            display: none;
            border-radius: 8px;
            background: #2a2a2a;
        }
        .logo {
            width: 120px;
            height: auto;
        }
        h1 {
            font-size: 2.5em;
            margin: 0;
            font-weight: bold;
        }
        h2 {
            color: #FFD700;
            padding-bottom: 10px;
            border-bottom: 2px solid #FFD700;
            font-weight: bold;
        }
        h3 {
            color: #FFD700;
            margin: 20px 0 10px;
            font-weight: bold;
        }
        .yellow-line {
            height: 2px;
            background-color: #FFD700;
            margin-bottom: 10px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 5px 0;
            position: relative;
            font-weight: bold;
        }
        li::before {
            content: '✓';
            color: #FFD700;
            position: absolute;
            left: -20px;
        }
        .about-bank {
            text-align: center;
            margin: 40px 0;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        .contact-info {
            display: none;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            margin-top: 20px;
        }
        .contact-info a {
            color: #FFD700;
            text-decoration: none;
            font-weight: bold;
        }
        .contact-info a:hover {
            color: #ffcc00;
        }
        .services, .cards {
            display: none;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            margin-top: 20px;
        }
        .bank-image {
            margin-top: 20px;
            width: 100%;
            max-width: 600px;
            height: auto;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .welcome-message {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: rgba(31, 31, 31, 0.9);
            color: #FFD700;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
            opacity: 1;
            transition: opacity 1s ease-out;
            z-index: 2000;
            font-weight: bold;
        }
        .fade-out {
            opacity: 0;
        }
        .auth-form {
            display: flex;
            flex-direction: column;
            background: #2a2a2a;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 3000;
            width: 350px;
        }
        .auth-form input {
            margin-bottom: 15px;
            padding: 12px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
            font-weight: bold;
        }
        .auth-form button {
            padding: 12px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .auth-form button:hover {
            background: #ffcc00;
        }
        .auth-form .switch-form {
            text-align: center;
            margin-top: 10px;
            color: #FFD700;
            cursor: pointer;
            font-weight: bold;
        }
        .auth-form .switch-form:hover {
            text-decoration: underline;
        }
        .hidden {
            display: none;
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
        .user-profile img {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
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
        .error-message {
            color: #ff4444;
            margin-bottom: 10px;
            text-align: center;
            font-weight: bold;
        }
    </style>
</head>
<body>

<header class="hidden">
    <h1>
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-11_142359079.png?raw=true" class="logo" alt="Логотип БК-Банк" />
        <strong>БК-Банк</strong>
    </h1>
    <nav>
        <a onclick="toggleSection('about')"><strong>Главная</strong></a>
        <a onclick="toggleSection('services')"><strong>Услуги</strong></a>
        <a onclick="toggleSection('cards')"><strong>Карты</strong></a> 
        <a onclick="toggleSection('contact')"><strong>Контакты</strong></a>
        <a onclick="toggleSection('profile')"><strong>Кабинет</strong></a>
    </nav>
</header>

<div class="container hidden">
    <div class="about-bank">
        <h2><strong>БК-Банк: Ваш надежный финансовый партнер</strong></h2>
        <div class="yellow-line"></div>
        <p><strong>В БК-Банке мы понимаем, что каждая покупка — это не просто транзакция, а часть Вашей жизни. Как говорит наш клиент: "Я ношу карту. И эта карта не прячет мои покупки, но создаёт их оформление." Мы стремимся сделать каждую Вашу финансовую операцию прозрачной и удобной.</strong></p>
        <p><strong>Мы гордимся тем, что предоставляем нашим клиентам не только услуги, но и возможность управлять своими финансами с уверенностью. Один из наших пользователей отметил: "Я всегда утверждал, что стал пользователем БК-Банка, чтобы сражаться с деньгами. Это была ложь."</strong></p>
        
        <h3><strong>Наши продукты</strong></h3>
        <div class="yellow-line"></div>
        <p><strong>Будь на стороне добра! Забудьте про врагов и оформите нашу карту от БК-Банк.</strong></p>
        
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" alt="Изображение о банке" class="bank-image" />
        
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_105015270.png?raw=true" alt="Изображение о банке" class="bank-image" />
        
        <div class="additional-info" style="color: #FFD700;"><strong>Наши карты</strong></div>
        <div class="yellow-line"></div>
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" alt="Наши карты" class="bank-image" />

        <div class="additional-text">
            <strong>Мы верим, что финансовая грамотность — это ключ к свободе. Каждый день мы работаем над тем, чтобы наши клиенты могли принимать обоснованные решения, основанные на чёткой информации. Мы предлагаем инструменты и ресурсы, которые помогут Вам лучше понять свои расходы и сбережения.</strong>
            <br /><br />
            <img src="" style="margin-top: 20px; max-width: 50%; height: auto;" />
        </div>
    </div>

    <div id="services" class="services">
        <h2><strong>Наши услуги</strong></h2>
        <div class="yellow-line"></div>
        <ul>
            <li><strong>Кредитование</strong></li>
            <li><strong>Депозиты</strong></li>
            <li><strong>Инвестиционные услуги</strong></li>
            <li><strong>Консультации по финансовым вопросам</strong></li>
            <li><strong>Онлайн-банкинг</strong></li>
        </ul>
    </div>

    <div id="cards" class="cards">
        <h2><strong>Наши карты</strong></h2>
        <div class="yellow-line"></div>
        <ul>
            <li><strong>Карта "тень и свет"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_092441724.png?raw=true" alt="Карта тень и свет" class="bank-image" />
            <li><strong>Карта "чёрно-жёлтая энергия"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_093348500.png?raw=true" alt="Карта чёрно-жёлтая энергия" class="bank-image" />
            <li><strong>Карта "жёлтая стрела"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_094122593.png?raw=true" alt="Карта жёлтая стрела" class="bank-image" />
            <li><strong>Карта "золотая волна"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_095046740.png?raw=true" alt="Карта золотая волна" class="bank-image" />
            <li><strong>Карта "солнечный ночной ветер"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_100946793.png?raw=true" alt="Карта солнечный ночной ветер" class="bank-image" />
            <li><strong>Карта "БКашная тёмный"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_101740633.png?raw=true" alt="Карта БКашная тёмный" class="bank-image" />
            <li><strong>Карта "БКашная светлый"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_102653372.png?raw=true" alt="Карта БКашная светлый" class="bank-image" />
        </ul>
        <p><strong>Наши карты всё ещё не будут доступны больше пару месяцев, советуем вам использовать нашу Биржу.</strong></p>
    </div>

    <div class="contact-info">
        <h2><strong>Контактная информация</strong></h2>
        <div class="yellow-line"></div>
        <p><strong>Email: <a href="mailto:hgaraew@mail.ru" style="color: #FFD700;">БК-Банк email</a></strong></p>
        <p><strong>Discord:</strong> <a href="https://discord.gg/q8kRuKebKH" target="_blank">БК-Банк server</a></p>
        <p><strong>Telegram:</strong> <a href="https://t.me/+NE8aj5oiHJhjYjgy" target="_blank">БК-Банк channel</a></p>
        <p><strong>YouTube:</strong> <a href="https://www.youtube.com/channel/UCnFbE5v1nzlonhsk9wX16Yw" target="_blank">БК-Банк YouTube</a></p>
        <p><strong>Token:</strong> <a href="ЕСЛИ ТЫ ЭТО ВИДИШЬ ЗНАЧИT ТЫ ОТКРЫЛ ПАСХАЛКУ НАПИШИ МНЕ В ДИСКОРД fa5" target="_blank">БК-Банк Token (ещё не вышел)</a></p>
    </div>

    <div class="profile-section" style="display: none;"></div>
</div>

<script>
    // Глобальные переменные
    let users = JSON.parse(localStorage.getItem('bankUsers')) || {};
    let currentUser = null;

    // Инициализация при загрузке страницы
    window.onload = function() {
        // Проверяем, есть ли активная сессия
        const session = localStorage.getItem('currentSession');
        if (session) {
            const sessionData = JSON.parse(session);
            // Проверяем, не истекла ли сессия (24 часа)
            if (Date.now() - sessionData.timestamp < 24 * 60 * 60 * 1000) {
                currentUser = sessionData.username;
                showMainContent();
                showWelcomeMessage(users[currentUser].name);
                return;
            } else {
                // Удаляем просроченную сессию
                localStorage.removeItem('currentSession');
            }
        }
        
        // Если нет активной сессии, показываем форму входа
        showLoginForm();
    };

    // Показать форму входа
    function showLoginForm() {
        const authForm = document.createElement('div');
        authForm.className = 'auth-form';
        authForm.innerHTML = 
            `<h2 style="text-align: center; color: #FFD700;"><strong>Вход в БК-Банк</strong></h2>
            <div id="loginError" class="error-message hidden"></div>
            <input type="text" id="loginUsername" placeholder="Ваш никнейм" required>
            <input type="password" id="loginPassword" placeholder="Пароль" required>
            <button onclick="login()"><strong>Войти</strong></button>
            <div class="switch-form" onclick="showRegistrationForm()"><strong>Нет аккаунта? Зарегистрироваться</strong></div>`;
        document.body.appendChild(authForm);
    }

    // Показать форму регистрации
    function showRegistrationForm() {
        document.querySelector('.auth-form').remove();
        
        const authForm = document.createElement('div');
        authForm.className = 'auth-form';
        authForm.innerHTML = 
            `<h2 style="text-align: center; color: #FFD700;"><strong>Регистрация в БК-Банк</strong></h2>
            <div id="registerError" class="error-message hidden"></div>
            <input type="text" id="regName" placeholder="Ваше имя" required>
            <input type="text" id="regUsername" placeholder="Ваш никнейм" required>
            <input type="email" id="regEmail" placeholder="Ваша электронная почта" required>
            <input type="password" id="regPassword" placeholder="Пароль (минимум 6 символов)" required>
            <input type="password" id="regConfirmPassword" placeholder="Подтвердите пароль" required>
            <button onclick="register()"><strong>Зарегистрироваться</strong></button>
            <div class="switch-form" onclick="showLoginForm()"><strong>Уже есть аккаунт? Войти</strong></div>`;
        document.body.appendChild(authForm);
    }

    // Функция входа
    function login() {
        const username = document.getElementById('loginUsername').value.trim();
        const password = document.getElementById('loginPassword').value;
        const errorElement = document.getElementById('loginError');
        
        // Проверка введенных данных
        if (!username || !password) {
            showError(errorElement, 'Пожалуйста, заполните все поля');
            return;
        }
        
        // Проверка существования пользователя
        if (!users[username]) {
            showError(errorElement, 'Пользователь с таким никнеймом не найден');
            return;
        }
        
        // Проверка пароля
        if (users[username].password !== password) {
            showError(errorElement, 'Неверный пароль');
            return;
        }
        
        // Успешный вход
        currentUser = username;
        
        // Создаем сессию
        const sessionData = {
            username: username,
            timestamp: Date.now()
        };
        localStorage.setItem('currentSession', JSON.stringify(sessionData));
        
        // Убираем форму и показываем основной контент
        document.querySelector('.auth-form').remove();
        showMainContent();
        showWelcomeMessage(users[username].name);
    }

    // Функция регистрации
    function register() {
        const name = document.getElementById('regName').value.trim();
        const username = document.getElementById('regUsername').value.trim();
        const email = document.getElementById('regEmail').value;
        const password = document.getElementById('regPassword').value;
        const confirmPassword = document.getElementById('regConfirmPassword').value;
        const errorElement = document.getElementById('registerError');
        
        // Проверка заполнения всех полей
        if (!name || !username || !email || !password || !confirmPassword) {
            showError(errorElement, 'Пожалуйста, заполните все поля');
            return;
        }
        
        // Проверка имени (должно содержать хотя бы одну букву)
        const nameRegex = /[a-zA-Zа-яА-ЯЁё]/;
        if (!nameRegex.test(name)) {
            showError(errorElement, 'Имя должно содержать хотя бы одну букву');
            return;
        }
        
        // Проверка никнейма (должен содержать хотя бы одну букву)
        if (!nameRegex.test(username)) {
            showError(errorElement, 'Никнейм должен содержать хотя бы одну букву');
            return;
        }
        
        // Проверка email
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(email)) {
            showError(errorElement, 'Пожалуйста, введите корректный адрес электронной почты');
            return;
        }
        
        // Проверка пароля
        if (password.length < 6) {
            showError(errorElement, 'Пароль должен содержать минимум 6 символов');
            return;
        }
        
        // Проверка совпадения паролей
        if (password !== confirmPassword) {
            showError(errorElement, 'Пароли не совпадают');
            return;
        }
        
        // Проверка существования пользователя
        if (users[username]) {
            showError(errorElement, 'Пользователь с таким никнеймом уже существует');
            return;
        }
        
        // Проверка email на уникальность
        for (const user in users) {
            if (users[user].email === email) {
                showError(errorElement, 'Пользователь с таким email уже существует');
                return;
            }
        }
        
        // Создание нового пользователя
        users[username] = {
            name: name,
            email: email,
            password: password,
            balance: 0,
            friends: [],
            friendRequests: [],
            registrationDate: new Date().toISOString()
        };
        
        // Сохранение в localStorage
        localStorage.setItem('bankUsers', JSON.stringify(users));
        
        // Автоматический вход после регистрации
        currentUser = username;
        
        // Создаем сессию
        const sessionData = {
            username: username,
            timestamp: Date.now()
        };
        localStorage.setItem('currentSession', JSON.stringify(sessionData));
        
        // Убираем форму и показываем основной контент
        document.querySelector('.auth-form').remove();
        showMainContent();
        showWelcomeMessage(name);
    }

    // Показать основной контент
    function showMainContent() {
        document.querySelectorAll('header, .container').forEach(el => el.classList.remove('hidden'));
        toggleSection('about');
    }

    // Показать приветственное сообщение
    function showWelcomeMessage(name) {
        const welcomeMessage = document.createElement('div');
        welcomeMessage.className = 'welcome-message';
        welcomeMessage.innerHTML = `<strong>Добро пожаловать, ${name}! Мы рады видеть вас в БК-Банке.</strong>`;
        document.body.appendChild(welcomeMessage);

        // Удаляем сообщение через 3 секунды
        setTimeout(() => {
            welcomeMessage.classList.add('fade-out');
            setTimeout(() => {
                welcomeMessage.remove();
            }, 1000);
        }, 3000);
    }

    // Показать ошибку
    function showError(element, message) {
        element.textContent = message;
        element.classList.remove('hidden');
        setTimeout(() => {
            element.classList.add('hidden');
        }, 3000);
    }

    // Выход из системы
    function logout() {
        // Удаляем сессию
        localStorage.removeItem('currentSession');
        currentUser = null;
        
        // Скрываем основной контент
        document.querySelectorAll('header, .container').forEach(el => el.classList.add('hidden'));
        
        // Показываем форму входа
        showLoginForm();
    }

    // Показать профиль пользователя
    function showProfile() {
        const user = users[currentUser];
        const profileSection = document.querySelector('.profile-section');
        profileSection.innerHTML = 
            `<h2><strong>Ваш Кабинет</strong></h2>
            <div class="yellow-line"></div>
            <div class="user-profile">
                <img src="https://github.com/lybat25/BK-Bank/blob/main/png/2025-01-30_17-50-13-Photoroom.png?raw=true" alt="Иконка пользователя" style="width: 40px; height: 40px; border-radius: 50%; margin-right: 10px;">
                <span><strong>${user.name}</strong></span>
                <button class="logout-button" onclick="logout()"><strong>Выйти</strong></button>
            </div>
            <p><strong>Никнейм: ${currentUser}</strong></p>
            <p><strong>Email: <a href="mailto:${user.email}" style="color: #FFD700;">${user.email}</a></strong></p>
            <p><strong>Баланс: ${user.balance} ₽</strong></p>
            <p><strong>Дата регистрации: ${new Date(user.registrationDate).toLocaleDateString()}</strong></p>
            
            <div class="add-friend">
                <h3><strong>Добавить в друзья</strong></h3>
                <input type="text" id="friendName" placeholder="Имя или Email друга" required>
                <button onclick="sendFriendRequest()"><strong>Отправить запрос</strong></button>
            </div>
            <div class="friend-list">
                <h3><strong>Список друзей</strong></h3>
                <ul id="friends">${user.friends.length ? user.friends.map(friend => `<li>${friend}</li>`).join('') : '<li>У вас пока нет друзей</li>'}</ul>
            </div>
            <div class="friend-requests">
                <h3><strong>Запросы в друзья</strong></h3>
                <ul id="friendRequests">${user.friendRequests.length ? user.friendRequests.map(request => `
                    <li>${request} 
                        <button onclick="acceptFriendRequest('${request}')">Принять</button>
                        <button onclick="declineFriendRequest('${request}')">Отклонить</button>
                    </li>`).join('') : '<li>Запросов нет</li>'}</ul>
            </div>`;
        profileSection.style.display = 'block';
    }

    // Отправить запрос на дружбу
    function sendFriendRequest() {
        const friendIdentifier = document.getElementById('friendName').value.trim();
        if (!friendIdentifier) {
            alert("Пожалуйста, введите имя или email друга.");
            return;
        }
        
        // Поиск пользователя по имени или email
        let foundUser = null;
        for (const username in users) {
            if (username === friendIdentifier || users[username].email === friendIdentifier) {
                foundUser = username;
                break;
            }
        }
        
        if (!foundUser) {
            alert("Пользователь не найден.");
            return;
        }
        
        if (foundUser === currentUser) {
            alert("Вы не можете добавить себя в друзья.");
            return;
        }
        
        if (users[currentUser].friends.includes(foundUser)) {
            alert("Этот пользователь уже у вас в друзьях.");
            return;
        }
        
        if (users[foundUser].friendRequests.includes(currentUser)) {
            alert("Вы уже отправили запрос этому пользователю.");
            return;
        }
        
        // Добавляем запрос в друзья
        users[foundUser].friendRequests.push(currentUser);
        localStorage.setItem('bankUsers', JSON.stringify(users));
        
        alert(`Запрос в друзья отправлен пользователю ${foundUser}`);
        document.getElementById('friendName').value = '';
    }

    // Принять запрос на дружбу
    function acceptFriendRequest(friendUsername) {
        const user = users[currentUser];
        
        // Удаляем запрос из списка
        user.friendRequests = user.friendRequests.filter(request => request !== friendUsername);
        
        // Добавляем в друзья
        if (!user.friends.includes(friendUsername)) {
            user.friends.push(friendUsername);
        }
        
        // Также добавляем текущего пользователя в друзья к тому, кто отправил запрос
        if (!users[friendUsername].friends.includes(currentUser)) {
            users[friendUsername].friends.push(currentUser);
        }
        
        // Сохраняем изменения
        localStorage.setItem('bankUsers', JSON.stringify(users));
        
        // Обновляем профиль
        showProfile();
        alert(`Вы добавили ${friendUsername} в друзья!`);
    }

    // Отклонить запрос на дружбу
    function declineFriendRequest(friendUsername) {
        users[currentUser].friendRequests = users[currentUser].friendRequests.filter(request => request !== friendUsername);
        localStorage.setItem('bankUsers', JSON.stringify(users));
        showProfile();
        alert(`Запрос от ${friendUsername} отклонен.`);
    }

    // Переключение между разделами
    function toggleSection(section) {
        // Скрываем все секции
        document.querySelectorAll('.about-bank, #services, #cards, .contact-info, .profile-section').forEach(el => {
            el.style.display = 'none';
        });
        
        // Показываем выбранную секцию
        if (section === 'services') {
            document.getElementById('services').style.display = 'block';
        } else if (section === 'cards') {
            document.getElementById('cards').style.display = 'block';
        } else if (section === 'contact') {
            document.querySelector('.contact-info').style.display = 'block';
        } else if (section === 'about') {
            document.querySelector('.about-bank').style.display = 'block';
        } else if (section === 'profile') {
            showProfile();
        }
    }
</script>

</body>
</html>
