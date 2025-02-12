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
        .deposit-form {
            display: none; /* Скрываем форму пополнения по умолчанию */
            background: #2a2a2a;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
            margin-top: 20px;
        }
        .deposit-form input {
            margin-bottom: 10px;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
        }
        .deposit-form button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
            font-weight: bold;
        }
        .deposit-form button:hover {
            background: #ffcc00;
        }
        /* Остальные стили остаются прежними */
        /* ... */
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
                    <button class="deposit-button" onclick="showDepositForm()">Пополнить баланс</button> <!-- Кнопка для пополнения баланса -->
                </div>
                <p>Email: ${email}</p>
                <p>Ваш текущий баланс: <span id="currentBalance">${balance}</span> рублей.</p>
            `;
            profileSection.style.display = 'block';
        }

        function logout() {
            localStorage.removeItem('user');
            document.querySelector('.profile-section').style.display = 'none';
            document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden'));
            showRegistrationForm();
        }

        function showDepositForm() {
            const depositForm = document.createElement('div');
            depositForm.className = 'deposit-form';
            depositForm.innerHTML = `
                <h2>Пополнение баланса</h2>
                <input type="text" id="cardNumber" placeholder="Номер карты" required>
                <input type="number" id="amount" placeholder="Сумма пополнения" required>
                <button onclick="deposit()">Пополнить</button>
                <button onclick="hideDepositForm()">Отмена</button>
            `;
            document.body.appendChild(depositForm);
            depositForm.style.display = 'block'; // Показываем форму
        }

        function hideDepositForm() {
            const depositForm = document.querySelector('.deposit-form');
            if (depositForm) {
                depositForm.remove(); // Удаляем форму
            }
        }

        function deposit() {
            const cardNumber = document.getElementById('cardNumber').value.trim();
            const amount = parseFloat(document.getElementById('amount').value);

            // Простейшая проверка номера карты (должен состоять из 16 цифр)
            const cardRegex = /^\d{16}$/;
            if (!cardRegex.test(cardNumber)) {
                alert("Номер карты должен состоять из 16 цифр.");
                return;
            }

            // Проверка суммы пополнения
            if (isNaN(amount) || amount <= 0) {
                alert("Введите корректную сумму для пополнения.");
                return;
            }

            // Получаем данные пользователя из localStorage
            const savedUser  = localStorage.getItem('user');
            if (savedUser ) {
                const user = JSON.parse(savedUser );
                user.balance += amount; // Увеличиваем баланс
                localStorage.setItem('user', JSON.stringify(user)); // Сохраняем обновленные данные

                alert(`Баланс успешно пополнен на ${amount} рублей!`);
                hideDepositForm(); // Скрываем форму пополнения
                showProfile(user.name, user.email, user.balance); // Обновляем профиль
            }
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

        // Дополнительные функции для улучшения пользовательского интерфейса
        function showError(message) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.innerText = message;
            document.body.appendChild(errorDiv);
            setTimeout(() => {
                errorDiv.remove();
            }, 3000);
        }

        function validateCardNumber(cardNumber) {
            // Простейшая проверка номера карты (должен состоять из 16 цифр)
            const cardRegex = /^\d{16}$/;
            return cardRegex.test(cardNumber);
        }

        function validateAmount(amount) {
            // Проверка суммы пополнения
            return !isNaN(amount) && amount > 0;
        }

        function validateUser Input(name, email, password) {
            const nameRegex = /[a-zA-Zа-яА-ЯЁё]/;
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

            if (!nameRegex.test(name)) {
                showError("Никнейм должен содержать хотя бы одну букву.");
                return false;
            }

            if (!emailRegex.test(email)) {
                showError("Пожалуйста, введите корректный адрес электронной почты.");
                return false;
            }

            if (password.length < 6) {
                showError("Пароль должен содержать минимум 6 символов.");
                return false;
            }

            return true;
        }

        function resetFormInputs() {
            document.getElementById('name').value = '';
            document.getElementById('email').value = '';
            document.getElementById('password').value = '';
            document.getElementById('cardNumber').value = '';
            document.getElementById('amount').value = '';
        }

        // Функция для отображения приветственного сообщения
        function showWelcomeMessage(name) {
            const welcomeMessage = document.createElement('div');
            welcomeMessage.className = 'welcome-message';
            welcomeMessage.innerText = `Добро пожаловать, ${name}! Мы рады видеть вас на нашем сайте.`;
            document.body.appendChild(welcomeMessage);

            setTimeout(() => {
                welcomeMessage.classList.add('fade-out');
                setTimeout(() => {
                    welcomeMessage.remove();
                }, 1000);
            }, 2000);
        }

        // Функция для обновления профиля
        function updateProfile(user) {
            const profileSection = document.querySelector('.profile-section');
            profileSection.querySelector('span').innerText = user.name;
            profileSection.querySelector('#currentBalance').innerText = user.balance;
        }

        // Функция для инициализации приложения
        function initApp() {
            const savedUser  = localStorage.getItem('user');
            if (savedUser ) {
                const user = JSON.parse(savedUser );
                showProfile(user.name, user.email, user.balance);
            } else {
                showRegistrationForm();
            }
        }

        // Запуск приложения
        initApp();
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
            <span>${name}</span>
            <button class="logout-button" onclick="logout()">Выйти</button>
            <button class="deposit-button" onclick="showDepositForm()">Пополнить баланс</button> <!-- Кнопка для пополнения баланса -->
        </div>
        <p>Email: <span id="userEmail"></span></p>
        <p>Ваш текущий баланс: <span id="currentBalance">0</span> рублей.</p>
    </div>
</div>

</body>
</html>
