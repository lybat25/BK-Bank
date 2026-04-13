<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БК-Банк — Финансы нового поколения</title>
    <!-- Современный плавный скролл -->
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            color: #ffffff;
            overflow-x: hidden;
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
        }

        /* Стильный скроллбар */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #1a1a1a;
        }
        ::-webkit-scrollbar-thumb {
            background: #FFD700;
            border-radius: 10px;
        }

        /* Анимированный градиентный фон */
        .bg-glow {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 20% 30%, rgba(255, 215, 0, 0.03) 0%, transparent 50%),
                        radial-gradient(circle at 80% 70%, rgba(255, 215, 0, 0.02) 0%, transparent 50%);
            pointer-events: none;
            z-index: -1;
        }

        /* Хедер с эффектом размытия (Glassmorphism) */
        .glass-header {
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            background-color: rgba(18, 18, 18, 0.85);
            border-bottom: 1px solid rgba(255, 215, 0, 0.15);
            padding: 16px 32px;
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }

        .logo-wrapper {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .logo-img {
            width: 48px;
            height: 48px;
            object-fit: contain;
            filter: drop-shadow(0 0 12px rgba(255, 215, 0, 0.4));
            transition: transform 0.3s ease;
        }

        .logo-img:hover {
            transform: scale(1.05);
        }

        .bank-name {
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #FFD700 0%, #FFC200 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            letter-spacing: -0.5px;
        }

        .nav-links {
            display: flex;
            gap: 8px;
        }

        .nav-link {
            background: transparent;
            border: none;
            color: #e0e0e0;
            padding: 12px 24px;
            margin: 0 4px;
            border-radius: 40px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.25s ease;
            backdrop-filter: blur(5px);
            position: relative;
            overflow: hidden;
        }

        .nav-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.15) 0%, transparent 80%);
            opacity: 0;
            transition: opacity 0.25s ease;
            z-index: -1;
        }

        .nav-link:hover {
            color: #FFD700;
            transform: translateY(-2px);
            box-shadow: 0 10px 20px -10px rgba(255, 215, 0, 0.2);
        }

        .nav-link:hover::before {
            opacity: 1;
        }

        /* Основной контейнер */
        .main-container {
            max-width: 1300px;
            margin: 30px auto;
            padding: 0 24px;
        }

        /* Карточки с контентом */
        .content-card {
            background: rgba(25, 25, 25, 0.7);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 215, 0, 0.1);
            border-radius: 32px;
            padding: 36px;
            margin-bottom: 30px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease, border-color 0.3s ease;
            animation: fadeInUp 0.6s ease-out;
        }

        .content-card:hover {
            border-color: rgba(255, 215, 0, 0.3);
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h2 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 24px;
            background: linear-gradient(135deg, #FFD700, #FFA500);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            letter-spacing: -0.5px;
        }

        .divider {
            height: 4px;
            width: 80px;
            background: linear-gradient(90deg, #FFD700, transparent);
            border-radius: 4px;
            margin-bottom: 32px;
        }

        /* Карточки карт в сетке */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 24px;
            margin-top: 30px;
        }

        .card-item {
            background: rgba(40, 40, 40, 0.6);
            backdrop-filter: blur(8px);
            border-radius: 24px;
            padding: 20px;
            border: 1px solid rgba(255, 215, 0, 0.08);
            transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
        }

        .card-item:hover {
            transform: translateY(-8px) scale(1.02);
            border-color: #FFD700;
            box-shadow: 0 30px 40px -20px rgba(255, 215, 0, 0.2);
        }

        .card-image {
            width: 100%;
            border-radius: 16px;
            margin-bottom: 16px;
            transition: transform 0.5s ease;
        }

        .card-item:hover .card-image {
            transform: perspective(1000px) rotateY(2deg);
        }

        .card-name {
            font-weight: 700;
            font-size: 1.2rem;
            color: #FFD700;
            text-align: center;
        }

        /* Формы (логин, регистрация, сброс) — современный стиль */
        .modal-form {
            background: rgba(20, 20, 20, 0.9);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 215, 0, 0.2);
            border-radius: 40px;
            padding: 40px 32px;
            width: 420px;
            max-width: 90%;
            box-shadow: 0 40px 80px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 215, 0, 0.1) inset;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 3000;
            animation: modalPop 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes modalPop {
            from { opacity: 0; transform: translate(-50%, -48%); }
            to { opacity: 1; transform: translate(-50%, -50%); }
        }

        .form-title {
            font-size: 2rem;
            font-weight: 700;
            color: #FFD700;
            text-align: center;
            margin-bottom: 30px;
        }

        .form-input {
            width: 100%;
            padding: 16px 20px;
            margin-bottom: 16px;
            background: rgba(255, 255, 255, 0.05);
            border: 1.5px solid rgba(255, 215, 0, 0.2);
            border-radius: 60px;
            color: white;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.2s ease;
            outline: none;
        }

        .form-input:focus {
            border-color: #FFD700;
            background: rgba(255, 255, 255, 0.08);
            box-shadow: 0 0 0 4px rgba(255, 215, 0, 0.1);
        }

        .form-input::placeholder {
            color: #999;
            font-weight: 400;
        }

        .gold-button {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #FFD700 0%, #FFB300 100%);
            border: none;
            border-radius: 60px;
            color: #0a0a0a;
            font-weight: 700;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(255, 215, 0, 0.2);
            margin-bottom: 16px;
        }

        .gold-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 30px rgba(255, 215, 0, 0.3);
            background: linear-gradient(135deg, #FFE44D 0%, #FFC200 100%);
        }

        .text-link {
            color: #FFD700;
            text-align: center;
            display: block;
            margin: 12px 0;
            cursor: pointer;
            font-weight: 600;
            text-decoration: underline;
            text-underline-offset: 4px;
            text-decoration-color: transparent;
            transition: text-decoration-color 0.2s;
        }

        .text-link:hover {
            text-decoration-color: #FFD700;
        }

        /* Приветственное сообщение */
        .toast-message {
            position: fixed;
            top: 100px;
            right: 30px;
            background: rgba(20, 20, 20, 0.9);
            backdrop-filter: blur(20px);
            border-left: 6px solid #FFD700;
            padding: 20px 30px;
            border-radius: 60px 16px 16px 60px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
            z-index: 2500;
            font-weight: 600;
            color: #FFD700;
            animation: slideIn 0.4s ease;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateX(50px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .fade-out {
            opacity: 0;
            transition: opacity 0.8s ease;
        }

        /* Профиль */
        .profile-header {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 30px;
            padding: 20px;
            background: rgba(255, 215, 0, 0.03);
            border-radius: 40px;
        }

        .profile-avatar {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            border: 3px solid #FFD700;
            padding: 3px;
            background: #1a1a1a;
        }

        .logout-btn {
            background: transparent;
            border: 1.5px solid #FFD700;
            color: #FFD700;
            padding: 10px 24px;
            border-radius: 40px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            margin-left: auto;
        }

        .logout-btn:hover {
            background: #FFD700;
            color: #0a0a0a;
        }

        /* Друзья и запросы */
        .friend-actions {
            display: flex;
            gap: 12px;
            margin: 20px 0;
        }

        .friend-input {
            flex: 1;
            padding: 14px 20px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 215, 0, 0.2);
            border-radius: 60px;
            color: white;
        }

        .small-gold-btn {
            background: #FFD700;
            border: none;
            padding: 14px 24px;
            border-radius: 60px;
            font-weight: 700;
            color: #0a0a0a;
            cursor: pointer;
            transition: 0.2s;
        }

        .small-gold-btn:hover {
            background: #FFE44D;
        }

        .friend-list {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin: 20px 0;
        }

        .friend-tag {
            background: rgba(255, 215, 0, 0.1);
            padding: 8px 18px;
            border-radius: 40px;
            border: 1px solid rgba(255, 215, 0, 0.2);
            font-weight: 500;
        }

        /* Утилиты */
        .hidden {
            display: none !important;
        }

        .error-text {
            color: #ff5e5e;
            text-align: center;
            margin-bottom: 12px;
            font-weight: 500;
        }

        .success-text {
            color: #4ade80;
            text-align: center;
            margin-bottom: 12px;
            font-weight: 500;
        }
    </style>
</head>
<body>

<div class="bg-glow"></div>

<!-- Хедер с эффектом стекла -->
<header class="glass-header hidden">
    <div class="logo-wrapper">
        <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-11_142359079.png?raw=true" class="logo-img" alt="БК-Банк">
        <span class="bank-name">БК-Банк</span>
    </div>
    <nav class="nav-links">
        <button class="nav-link" onclick="toggleSection('about')">Главная</button>
        <button class="nav-link" onclick="toggleSection('services')">Услуги</button>
        <button class="nav-link" onclick="toggleSection('cards')">Карты</button>
        <button class="nav-link" onclick="toggleSection('contact')">Контакты</button>
        <button class="nav-link" onclick="toggleSection('profile')">Кабинет</button>
    </nav>
</header>

<main class="main-container hidden">
    <!-- Главная -->
    <div id="about-section" class="content-card">
        <h2>Ваш надёжный финансовый партнёр</h2>
        <div class="divider"></div>
        <p style="font-size: 1.2rem; margin-bottom: 30px; color: #ccc;"><strong>В БК-Банке мы понимаем, что каждая покупка — это не просто транзакция, а часть Вашей жизни.</strong></p>
        <p style="margin-bottom: 20px;"><strong>«Я ношу карту. И эта карта не прячет мои покупки, но создаёт их оформление.»</strong></p>
        <p><strong>Мы гордимся тем, что предоставляем нашим клиентам не только услуги, но и возможность управлять своими финансами с уверенностью.</strong></p>
        
        <div style="display: flex; gap: 20px; margin-top: 40px; flex-wrap: wrap;">
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_102355995.png?raw=true" style="max-width: 48%; border-radius: 24px;" alt="О банке">
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-12_105015270.png?raw=true" style="max-width: 48%; border-radius: 24px;" alt="О банке">
        </div>
    </div>

    <!-- Услуги -->
    <div id="services-section" class="content-card hidden">
        <h2>Наши услуги</h2>
        <div class="divider"></div>
        <ul style="list-style: none; font-size: 1.3rem;">
            <li style="padding: 12px 0;">✓ Кредитование</li>
            <li style="padding: 12px 0;">✓ Депозиты</li>
            <li style="padding: 12px 0;">✓ Инвестиционные услуги</li>
            <li style="padding: 12px 0;">✓ Консультации по финансам</li>
            <li style="padding: 12px 0;">✓ Онлайн-банкинг</li>
        </ul>
    </div>

    <!-- Карты -->
    <div id="cards-section" class="content-card hidden">
        <h2>Эксклюзивные карты</h2>
        <div class="divider"></div>
        <div class="cards-grid" id="cards-container"></div>
        <p style="margin-top: 30px; font-style: italic; color: #FFD700;"><strong>Карты появятся в ближайшее время. Рекомендуем воспользоваться Биржей.</strong></p>
    </div>

    <!-- Контакты -->
    <div id="contact-section" class="content-card hidden">
        <h2>Связь с нами</h2>
        <div class="divider"></div>
        <p style="font-size: 1.2rem; margin: 15px 0;"><strong>Email:</strong> <a href="mailto:hgaraew@mail.ru" style="color: #FFD700;">БК-Банк email</a></p>
        <p style="font-size: 1.2rem; margin: 15px 0;"><strong>Discord:</strong> <a href="https://discord.gg/q8kRuKebKH" target="_blank" style="color: #FFD700;">Сервер БК-Банк</a></p>
        <p style="font-size: 1.2rem; margin: 15px 0;"><strong>Telegram:</strong> <a href="https://t.me/+NE8aj5oiHJhjYjgy" target="_blank" style="color: #FFD700;">Канал БК-Банк</a></p>
        <p style="font-size: 1.2rem; margin: 15px 0;"><strong>YouTube:</strong> <a href="https://www.youtube.com/channel/UCnFbE5v1nzlonhsk9wX16Yw" target="_blank" style="color: #FFD700;">БК-Банк YouTube</a></p>
    </div>

    <!-- Профиль -->
    <div id="profile-section" class="content-card hidden"></div>
</main>

<script>
    (function(){
        // --- Данные и состояние (без изменений в логике) ---
        let users = JSON.parse(localStorage.getItem('bankUsers')) || {};
        let currentUser = null;
        let resetTokens = JSON.parse(localStorage.getItem('resetTokens')) || {};

        // Список карт (для отрисовки)
        const cardList = [
            { name: 'Тень и свет', img: 'https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_092441724.png?raw=true' },
            { name: 'Чёрно-жёлтая энергия', img: 'https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_093348500.png?raw=true' },
            { name: 'Жёлтая стрела', img: 'https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_094122593.png?raw=true' },
            { name: 'Золотая волна', img: 'https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_095046740.png?raw=true' },
            { name: 'Солнечный ночной ветер', img: 'https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_100946793.png?raw=true' },
            { name: 'БКашная тёмный', img: 'https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_101740633.png?raw=true' },
            { name: 'БКашная светлый', img: 'https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-14_102653372.png?raw=true' }
        ];

        // Рендер карточек карт
        function renderCards() {
            const container = document.getElementById('cards-container');
            if (!container) return;
            container.innerHTML = cardList.map(card => `
                <div class="card-item">
                    <img src="${card.img}" class="card-image" alt="${card.name}">
                    <div class="card-name">${card.name}</div>
                </div>
            `).join('');
        }

        // Инициализация
        window.onload = function() {
            const session = localStorage.getItem('currentSession');
            if (session) {
                const sessionData = JSON.parse(session);
                if (Date.now() - sessionData.timestamp < 24 * 60 * 60 * 1000) {
                    currentUser = sessionData.username;
                    showMainContent();
                    showWelcomeMessage(users[currentUser].name);
                    renderCards();
                    return;
                } else {
                    localStorage.removeItem('currentSession');
                }
            }
            showLoginForm();
        };

        function showLoginForm() {
            removeExistingModals();
            const modal = document.createElement('div');
            modal.className = 'modal-form';
            modal.innerHTML = `
                <div class="form-title">Вход</div>
                <div id="loginError" class="error-text hidden"></div>
                <input type="text" id="loginUsername" class="form-input" placeholder="Никнейм">
                <input type="password" id="loginPassword" class="form-input" placeholder="Пароль">
                <button class="gold-button" onclick="window.login()">Войти</button>
                <span class="text-link" onclick="window.showForgotPasswordForm()">Забыли пароль?</span>
                <span class="text-link" onclick="window.showRegistrationForm()">Регистрация</span>
            `;
            document.body.appendChild(modal);
        }

        window.showLoginForm = showLoginForm;

        window.showForgotPasswordForm = function() {
            removeExistingModals();
            const modal = document.createElement('div');
            modal.className = 'modal-form';
            modal.innerHTML = `
                <div class="form-title">Восстановление</div>
                <div id="resetError" class="error-text hidden"></div>
                <div id="resetSuccess" class="success-text hidden"></div>
                <input type="email" id="resetEmail" class="form-input" placeholder="Ваш email">
                <button class="gold-button" onclick="window.sendResetEmail()">Отправить</button>
                <span class="text-link" onclick="showLoginForm()">← Назад</span>
            `;
            document.body.appendChild(modal);
        };

        window.sendResetEmail = function() {
            const email = document.getElementById('resetEmail')?.value;
            const errEl = document.getElementById('resetError');
            const sucEl = document.getElementById('resetSuccess');
            if (!email) return showError(errEl, 'Введите email');
            let found = null;
            for (let u in users) if (users[u].email === email) { found = u; break; }
            if (!found) return showError(errEl, 'Email не найден');
            const token = Math.random().toString(36).substring(2) + Date.now().toString(36);
            resetTokens[token] = { username: found, email, expires: Date.now() + 3600000 };
            localStorage.setItem('resetTokens', JSON.stringify(resetTokens));
            const link = `${location.origin}${location.pathname}?resetToken=${token}`;
            showSuccess(sucEl, `Ссылка: ${link}`);
        };

        window.showRegistrationForm = function() {
            removeExistingModals();
            const modal = document.createElement('div');
            modal.className = 'modal-form';
            modal.innerHTML = `
                <div class="form-title">Регистрация</div>
                <div id="registerError" class="error-text hidden"></div>
                <input id="regName" class="form-input" placeholder="Имя">
                <input id="regUsername" class="form-input" placeholder="Никнейм">
                <input id="regEmail" class="form-input" placeholder="Email">
                <input id="regPassword" class="form-input" type="password" placeholder="Пароль">
                <input id="regConfirmPassword" class="form-input" type="password" placeholder="Подтверждение">
                <button class="gold-button" onclick="window.register()">Зарегистрироваться</button>
                <span class="text-link" onclick="showLoginForm()">← Войти</span>
            `;
            document.body.appendChild(modal);
        };

        window.login = function() {
            const username = document.getElementById('loginUsername')?.value.trim();
            const pass = document.getElementById('loginPassword')?.value;
            const err = document.getElementById('loginError');
            if (!username || !pass) return showError(err, 'Заполните поля');
            if (!users[username] || users[username].password !== pass) return showError(err, 'Неверные данные');
            currentUser = username;
            localStorage.setItem('currentSession', JSON.stringify({username, timestamp: Date.now()}));
            removeExistingModals();
            showMainContent();
            showWelcomeMessage(users[username].name);
            renderCards();
        };

        window.register = function() {
            const name = document.getElementById('regName')?.value.trim();
            const username = document.getElementById('regUsername')?.value.trim();
            const email = document.getElementById('regEmail')?.value.trim();
            const pass = document.getElementById('regPassword')?.value;
            const confirm = document.getElementById('regConfirmPassword')?.value;
            const err = document.getElementById('registerError');
            if (!name || !username || !email || !pass || !confirm) return showError(err, 'Все поля обязательны');
            if (!/[a-zA-Zа-яА-ЯЁё]/.test(name)) return showError(err, 'Имя должно содержать буквы');
            if (pass.length < 6) return showError(err, 'Пароль от 6 символов');
            if (pass !== confirm) return showError(err, 'Пароли не совпадают');
            if (users[username]) return showError(err, 'Никнейм занят');
            users[username] = { name, email, password: pass, balance: 0, friends: [], friendRequests: [], registrationDate: new Date().toISOString() };
            localStorage.setItem('bankUsers', JSON.stringify(users));
            currentUser = username;
            localStorage.setItem('currentSession', JSON.stringify({username, timestamp: Date.now()}));
            removeExistingModals();
            showMainContent();
            showWelcomeMessage(name);
            renderCards();
        };

        function showMainContent() {
            document.querySelector('header')?.classList.remove('hidden');
            document.querySelector('.main-container')?.classList.remove('hidden');
            toggleSection('about');
        }

        function showWelcomeMessage(name) {
            const toast = document.createElement('div');
            toast.className = 'toast-message';
            toast.innerHTML = `<strong>✨ Добро пожаловать, ${name}!</strong>`;
            document.body.appendChild(toast);
            setTimeout(() => { toast.classList.add('fade-out'); setTimeout(() => toast.remove(), 800); }, 3000);
        }

        window.toggleSection = function(section) {
            ['about-section','services-section','cards-section','contact-section','profile-section'].forEach(id => {
                const el = document.getElementById(id);
                if (el) el.classList.add('hidden');
            });
            if (section === 'about') document.getElementById('about-section')?.classList.remove('hidden');
            else if (section === 'services') document.getElementById('services-section')?.classList.remove('hidden');
            else if (section === 'cards') { document.getElementById('cards-section')?.classList.remove('hidden'); renderCards(); }
            else if (section === 'contact') document.getElementById('contact-section')?.classList.remove('hidden');
            else if (section === 'profile') showProfile();
        };

        function showProfile() {
            const user = users[currentUser];
            const container = document.getElementById('profile-section');
            container.innerHTML = `
                <h2>Личный кабинет</h2><div class="divider"></div>
                <div class="profile-header">
                    <img src="https://github.com/lybat25/BK-Bank/blob/main/png/2025-01-30_17-50-13-Photoroom.png?raw=true" class="profile-avatar">
                    <div><strong style="font-size:1.5rem;">${user.name}</strong><br>${currentUser}</div>
                    <button class="logout-btn" onclick="window.logout()">Выйти</button>
                </div>
                <p><strong>Email:</strong> ${user.email} &nbsp;|&nbsp; <strong>Баланс:</strong> ${user.balance} ₽</p>
                <div class="friend-actions">
                    <input id="friendName" class="friend-input" placeholder="Имя или Email друга">
                    <button class="small-gold-btn" onclick="window.sendFriendRequest()">Добавить</button>
                </div>
                <h3>Друзья</h3>
                <div class="friend-list">${user.friends.length ? user.friends.map(f => `<span class="friend-tag">${f}</span>`).join('') : 'Пока нет друзей'}</div>
                <h3>Запросы</h3>
                <div class="friend-list">${user.friendRequests.length ? user.friendRequests.map(r => `<span class="friend-tag">${r} <button onclick="window.acceptFriendRequest('${r}')">✓</button> <button onclick="window.declineFriendRequest('${r}')">✗</button></span>`).join('') : 'Нет запросов'}</div>
            `;
            container.classList.remove('hidden');
        }

        window.logout = function() { localStorage.removeItem('currentSession'); location.reload(); };
        window.sendFriendRequest = function() { /* логика без изменений */ 
            const val = document.getElementById('friendName')?.value.trim(); if(!val) return alert('Введите данные'); 
            let found = null; for(let u in users) if(u === val || users[u].email === val) { found = u; break; } 
            if(!found) return alert('Не найден'); if(found === currentUser) return alert('Нельзя себя'); 
            if(users[currentUser].friends.includes(found)) return alert('Уже друг');
            users[found].friendRequests.push(currentUser); localStorage.setItem('bankUsers', JSON.stringify(users)); alert('Запрос отправлен'); showProfile(); 
        };
        window.acceptFriendRequest = function(f) { 
            const u = users[currentUser]; u.friendRequests = u.friendRequests.filter(r=>r!==f); if(!u.friends.includes(f)) u.friends.push(f); 
            if(!users[f].friends.includes(currentUser)) users[f].friends.push(currentUser); localStorage.setItem('bankUsers', JSON.stringify(users)); showProfile(); 
        };
        window.declineFriendRequest = function(f) { users[currentUser].friendRequests = users[currentUser].friendRequests.filter(r=>r!==f); localStorage.setItem('bankUsers', JSON.stringify(users)); showProfile(); };

        function removeExistingModals() { document.querySelectorAll('.modal-form').forEach(m => m.remove()); }
        function showError(el, msg) { if(!el) return; el.textContent = msg; el.classList.remove('hidden'); setTimeout(() => el.classList.add('hidden'), 3000); }
        function showSuccess(el, msg) { if(!el) return; el.textContent = msg; el.classList.remove('hidden'); setTimeout(() => el.classList.add('hidden'), 5000); }

        // Глобальные ссылки для onclick
        window.login = login;
        window.register = register;
        window.showForgotPasswordForm = showForgotPasswordForm;
        window.showRegistrationForm = showRegistrationForm;
        window.sendResetEmail = sendResetEmail;
        window.logout = logout;
        window.toggleSection = toggleSection;
        window.sendFriendRequest = sendFriendRequest;
        window.acceptFriendRequest = acceptFriendRequest;
        window.declineFriendRequest = declineFriendRequest;
    })();
</script>
</body>
</html>
