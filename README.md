<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BC-Bank - Ваш надежный банк</title>
    <base href="http://www.BK-Bank.com/mypage.html">
    <link rel="stylesheet" href="styles.css">
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
            padding: 10px 20px;
            box-shadow: 0 2px 10px rgba(255, 215, 0, 0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }
        nav {
            margin: 0;
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
        .content {
            padding: 20px;
            margin-bottom: 20px;
            display: none;
            border-radius: 8px;
            background: #2a2a2a;
        }
        .logo {
            width: 100px;
            height: auto;
        }
        h1 {
            font-size: 2.5em;
            margin: 0;
        }
        h2 {
            color: #FFD700;
            border-bottom: 2px solid #FFD700;
            padding-bottom: 10px;
        }
        h3 {
            color: #FFD700;
            margin: 20px 0 10px;
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
        }
        .fade-out {
            opacity: 0;
        }
        .registration-form {
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
        .registration-form input {
            margin-bottom: 10px;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
        }
        .registration-form button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
            font-weight: bold;
        }
        .registration-form button:hover {
            background: #ffcc00;
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
        .additional-info {
            text-align: center;
            margin: 20px 0;
            font-size: 1.5em;
            color: #FFD700;
        }
        .additional-text {
            text-align: center;
            margin: 20px 0;
            font-size: 1em;
            color: #ffffff;
            padding: 0 20px;
        }
        .profile-section {
            display: none;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
    <script>
        window.onload = function() {
            const savedUser  = localStorage.getItem('user');
            if (savedUser ) {
                const user = JSON.parse(savedUser );
                showProfile(user.name, user.email, user.balance);
            } else {
                document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden'));
                showRegistrationForm();
            }
            document.querySelector('.profile-section').style.display = 'none';
        };

        function showRegistrationForm() {
            const registrationForm = document.createElement('div');
            registrationForm.className = 'registration-form';
            registrationForm.innerHTML = `
                <h2>Регистрация</h2>
                <input type="text" id="name" placeholder="Ваш никнейм" required>
                <input type="email" id="email" placeholder="Ваша электронная почта" required>
                <input type="password" id="password" placeholder="Пароль" required>
                <button onclick="register()">Зарегистрироваться</button>
            `;
            document.body.appendChild(registrationForm);
        }

        function register() {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const nameRegex = /[a-zA-Zа-яА-ЯЁё]/;
            if (!nameRegex.test(name)) {
                alert("Никнейм должен содержать хотя бы одну букву.");
                return;
            }

            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!emailRegex.test(email)) {
                alert("Пожалуйста, введите корректный адрес электронной почты.");
                return;
            }

            if (password.length < 6) {
                alert("Пароль должен содержать минимум 6 символов.");
                return;
            }

            const user = {
                name: name,
                email: email,
                balance: 0
            };
            localStorage.setItem('user', JSON.stringify(user));

            const welcomeMessage = document.createElement('div');
            welcomeMessage.className = 'welcome-message';
            welcomeMessage.innerText = `Добро пожаловать, ${name}! Мы рады видеть вас на нашем сайте.`;
            document.body.appendChild(welcomeMessage);

            document.querySelector('.registration-form').remove();
            document.querySelectorAll('.hidden').forEach(el => el.classList.remove('hidden'));

            setTimeout(() => {
                welcomeMessage.classList.add('fade-out');
                setTimeout(() => {
                    welcomeMessage.remove();
                }, 1000);
            }, 2000);
        }

        function showProfile(name, email, balance) {
            const profileSection = document.querySelector('.profile-section');
            profileSection.innerHTML = `
                <h2>Ваш Кабинет</h2>
                <div class="user-profile">
                    <img src="https://github.com/lybat25/BC-Bank/blob/main/png/2025-01-30_17-50-13-Photoroom.png?raw=true" alt="Иконка пользователя">
                    <span>${name}</span>
                    <button class="logout-button" onclick="logout()">Выйти</button>
                </div>
                <p>Email: ${email}</p>
                <p>Ваш текущий баланс: <span id="currentBalance">${balance}</span> рублей.</p>
                <h3>Пополнить баланс</h3>
                <input type="number" id="depositAmount" placeholder="Сумма для пополнения" min="1">
                <button onclick="deposit()">Пополнить</button>
            `;
            profileSection.style.display = 'block';
        }

        function deposit() {
            const depositAmount = parseFloat(document.getElementById('depositAmount').value);
            const user = JSON.parse(localStorage.getItem('user'));

            if (isNaN(depositAmount) || depositAmount <= 0) {
                alert("Пожалуйста, введите корректную сумму для пополнения.");
                return;
            }

            user.balance += depositAmount;
            localStorage.setItem('user', JSON.stringify(user));
            document.getElementById('currentBalance').innerText = user.balance;
            document.getElementById('depositAmount').value = ''; // Очистить поле ввода
            alert(`Баланс успешно пополнен на ${depositAmount} рублей.`);
        }

        function logout() {
            localStorage.removeItem('user');
            document.querySelector('.profile-section').style.display = 'none';
            document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden'));
            showRegistrationForm();
        }

        function toggleSection(section) {
            const services = document.getElementById('services');
            const cards = document.getElementById('cards');
            const contact = document.querySelector('.contact-info');
            const about = document.querySelector('.about-bank');
            const profile = document.querySelector('.profile-section');

            services.style.display = 'none';
            cards.style.display = 'none';
            contact.style.display = 'none';
            about.style.display = 'none';
            profile.style.display = 'none';

            if (section === 'services') {
                services.style.display = 'block';
            } else if (section === 'cards') {
                cards.style.display = 'block';
            } else if (section === 'contact') {
                contact.style.display = 'block';
            } else if (section === 'about') {
                about.style.display = 'block';
            } else if (section === 'profile') {
                profile.style.display = 'block';
            }
        }
    </script>
</head>
<body>

<header>
    <h1>
        <img src="https://github.com/lybat25/BC-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-11_142359079.png?raw=true" class="logo" alt="Логотип BC-Bank">
        <a href="https://lybat25.github.io/BC-Bank/" style="color: #FFD700;">BC-Bank</a>
    </h1>
    <nav>
        <a onclick="toggleSection('about')">Главная</a>
        <a onclick="toggleSection('services')">Услуги</a>
        <a onclick="toggleSection('cards')">Карты</a>
        <a onclick="toggleSection('contact')">Контакты</a>
        <a onclick="toggleSection('profile')">Кабинет</a>
    </nav>
</header>

<div class="container">
    <div class="about-bank">
        <h2>БК-Банк: Ваш надежный финансовый партнер</h2>
        <p>В БК-Банке мы понимаем, что каждая покупка — это не просто транзакция, а часть Вашей жизни. Как говорит наш клиент: "Я ношу карту. И эта карта не прячет мои покупки, но создаёт их оформление." Мы стремимся сделать каждую Вашу финансовую операцию прозрачной и удобной.</p>
        <p>Мы гордимся тем, что предоставляем нашим клиентам не только услуги, но и возможность управлять своими финансами с уверенностью. Один из наших пользователей отметил: "Я всегда утверждал, что стал пользователем БК-Банка, чтобы сражаться с деньгами. Это была ложь."</p>
        
        <h3 style="color: #FFD700;">Наши продукты</h3>
        <div class="yellow-line"></div>
        <p>Будь на стороне добра! Забудьте про врагов и оформите нашу карту от BK-Bank.</p>
        
        <img src="https://github.com/lybat25/BC-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" alt="Изображение о банке" class="bank-image">
        
        <img src="https://github.com/lybat25/BC-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_105015270.png?raw=true" alt="Изображение о банке" class="bank-image">
        
        <div class="additional-info" style="color: #FFD700;">Наши карты</div>
        <div class="yellow-line"></div>
        <img src="https://github.com/lybat25/BC-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" alt="Наши карты" class="bank-image">

        <div class="additional-text">
            Мы верим, что финансовая грамотность — это ключ к свободе. Каждый день мы работаем над тем, чтобы наши клиенты могли принимать обоснованные решения, основанные на чёткой информации. Мы предлагаем инструменты и ресурсы, которые помогут Вам лучше понять свой расходы и сбережения.
            <br><br>
            <img src="" style="margin-top: 20px; max-width: 50%; height: auto;">
        </div>
    </div>

    <div id="services" class="services">
        <h2>Наши услуги</h2>
        <ul>
            <li>Кредитование</li>
            <li>Депозиты</li>
            <li>Инвестиционные услуги</li>
            <li>Консультации по финансовым вопросам</li>
            <li>Онлайн-банкинг</li>
        </ul>
    </div>

    <div id="cards" class="cards">
        <h2>Наши карты</h2>
        <ul>
            <li>Карта "тень и свет"</li>
            <li>Карта "чёрно-жёлтая энергия"</li>
            <li>Карта "жёлтая стрела"</li>
            <li>Карта "золотая волна"</li>
            <li>Карта "солнечный ночной ветер"</li>
            <li>Карта "БКашная тёмный"</li>
            <li>Карта "БКашная светлый"</li>
        </ul>
        <p>Наши карты всё ещё не будут доступны больше пару месяцев советуем вам использовать нашу Биржу</p>
    </div>

    <div class="contact-info">
        <h2>Контактная информация</h2>
        <p>Email: <a href="mailto:bkbank636@gmail.com">bkbank636@gmail.com</a></p>
        <p>Discord: <a href="https://discord.gg/q8kRuKebKH" target="_blank">BK-Bank server</a></p>
        <p>Telegram: <a href="https://t.me/+NE8aj5oiHJhjYjgy" target="_blank">BK-Bank channel</a></p>
        <p>YouTube: <a href="https://www.youtube.com/channel/UCnFbE5v1nzlonhsk9wX16Yw" target="_blank">BK-Bank YouTube</a></p>
        <p>Token: <a href="ЕСЛИ ТЫ ЭТО ВИДИШЬ ЗНАЧИТ ТЫ ОТКРЫЛ ПАСХАЛКУ НАПИШИ МНЕ В ДИСКОРД fa5" target="_blank">BK-Bank Token (ещё не вышел)</a></p>
    </div>

    <div class="profile-section" style="display: none;">
        <h2>Ваш Кабинет</h2>
        <div class="user-profile">
            <img src="https://github.com/lybat25/BC-Bank/blob/main/png/2025-01-30_17-50-13-Photoroom.png?raw=true" alt="Иконка пользователя">
            <span id="userName"></span>
            <button class="logout-button" onclick="logout()">Выйти</button>
        </div>
        <p>Email: <span id="userEmail"></span></p>
        <p>Ваш текущий баланс: <span id="currentBalance">0</span> рублей.</p>
    </div>
</div>

</body>
</html>
