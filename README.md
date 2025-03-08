<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БК-Банк - Ваш надежный банк</title>
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
        }
        nav {
            margin: 0; /* Убираем отступы */
        }
        nav a {
            margin: 0 15px;
            color: #FFD700; /* Желтый текст для ссылок */
            text-decoration: none;
            font-weight: bold; /* Жирный шрифт для ссылок */
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
            font-weight: bold; /* Жирный шрифт для заголовка */
        }
        h2 {
            color: #FFD700; /* Желтый цвет для заголовков */
            padding-bottom: 10px;
            border-bottom: 2px solid #FFD700; /* Подчеркивание заголовка */
            font-weight: bold; /* Жирный шрифт для заголовка */
        }
        h3 {
            color: #FFD700; /* Желтый цвет для подзаголовка "Наши продукты" */
            margin: 20px 0 10px; /* Отступы сверху и снизу */
            font-weight: bold; /* Жирный шрифт для подзаголовка */
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
            font-weight: bold; /* Жирный шрифт для элементов списка */
        }
        li::before {
            content: '✓'; /* Знак перед элементами списка изменен на "✓" */
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
            font-weight: bold; /* Жирный шрифт для ссылки */
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
            font-weight: bold; /* Жирный шрифт для приветственного сообщения */
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
            font-weight: bold; /* Жирный шрифт для полей ввода */
        }
        .registration-form button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
            font-weight: bold; /* Жирный шрифт для кнопки */
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
            font-weight: bold; /* Жирный шрифт для кнопки "Выйти" */
        }
        .logout-button:hover {
            background: #ffcc00; /* Более светлый желтый при наведении */
        }
    </style>
    <script>
        window.onload = function() {
            // Проверка, есть ли сохраненные данные в localStorage
            const savedUser   = localStorage.getItem('user');
            if (savedUser  ) {
                const user = JSON.parse(savedUser  );
                showProfile(user.name, user.email);
            } else {
                // Скрываем все содержимое, кроме формы регистрации
                document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden'));
                // Показ формы регистрации
                showRegistrationForm();
            }

            // Всегда показываем главную страницу
            toggleSection('about');
        };

        function showRegistrationForm() {
            const registrationForm = document.createElement('div');
            registrationForm.className = 'registration-form';
            registrationForm.innerHTML = 
                `<h2><strong>Регистрация</strong></h2>
                <input type="text" id="name" placeholder="Ваш никнейм" required>
                <input type="email" id="email" placeholder="Ваша электронная почта" required>
                <input type="password" id="password" placeholder="Пароль" required>
                <button onclick="register()"><strong>Зарегистрироваться</strong></button>`;
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
            if (password.length < 6 || !/^[a-zA-Z]+$/.test(password)) {
                alert("Пароль должен содержать минимум 6 символов и состоять только из английских букв.");
                return;
            }

            // Сохранение данных в localStorage
            const user = {
                name: name,
                email: email,
                balance: 0, // Инициализируем баланс
                friends: [], // Инициализируем список друзей
                friendRequests: [] // Инициализируем список запросов в друзья
            };
            localStorage.setItem('user', JSON.stringify(user));

            const welcomeMessage = document.createElement('div');
            welcomeMessage.className = 'welcome-message';
            welcomeMessage.innerHTML = `<strong>Добро пожаловать, ${name}! Мы рады видеть вас на нашем сайте.</strong>`;
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

        function showProfile(name, email) {
            const profileSection = document.querySelector('.profile-section');
            profileSection.innerHTML = 
                `<h2><strong>Ваш Кабинет</strong></h2>
                <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
                <div class="user-profile">
                    <img src="https://github.com/lybat25/BK-Bank/blob/main/png/2025-01-30_17-50-13-Photoroom.png?raw=true" alt="Иконка пользователя" style="width: 40px; height: 40px; border-radius: 50%; margin-right: 10px;">
                    <span><strong>${name}</strong></span>
                    <button class="logout-button" onclick="logout()"><strong>Выйти</strong></button> <!-- Кнопка "Выйти" рядом с именем -->
                </div>
                <p><strong>Email: <a href="mailto:${email}" style="color: #FFD700;">${email}</a></strong></p> <!-- Отображение электронной почты -->
                <p><strong>Наш банк ещё не готов полностью, пока что у нас есть только это насчёт вашего кабинета.</strong></p> <!-- Обновленный текст -->
                
                <div class="add-friend">
                    <h3><strong>Добавить в друзья</strong></h3>
                    <input type="text" id="friendName" placeholder="Имя или Email друга" required>
                    <button onclick="sendFriendRequest()"><strong>Отправить запрос</strong></button>
                </div>
                <div class="friend-list">
                    <h3><strong>Список друзей</strong></h3>
                    <ul id="friends"></ul>
                </div>
                <div class="friend-requests">
                    <h3><strong>Запросы в друзья</strong></h3>
                    <ul id="friendRequests"></ul>
                </div>`;
            profileSection.style.display = 'block'; // Показываем раздел профиля

            // Отображаем список друзей
            const friendsList = document.getElementById('friends');
            const user = JSON.parse(localStorage.getItem('user')); // Получаем данные пользователя из localStorage
            user.friends.forEach(friend => {
                const friendItem = document.createElement('li');
                friendItem.textContent = friend;
                friendsList.appendChild(friendItem);
            });

            // Отображаем запросы в друзья
            const requestsList = document.getElementById('friendRequests');
            user.friendRequests.forEach(request => {
                const requestItem = document.createElement('li');
                requestItem.textContent = request;
                const acceptButton = document.createElement('button');
                acceptButton.textContent = "Принять";
                acceptButton.onclick = () => acceptFriendRequest(request);
                requestItem.appendChild(acceptButton);
                requestsList.appendChild(requestItem);
            });
        }

        function sendFriendRequest() {
            const friendName = document.getElementById('friendName').value.trim();
            const user = JSON.parse(localStorage.getItem('user')); // Получаем данные пользователя из localStorage

            if (friendName) {
                // Добавляем запрос в друзья текущего пользователя
                user.friendRequests.push(friendName);
                localStorage.setItem('user', JSON.stringify(user)); // Сохраняем обновленные данные

                alert(`Запрос в друзья отправлен пользователю ${friendName}`);
                document.getElementById('friendName').value = ''; // Очищаем поле ввода
            } else {
                alert("Пожалуйста, введите имя или email друга.");
            }
        }

        function acceptFriendRequest(friendName) {
            const user = JSON.parse(localStorage.getItem('user')); // Получаем данные пользователя из localStorage

            // Удаляем запрос из списка запросов
            user.friendRequests = user.friendRequests.filter(request => request !== friendName);
            // Добавляем друга в список друзей
            user.friends.push(friendName);
            localStorage.setItem('user', JSON.stringify(user)); // Сохраняем обновленные данные

            showProfile(user.name, user.email); // Обновляем профиль
            alert(`Вы добавили ${friendName} в друзья!`);
        }

        function logout() {
            localStorage.removeItem('user'); // Удаляем данные пользователя из localStorage
            document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden')); // Скрываем остальное содержимое
            // Показ формы регистрации снова
            showRegistrationForm();
        }

        function toggleSection(section) {
            const services = document.getElementById('services');
            const cards = document.getElementById('cards');
            const contact = document.querySelector('.contact-info');
            const about = document.querySelector('.about-bank');
            const profile = document.querySelector('.profile-section');

            // Скрываем все секции
            services.style.display = 'none';
            cards.style.display = 'none';
            contact.style.display = 'none';
            about.style.display = 'none';
            profile.style.display = 'none';

            // Показываем выбранную секцию
            if (section === 'services') {
                services.style.display = 'block';
            } else if (section === 'cards') {
                cards.style.display = 'block';
            } else if (section === 'contact') {
                contact.style.display = 'block';
            } else if (section === 'about') {
                about.style.display = 'block';
            } else if (section === 'profile') {
                profile.style.display = 'block'; // Показываем раздел "Ваш Кабинет"
                showProfile(JSON.parse(localStorage.getItem('user')).name, JSON.parse(localStorage.getItem('user')).email); // Обновляем профиль
            }
        }
    </script>
</head>
<body>

<header>
    <h1>
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-11_142359079.png?raw=true" class="logo" alt="Логотип БК-Банк">
        <strong>БК-Банк</strong>
    </h1>
    <nav>
        <a onclick="toggleSection('about')"><strong>Главная</strong></a>
        <a onclick="toggleSection('services')"><strong>Услуги</strong></a>
        <a onclick="toggleSection('cards')"><strong>Карты</strong></a> 
        <a onclick="toggleSection('contact')"><strong>Контакты</strong></a>
        <a onclick="toggleSection('profile')"><strong>Кабинет</strong></a> <!-- Вкладка "Ваш Кабинет" -->
    </nav>
</header>

<div class="container">
    <div class="about-bank">
        <h2><strong>БК-Банк: Ваш надежный финансовый партнер</strong></h2>
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <p><strong>В БК-Банке мы понимаем, что каждая покупка — это не просто транзакция, а часть Вашей жизни. Как говорит наш клиент: "Я ношу карту. И эта карта не прячет мои покупки, но создаёт их оформление." Мы стремимся сделать каждую Вашу финансовую операцию прозрачной и удобной.</strong></p>
        <p><strong>Мы гордимся тем, что предоставляем нашим клиентам не только услуги, но и возможность управлять своими финансами с уверенностью. Один из наших пользователей отметил: "Я всегда утверждал, что стал пользователем БК-Банка, чтобы сражаться с деньгами. Это была ложь."</strong></p>
        
        <h3 style="color: #FFD700;"><strong>Наши продукты</strong></h3> <!-- Заголовок "Наши продукты" теперь желтый -->
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <p><strong>Будь на стороне добра! Забудьте про врагов и оформите нашу карту от БК-Банк.</strong></p>
        
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" alt="Изображение о банке" class="bank-image"> <!-- Первое изображение -->
        
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_105015270.png?raw=true" alt="Изображение о банке" class="bank-image"> <!-- Второе изображение -->
        
        <div class="additional-info" style="color: #FFD700;"><strong>Наши карты</strong></div> <!-- Заголовок "Наши карты" -->
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" alt="Наши карты" class="bank-image"> <!-- Изображение карт -->

        <div class="additional-text">
            <strong>Мы верим, что финансовая грамотность — это ключ к свободе. Каждый день мы работаем над тем, чтобы наши клиенты могли принимать обоснованные решения, основанные на чёткой информации. Мы предлагаем инструменты и ресурсы, которые помогут Вам лучше понять свои расходы и сбережения.</strong>
            <br><br>
            <img src="" style="margin-top: 20px; max-width: 50%; height: auto;">
        </div>
    </div>

    <div id="services" class="services">
        <h2><strong>Наши услуги</strong></h2>
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
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
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <ul>
            <li><strong>Карта "тень и свет"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_092441724.png?raw=true" alt="Карта тень и свет" class="bank-image"> <!-- Добавлено изображение -->
            <li><strong>Карта "чёрно-жёлтая энергия"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_093348500.png?raw=true" alt="Карта чёрно-жёлтая энергия" class="bank-image"> <!-- Добавлено изображение -->
            <li><strong>Карта "жёлтая стрела"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_094122593.png?raw=true" alt="Карта жёлтая стрела" class="bank-image"> <!-- Добавлено изображение -->
            <li><strong>Карта "золотая волна"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_095046740.png?raw=true" alt="Карта золотая волна" class="bank-image"> <!-- Новое изображение -->
            <li><strong>Карта "солнечный ночной ветер"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_100946793.png?raw=true" alt="Карта солнечный ночной ветер" class="bank-image"> <!-- Новое изображение -->
            <li><strong>Карта "БКашная тёмный"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_101740633.png?raw=true" alt="Карта БКашная тёмный" class="bank-image"> <!-- Новое изображение -->
            <li><strong>Карта "БКашная светлый"</strong></li>
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_102653372.png?raw=true" alt="Карта БКашная светлый" class="bank-image"> <!-- Новое изображение -->
        </ul>
        <p><strong>Наши карты всё ещё не будут доступны больше пару месяцев, советуем вам использовать нашу Биржу.</strong></p>
    </div>

    <div class="contact-info">
        <h2><strong>Контактная информация</strong></h2>
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <p><strong>Email: <a href="mailto:hgaraew@mail.ru" style="color: #FFD700;">БК-Банк email</a></strong></p> <!-- Изменено на "БК-Банк email" с ссылкой -->
        <p><strong>Discord:</strong> <a href="https://discord.gg/q8kRuKebKH" target="_blank">БК-Банк server</a></p> <!-- Добавлена ссылка на Discord -->
        <p><strong>Telegram:</strong> <a href="https://t.me/+NE8aj5oiHJhjYjgy" target="_blank">БК-Банк channel</a></p> <!-- Добавлена ссылка на Telegram -->
        <p><strong>YouTube:</strong> <a href="https://www.youtube.com/channel/UCnFbE5v1nzlonhsk9wX16Yw" target="_blank">БК-Банк YouTube</a></p> <!-- Добавлена ссылка на YouTube -->
        <p><strong>Token:</strong> <a href="ЕСЛИ ТЫ ЭТО ВИДИШЬ ЗНАЧИT ТЫ ОТКРЫЛ ПАСХАЛКУ НАПИШИ МНЕ В ДИСКОРД fa5" target="_blank">БК-Банк Token (ещё не вышел)</a></p>
    </div>

    <div class="profile-section" style="display: none;"></div> <!-- Секция профиля, скрыта по умолчанию -->
</div>

</body>
</html>
