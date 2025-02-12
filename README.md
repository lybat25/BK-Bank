<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BC-Bank - Ваш надежный банк</title>
    <base href="http://www.BK-Bank.com/mypage.html"> <!-- Базовый URL для относительных ссылок -->
    <link rel="stylesheet" href="styles.css"> <!-- Подключите свой CSS файл -->
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212; /* Темный фон */
            color: #ffffff; /* Белый текст */
            overflow-y: auto; /* Включает вертикальную прокрутку */
        }
        header {
            background: #1f1f1f; /* Темно-серый фон */
            color: #FFD700; /* Желтый текст */
            padding: 10px 20px; /* Увеличены отступы */
            box-shadow: 0 2px 10px rgba(255, 215, 0, 0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex; /* Используем flexbox для выравнивания */
            justify-content: space-between; /* Разделяем пространство между элементами */
            align-items: center; /* Центрируем по вертикали */
            flex-wrap: wrap; /* Позволяет элементам переноситься на новую строку */
        }
        nav {
            margin: 0; /* Убираем отступы */
        }
        nav a {
            margin: 0 15px;
            color: #FFD700; /* Желтый текст для ссылок */
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease; /* Плавный переход цвета */
            cursor: pointer; /* Указатель при наведении */
        }
        nav a:hover {
            color: #ffcc00; /* Более светлый желтый при наведении */
        }
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
            background: #1e1e1e; /* Темно-серый фон для контента */
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5); /* Легкая тень */
        }
        .content {
            padding: 20px;
            margin-bottom: 20px;
            display: none; /* Скрываем раздел по умолчанию */
            border-radius: 8px;
            background: #2a2a2a; /* Фон для контента */
        }
        .logo {
            width: 100px; /* Установлена ширина для логотипа */
            height: auto; /* Сохраняет пропорции изображения */
        }
        h1 {
            font-size: 2.5em; /* Размер шрифта для заголовка */
            margin: 0; /* Убираем отступы */
        }
        h2 {
            color: #FFD700; /* Желтый цвет для заголовков */
            border-bottom: 2px solid #FFD700; /* Подчеркивание заголовка */
            padding-bottom: 10px;
        }
        h3 {
            color: #FFD700; /* Желтый цвет для подзаголовка "Наши продукты" */
            margin: 20px 0 10px; /* Отступы сверху и снизу */
        }
        .yellow-line {
            height: 2px; /* Высота желтой полоски */
            background-color: #FFD700; /* Цвет полоски */
            margin-bottom: 10px; /* Отступ снизу */
        }
        ul {
            list-style-type: none; /* Убираем маркеры списка */
            padding: 0;
        }
        li {
            padding: 5px 0; /* Отступы для элементов списка */
            position: relative;
        }
        li::before {
            content: '✅'; /* Знак перед элементами списка (желтая галочка) */
            color: #FFD700; /* Цвет знака */
            position: absolute;
            left: -20px; /* Отступ от текста */
        }
        .about-bank {
            text-align: center; /* Центрируем текст */
            margin: 40px 0; /* Отступы сверху и снизу */
            padding: 20px; /* Внутренние отступы */
            background: #2a2a2a; /* Фон для раздела о банке */
            border-radius: 8px; /* Закругленные углы */
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5); /* Тень для раздела */
        }
        .contact-info {
            display: none; /* Скрываем информацию по умолчанию */
            padding: 20px;
            background: #2a2a2a; /* Фон для контактной информации */
            border-radius: 8px; /* Закругленные углы */
            margin-top: 20px; /* Отступ сверху */
        }
        .contact-info a {
            color: #FFD700; /* Желтый цвет для ссылки электронной почты */
            text-decoration: none; /* Убираем подчеркивание */
        }
        .contact-info a:hover {
            color: #ffcc00; /* Более светлый желтый при наведении */
        }
        .services {
            display: none; /* Скрываем раздел по умолчанию */
            padding: 20px;
            background: #2a2a2a; /* Фон для услуг */
            border-radius: 8px; /* Закругленные углы */
            margin-top: 20px; /* Отступ сверху */
        }
        .cards {
            display: none; /* Скрываем раздел по умолчанию */
            padding: 20px;
            background: #2a2a2a; /* Фон для карт */
            border-radius: 8px; /* Закругленные углы */
            margin-top: 20px; /* Отступ сверху */
        }
        .bank-image {
            margin-top: 20px; /* Отступ сверху для изображения */
            width: 100%; /* Ширина изображения */
            max-width: 600px; /* Максимальная ширина изображения */
            height: auto; /* Сохраняет пропорции изображения */
            display: block; /* Убедимся, что изображение блочное */
            margin-left: auto; /* Центрируем изображение */
            margin-right: auto; /* Центрируем изображение */
        }
        /* Стили для приветственного сообщения */
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
            transition: opacity 1s ease-out; /* Плавное исчезновение */
            z-index: 2000; /* Убедитесь, что сообщение поверх других элементов */
        }
        .fade-out {
            opacity: 0; /* Прозрачность для исчезновения */
        }
        /* Стили для формы регистрации */
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
            z-index: 3000; /* Поверх других элементов */
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
            background: #ffcc00; /* Более светлый желтый при наведении */
        }
        .hidden {
            display: none; /* Класс для скрытия элементов */
        }
        /* Стили для профиля пользователя */
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
            width: 40px; /* Ширина иконки пользователя */
            height: 40px; /* Высота иконки пользователя */
            border-radius: 50%; /* Круглая иконка */
            margin-right: 10px; /* Отступ справа от иконки */
        }
        .logout-button {
            margin-left: 10px; /* Отступ слева от кнопки "Выйти" */
            padding: 5px 10px; /* Отступы для кнопки */
            background: #FFD700; /* Цвет фона кнопки */
            color: #000; /* Цвет текста кнопки */
            border: none; /* Убираем рамку */
            border-radius: 4px; /* Закругленные углы */
            cursor: pointer; /* Указатель при наведении */
            font-weight: bold; /* Жирный шрифт */
        }
        .logout-button:hover {
            background: #ffcc00; /* Более светлый желтый при наведении */
        }
        .additional-info {
            text-align: center; /* Центрируем текст */
            margin: 20px 0; /* Отступы сверху и снизу */
            font-size: 1.5em; /* Размер шрифта для текста */
            color: #FFD700; /* Желтый цвет для текста */
        }
        .additional-text {
            text-align: center; /* Центрируем текст */
            margin: 20px 0; /* Отступы сверху и снизу */
            font-size: 1em; /* Размер шрифта для текста */
            color: #ffffff; /* Белый цвет для текста */
            padding: 0 20px; /* Отступы по бокам */
        }
        .profile-section {
            display: none; /* Скрываем раздел по умолчанию */
            padding: 20px;
            background: #2a2a2a; /* Фон для профиля */
            border-radius: 8px; /* Закругленные углы */
            margin-top: 20px; /* Отступ сверху */
        }
        .balance-form {
            display: flex;
            flex-direction: column;
            margin-top: 20px;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
        }
        .balance-form input {
            margin-bottom: 10px;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
        }
        .balance-form button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
            font-weight: bold;
        }
        .balance-form button:hover {
            background: #ffcc00; /* Более светлый желтый при наведении */
        }

        /* Адаптивные стили */
        @media (max-width: 768px) {
            header {
                flex-direction: column; /* Вертикальное расположение элементов в заголовке */
                align-items: flex-start; /* Выравнивание по левому краю */
            }
            nav {
                margin-top: 10px; /* Отступ сверху для навигации */
            }
            h1 {
                font-size: 2em; /* Уменьшаем размер заголовка на мобильных устройствах */
            }
            .container {
                padding: 10px; /* Уменьшаем отступы в контейнере */
            }
            .about-bank, .services, .cards, .contact-info, .profile-section {
                padding: 15px; /* Уменьшаем отступы в разделах */
            }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 1.5em; /* Еще больше уменьшаем размер заголовка на маленьких экранах */
            }
            nav a {
                margin: 0 10px; /* Уменьшаем отступы между ссылками */
            }
            .registration-form {
                width: 90%; /* Увеличиваем ширину формы регистрации */
            }
        }
    </style>
    <script>
        window.onload = function() {
            // Проверка, есть ли сохраненные данные в localStorage
            const savedUser               = localStorage.getItem('user');
            if (savedUser              ) {
                const user = JSON.parse(savedUser              );
                showProfile(user.name, user.email, user.balance);
            } else {
                // Скрываем все содержимое, кроме формы регистрации
                document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden'));

                // Показ формы регистрации
                showRegistrationForm();
            }

            // Скрываем раздел "Ваш кабинет" при загрузке страницы
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
            const name = document.getElementById('name').value.trim(); // Убираем пробелы
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Проверка на наличие хотя бы одной буквы в никнейме
            const nameRegex = /[a-zA-Zа-яА-ЯЁё]/; // Регулярное выражение для проверки наличия хотя бы одной буквы

            if (!nameRegex.test(name)) {
                alert("Никнейм должен содержать хотя бы одну букву.");
                return;
            }

            // Проверка электронной почты
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

            if (!emailRegex.test(email)) {
                alert("Пожалуйста, введите корректный адрес электронной почты.");
                return;
            }

            // Проверка пароля
            if (password.length < 6) {
                alert("Пароль должен содержать минимум 6 символов.");
                return;
            }

            // Сохранение данных в localStorage
            const user = {
                name: name,
                email: email,
                balance: 0 // Инициализируем баланс
            };
            localStorage.setItem('user', JSON.stringify(user));

            const welcomeMessage = document.createElement('div');
            welcomeMessage.className = 'welcome-message';
            welcomeMessage.innerText = `Добро пожаловать, ${name}! Мы рады видеть вас на нашем сайте.`;
            document.body.appendChild(welcomeMessage);

            // Удаляем форму регистрации
            document.querySelector('.registration-form').remove();

            // Показываем содержимое страницы
            document.querySelectorAll('.hidden').forEach(el => el.classList.remove('hidden'));

            // Удаляем сообщение через 1 секунду
            setTimeout(() => {
                welcomeMessage.classList.add('fade-out');
                // Удаляем элемент из DOM после завершения анимации
                setTimeout(() => {
                    welcomeMessage.remove();
                }, 1000); // Время, соответствующее времени анимации
            }, 2000); // Показать сообщение на 2 секунды
        }

        function showProfile(name, email, balance) {
            const profileSection = document.querySelector('.profile-section');
            profileSection.innerHTML = `
                <h2>Ваш Кабинет</h2>
                <div class="user-profile">
                    <img src="https://github.com/lybat25/BC-Bank/blob/main/png/2025-01-30_17-50-13-Photoroom.png?raw=true" alt="Иконка пользователя" style="width: 40px; height: 40px; border-radius: 50%; margin-right: 10px;">
                    <span>${name}</span>
                    <button class="logout-button" onclick="logout()">Выйти</button> <!-- Кнопка "Выйти" рядом с именем -->
                </div>
                <p>Email: ${email}</p> <!-- Изменено на "Email" -->
                <p>Ваш текущий баланс: <span id="currentBalance">${balance}</span> рублей.</p> <!-- Отображаем текущий баланс -->
                
                <!-- Форма для пополнения баланса -->
                <div class="balance-form">
                    <h3>Пополнить баланс</h3>
                    <input type="text" id="cardNumber" placeholder="Номер карты" required>
                    <input type="text" id="cardHolder" placeholder="Имя владельца" required>
                    <input type="text" id="expiryDate" placeholder="Срок действия (MM/YY)" required>
                    <input type="text" id="cvv" placeholder="CVV" required>
                    <input type="number" id="amount" placeholder="Сумма пополнения" required>
                    <button onclick="addBalance()">Пополнить</button>
                </div>
            `;
            profileSection.style.display = 'block'; // Показываем раздел профиля
        }

        function addBalance() {
            const cardNumber = document.getElementById('cardNumber').value;
            const cardHolder = document.getElementById('cardHolder').value;
            const expiryDate = document.getElementById('expiryDate').value;
            const cvv = document.getElementById('cvv').value;
            const amount = parseFloat(document.getElementById('amount').value);

            // Проверка данных карты
            if (!cardNumber || !cardHolder || !expiryDate || !cvv) {
                alert("Пожалуйста, заполните все поля для карты.");
                return;
            }

            // Простейшая валидация номера карты (должен состоять из 16 цифр)
            const cardNumberRegex = /^\d{16}$/;
            if (!cardNumberRegex.test(cardNumber)) {
                alert("Номер карты должен содержать 16 цифр.");
                return;
            }

            if (isNaN(amount) || amount <= 0) {
                alert("Пожалуйста, введите корректную сумму для пополнения.");
                return;
            }

            const savedUser    = localStorage.getItem('user');
            if (savedUser   ) {
                const user = JSON.parse(savedUser   );
                user.balance += amount; // Увеличиваем баланс
                localStorage.setItem('user', JSON.stringify(user)); // Сохраняем обновленный баланс
                alert(`Баланс успешно пополнен на ${amount} рублей. Ваш новый баланс: ${user.balance} рублей.`);
            }
        }

        function logout() {
            localStorage.removeItem('user'); // Удаляем данные пользователя из localStorage
            document.querySelector('.profile-section').style.display = 'none'; // Скрываем раздел профиля
            document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden')); // Скрываем остальное содержимое
            // Показ формы регистрации снова
            showRegistrationForm();
        }

        function toggleSection(section) {
            const services = document.getElementById('services');
            const cards = document.getElementById('cards'); // Новый раздел для карт
            const contact = document.querySelector('.contact-info');
            const about = document.querySelector('.about-bank');
            const profile = document.querySelector('.profile-section');

            // Скрываем все секции
            services.style.display = 'none';
            cards.style.display = 'none'; // Скрываем раздел карт
            contact.style.display = 'none';
            about.style.display = 'none';
            profile.style.display = 'none';

            // Показываем выбранную секцию
            if (section === 'services') {
                services.style.display = 'block';
            } else if (section === 'cards') { // Показать раздел карт
                cards.style.display = 'block';
            } else if (section === 'contact') {
                contact.style.display = 'block';
            } else if (section === 'about') {
                about.style.display = 'block';
            } else if (section === 'profile') {
                profile.style.display = 'block'; // Показываем раздел "Ваш Кабинет"
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
        
        <h3 style="color: #FFD700;">Наши продукты</h3> <!-- Заголовок "Наши продукты" теперь желтый -->
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <p>Будь на стороне добра! Забудьте про врагов и оформите нашу карту от BK-Bank.</p>
        
        <img src="https://github.com/lybat25/BC-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" alt="Изображение о банке" class="bank-image"> <!-- Изображение о банке -->
        
        <img src="https://github.com/lybat25/BC-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_105015270.png?raw=true" alt="Изображение о банке" class="bank-image"> <!-- Второе изображение -->
        
        <div class="additional-info" style="color: #FFD700;">Наши карты</div> <!-- Заголовок "Наши карты" -->
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <img src="https://github.com/lybat25/BC-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" alt="Наши карты" class="bank-image"> <!-- Изображение карт -->

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
        <p>Email: <a href="mailto:bkbank636@gmail.com">bkbank636@gmail.com</a></p> <!-- Изменена электронная почта -->
        <p>Discord: <a href="https://discord.gg/q8kRuKebKH" target="_blank">BK-Bank server</a></p> <!-- Добавлена ссылка на Discord -->
        <p>Telegram: <a href="https://t.me/+NE8aj5oiHJhjYjgy" target="_blank">BK-Bank channel</a></p> <!-- Добавлена ссылка на Telegram -->
        <p>YouTube: <a href="https://www.youtube.com/channel/UCnFbE5v1nzlonhsk9wX16Yw" target="_blank">BK-Bank YouTube</a></p> <!-- Добавлена ссылка на YouTube -->
         <p>Token: <a href="ЕСЛИ ТЫ ЭТО ВИДИШЬ ЗНАЧИТ ТЫ ОТКРЫЛ ПАСХАЛКУ НАПИШИ МНЕ В ДИСКОРД fa5" target="_blank">BK-Bank Token (ещё не вышел)</a></p> <!-- Добавлена ссылка на Token -->
    </div>

    <div class="profile-section" style="display: none;"> <!-- Скрываем раздел "Ваш Кабинет" по умолчанию -->
        <h2>Ваш Кабинет</h2>
        <div class="user-profile">
            <img src="https://github.com/lybat25/BC-Bank/blob/main/png/2025-01-30_17-50-13-Photoroom.png?raw=true" alt="Иконка пользователя" style="width: 40px; height: 40px; border-radius: 50%; margin-right: 10px;">
            <span>${name}</span>
            <button class="logout-button" onclick="logout()">Выйти</button> <!-- Кнопка "Выйти" рядом с именем -->
        </div>
        <p>Email: <span id="userEmail"></span></p>
        <p>Ваш текущий баланс: <span id="currentBalance">0</span> рублей.</p>
        
        <!-- Форма для пополнения баланса -->
        <div class="balance-form">
            <h3>Пополнить баланс</h3>
            <input type="text" id="cardNumber" placeholder="Номер карты" required>
            <input type="text" id="cardHolder" placeholder="Имя владельца" required>
            <input type="text" id="expiryDate" placeholder="Срок действия (MM/YY)" required>
            <input type="text" id="cvv" placeholder="CVV" required>
            <input type="number" id="amount" placeholder="Сумма пополнения" required>
            <button onclick="addBalance()">Пополнить</button>
        </div>
    </div>
</div>

</body>
</html>
