<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БК-Банк - Ваш надежный банк</title>
    <link rel="stylesheet" href="styles.css"> <!-- Подключите свой CSS файл -->
    <style>
        /* Стили из первого скрипта */
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
        .additional-info {
            text-align: center; /* Центрируем текст */
            margin: 20px 0; /* Отступы сверху и снизу */
            font-size: 1.5em; /* Размер шрифта для текста */
            color: #FFD700; /* Желтый цвет для текста */
            font-weight: bold; /* Жирный шрифт для дополнительной информации */
        }
        .additional-text {
            text-align: center; /* Центрируем текст */
            margin: 20px 0; /* Отступы сверху и снизу */
            font-size: 1em; /* Размер шрифта для текста */
            color: #ffffff; /* Белый цвет для текста */
            padding: 0 20px; /* Отступы по бокам */
            font-weight: bold; /* Жирный шрифт для дополнительного текста */
        }
        .profile-section {
            display: none; /* Скрываем раздел по умолчанию */
            padding: 20px;
            background: #2a2a2a; /* Фон для профиля */
            border-radius: 8px; /* Закругленные углы */
            margin-top: 20px; /* Отступ сверху */
        }
    </style>
    <script>
        window.onload = function() {
            // Проверка, есть ли сохраненные данные в localStorage
            const savedUser = localStorage.getItem('user');
            if (savedUser) {
                const user = JSON.parse(savedUser);
                showProfile(user.name, user.email);
            } else {
                // Скрываем все содержимое, кроме формы регистрации
                document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden'));

                // Показ формы регистрации
                showRegistrationForm();
            }

            // Скрываем раздел "Ваш кабинет" при загрузке страницы
            document.querySelector('.profile-section').style.display = 'none';

            // Подключение к WebSocket для считывания количества пользователей
            const userCountElement = document.getElementById('currentUserCount');
            const socket = new WebSocket('ws://localhost:8080');

            socket.onmessage = function(event) {
                const data = JSON.parse(event.data);
                userCountElement.innerText = data.users; // Обновляем количество пользователей
            };

            socket.onopen = function() {
                console.log('Connected to WebSocket server');
            };

            socket.onclose = function() {
                console.log('Disconnected from WebSocket server');
            };
        };

        function showRegistrationForm() {
            const registrationForm = document.createElement('div');
            registrationForm.className = 'registration-form';
            registrationForm.innerHTML = `
                <h2><strong>Регистрация</strong></h2>
                <input type="text" id="name" placeholder="Ваш никнейм" required>
                <input type="email" id="email" placeholder="Ваша электронная почта" required>
                <input type="password" id="password" placeholder="Пароль" required>
                <button onclick="register()"><strong>Зарегистрироваться</strong></button>
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
                alert("<strong>Никнейм должен содержать хотя бы одну букву.</strong>");
                return;
            }

            // Проверка электронной почты
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

            if (!emailRegex.test(email)) {
                alert("<strong>Пожалуйста, введите корректный адрес электронной почты.</strong>");
                return;
            }

            // Проверка пароля
            if (password.length < 6 || !/^[a-zA-Z]+$/.test(password)) {
                alert("<strong>Пароль должен содержать минимум 6 символов и состоять только из английских букв.</strong>");
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
            const user = JSON.parse(localStorage.getItem('user')); // Получаем данные пользователя из localStorage
            profileSection.innerHTML = `
                <h2><strong>Ваш Кабинет</strong></h2>
                <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
                <div class="user-profile">
                    <img src="https://github.com/lybat25/BK-Bank/blob/main/png/2025-01-30_17-50-13-Photoroom.png?raw=true" alt="Иконка пользователя" style="width: 40px; height: 40px; border-radius: 50%; margin-right: 10px;">
                    <span><strong>${name}</strong></span>
                    <button class="logout-button" onclick="logout()"><strong>Выйти</strong></button> <!-- Кнопка "Выйти" рядом с именем -->
                </div>
                <p><strong>Email: ${email}</strong></p> <!-- Изменено на "Email" -->
                <p><strong>Наш банк ещё не готов полностью, пока что у нас есть только это насчёт вашего кабин
                
