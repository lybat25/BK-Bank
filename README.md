<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БК-Банк - Восстановление пароля</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #121212 0%, #1e1e1e 100%);
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            width: 100%;
            max-width: 500px;
            background: #2a2a2a;
            border-radius: 12px;
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.2);
            overflow: hidden;
        }
        
        .header {
            background: #1f1f1f;
            padding: 25px;
            text-align: center;
            border-bottom: 2px solid #FFD700;
        }
        
        .logo {
            width: 120px;
            height: auto;
            margin-bottom: 15px;
        }
        
        h1 {
            color: #FFD700;
            font-size: 28px;
            margin-bottom: 10px;
        }
        
        .subtitle {
            color: #cccccc;
            font-size: 16px;
        }
        
        .content {
            padding: 30px;
        }
        
        .step {
            display: none;
            animation: fadeIn 0.5s ease;
        }
        
        .step.active {
            display: block;
        }
        
        .form-group {
            margin-bottom: 20px;
            position: relative;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            color: #FFD700;
            font-weight: bold;
        }
        
        input {
            width: 100%;
            padding: 14px 14px 14px 40px;
            border: none;
            border-radius: 6px;
            background: #1e1e1e;
            color: #ffffff;
            font-size: 16px;
            border: 1px solid #333;
            transition: border-color 0.3s;
        }
        
        input:focus {
            outline: none;
            border-color: #FFD700;
        }
        
        .input-icon {
            position: absolute;
            left: 12px;
            top: 40px;
            color: #FFD700;
        }
        
        button {
            width: 100%;
            padding: 14px;
            background: #FFD700;
            color: #000;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        button:hover {
            background: #ffcc00;
        }
        
        button:disabled {
            background: #666;
            cursor: not-allowed;
        }
        
        .message {
            padding: 12px;
            border-radius: 6px;
            margin-bottom: 20px;
            text-align: center;
            font-weight: bold;
        }
        
        .error {
            background: rgba(255, 68, 68, 0.2);
            color: #ff4444;
            border: 1px solid #ff4444;
        }
        
        .success {
            background: rgba(76, 175, 80, 0.2);
            color: #4CAF50;
            border: 1px solid #4CAF50;
        }
        
        .info {
            background: rgba(33, 150, 243, 0.2);
            color: #2196F3;
            border: 1px solid #2196F3;
        }
        
        .timer {
            text-align: center;
            margin-top: 15px;
            color: #FFD700;
            font-weight: bold;
        }
        
        .links {
            text-align: center;
            margin-top: 25px;
        }
        
        .links a {
            color: #FFD700;
            text-decoration: none;
            margin: 0 10px;
            font-weight: bold;
            transition: color 0.3s;
        }
        
        .links a:hover {
            color: #ffcc00;
            text-decoration: underline;
        }
        
        .password-strength {
            height: 5px;
            margin-top: 8px;
            border-radius: 3px;
            background: #333;
            overflow: hidden;
        }
        
        .strength-meter {
            height: 100%;
            width: 0;
            transition: width 0.3s, background 0.3s;
        }
        
        .password-rules {
            margin-top: 8px;
            font-size: 13px;
            color: #999;
        }
        
        .rule {
            margin-bottom: 4px;
            display: flex;
            align-items: center;
        }
        
        .rule i {
            margin-right: 5px;
            width: 16px;
        }
        
        .rule.valid {
            color: #4CAF50;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .loader {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255, 215, 0, 0.3);
            border-radius: 50%;
            border-top-color: #FFD700;
            animation: spin 1s ease-in-out infinite;
            margin-right: 10px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        @media (max-width: 600px) {
            .container {
                border-radius: 0;
            }
            
            .content {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://github.com/lybat25/BK-Bank/blob/main/png/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2025-02-11_142359079.png?raw=true" alt="БК-Банк" class="logo">
            <h1>Восстановление пароля</h1>
            <p class="subtitle">Введите данные для сброса пароля</p>
        </div>
        
        <div class="content">
            <!-- Шаг 1: Ввод email -->
            <div class="step active" id="step1">
                <div class="message info">
                    На вашу почту будет отправлена ссылка для сброса пароля
                </div>
                
                <div class="form-group">
                    <label for="email">Email адрес</label>
                    <i class="fas fa-envelope input-icon"></i>
                    <input type="email" id="email" placeholder="Введите ваш email" required>
                </div>
                
                <button onclick="sendResetEmail()" id="sendEmailBtn">
                    <span>Отправить ссылку для сброса</span>
                </button>
                
                <div class="links">
                    <a href="#" onclick="showLogin()">Вернуться к входу</a>
                </div>
            </div>
            
            <!-- Шаг 2: Ввод кода подтверждения -->
            <div class="step" id="step2">
                <div class="message info">
                    Код подтверждения отправлен на вашу почту
                </div>
                
                <div class="form-group">
                    <label for="code">Код подтверждения</label>
                    <i class="fas fa-key input-icon"></i>
                    <input type="text" id="code" placeholder="Введите код из письма" required maxlength="6">
                </div>
                
                <div class="timer" id="timer">Код действителен: 04:59</div>
                
                <button onclick="verifyCode()" id="verifyCodeBtn">
                    <span>Подтвердить код</span>
                </button>
                
                <div class="links">
                    <a href="#" onclick="resendCode()">Отправить код повторно</a>
                </div>
            </div>
            
            <!-- Шаг 3: Ввод нового пароля -->
            <div class="step" id="step3">
                <div class="message success">
                    Email успешно подтвержден
                </div>
                
                <div class="form-group">
                    <label for="newPassword">Новый пароль</label>
                    <i class="fas fa-lock input-icon"></i>
                    <input type="password" id="newPassword" placeholder="Введите новый пароль" required onkeyup="checkPasswordStrength()">
                    <div class="password-strength">
                        <div class="strength-meter" id="passwordStrengthMeter"></div>
                    </div>
                    <div class="password-rules">
                        <div class="rule" id="lengthRule"><i class="fas fa-circle"></i> Не менее 8 символов</div>
                        <div class="rule" id="uppercaseRule"><i class="fas fa-circle"></i> Содержит заглавные буквы</div>
                        <div class="rule" id="numberRule"><i class="fas fa-circle"></i> Содержит цифры</div>
                        <div class="rule" id="specialRule"><i class="fas fa-circle"></i> Содержит специальные символы</div>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="confirmPassword">Подтверждение пароля</label>
                    <i class="fas fa-lock input-icon"></i>
                    <input type="password" id="confirmPassword" placeholder="Повторите новый пароль" required onkeyup="checkPasswordMatch()">
                    <div id="passwordMatch" style="margin-top: 8px; font-size: 13px;"></div>
                </div>
                
                <button onclick="resetPassword()" id="resetPasswordBtn">
                    <span>Установить новый пароль</span>
                </button>
            </div>
            
            <!-- Шаг 4: Успешное завершение -->
            <div class="step" id="step4">
                <div class="message success">
                    <i class="fas fa-check-circle"></i> Пароль успешно изменен!
                </div>
                
                <p style="text-align: center; margin: 20px 0;">
                    Теперь вы можете войти в систему с новым паролем.
                </p>
                
                <button onclick="showLogin()">
                    <span>Перейти к входу</span>
                </button>
            </div>
        </div>
    </div>

    <script>
        // Глобальные переменные
        let resetCode = '';
        let userEmail = '';
        let countdownInterval;
        let passwordValid = false;
        let passwordsMatch = false;
        
        // Функция для отправки email с кодом подтверждения
        function sendResetEmail() {
            const email = document.getElementById('email').value.trim();
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            const btn = document.getElementById('sendEmailBtn');
            
            if (!email) {
                showMessage('Пожалуйста, введите email адрес', 'error');
                return;
            }
            
            if (!emailRegex.test(email)) {
                showMessage('Пожалуйста, введите корректный email адрес', 'error');
                return;
            }
            
            // Показываем индикатор загрузки
            btn.innerHTML = '<div class="loader"></div><span>Отправка...</span>';
            btn.disabled = true;
            
            // Имитация отправки email
            setTimeout(() => {
                // Сохраняем email
                userEmail = email;
                
                // Генерируем случайный 6-значный код
                resetCode = Math.floor(100000 + Math.random() * 900000).toString();
                
                // В реальном приложении здесь был бы код отправки email
                // Для демонстрации покажем код в сообщении
                showMessage(`Код подтверждения отправлен на ${email}. Для демонстрации: ${resetCode}`, 'success');
                
                // Восстанавливаем кнопку
                btn.innerHTML = '<span>Отправить ссылку для сброса</span>';
                btn.disabled = false;
                
                // Переходим к следующему шагу
                showStep(2);
                
                // Запускаем таймер
                startTimer(5 * 60); // 5 минут
            }, 1500);
        }
        
        // Функция для проверки кода подтверждения
        function verifyCode() {
            const code = document.getElementById('code').value.trim();
            const btn = document.getElementById('verifyCodeBtn');
            
            if (!code) {
                showMessage('Пожалуйста, введите код подтверждения', 'error');
                return;
            }
            
            if (code !== resetCode) {
                showMessage('Неверный код подтверждения', 'error');
                return;
            }
            
            // Показываем индикатор загрузки
            btn.innerHTML = '<div class="loader"></div><span>Проверка...</span>';
            btn.disabled = true;
            
            // Имитация проверки кода
            setTimeout(() => {
                // Останавливаем таймер
                clearInterval(countdownInterval);
                
                // Восстанавливаем кнопку
                btn.innerHTML = '<span>Подтвердить код</span>';
                btn.disabled = false;
                
                // Переходим к следующему шагу
                showStep(3);
            }, 1000);
        }
        
        // Функция для сброса пароля
        function resetPassword() {
            const newPassword = document.getElementById('newPassword').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            const btn = document.getElementById('resetPasswordBtn');
            
            if (!newPassword || !confirmPassword) {
                showMessage('Пожалуйста, заполните все поля', 'error');
                return;
            }
            
            if (newPassword.length < 8) {
                showMessage('Пароль должен содержать минимум 8 символов', 'error');
                return;
            }
            
            if (newPassword !== confirmPassword) {
                showMessage('Пароли не совпадают', 'error');
                return;
            }
            
            // Показываем индикатор загрузки
            btn.innerHTML = '<div class="loader"></div><span>Обновление...</span>';
            btn.disabled = true;
            
            // Имитация обновления пароля
            setTimeout(() => {
                // В реальном приложении здесь был бы код обновления пароля в базе данных
                // Для демонстрации просто покажем успешное сообщение
                
                // Сохраняем в localStorage для демонстрации
                const users = JSON.parse(localStorage.getItem('bankUsers')) || {};
                let userFound = false;
                
                for (const username in users) {
                    if (users[username].email === userEmail) {
                        users[username].password = newPassword;
                        userFound = true;
                        break;
                    }
                }
                
                if (!userFound) {
                    // Создаем демо-пользователя
                    users['demo_user'] = {
                        name: 'Демо пользователь',
                        email: userEmail,
                        password: newPassword,
                        balance: 0,
                        friends: [],
                        friendRequests: [],
                        registrationDate: new Date().toISOString()
                    };
                }
                
                localStorage.setItem('bankUsers', JSON.stringify(users));
                
                // Восстанавливаем кнопку
                btn.innerHTML = '<span>Установить новый пароль</span>';
                btn.disabled = false;
                
                // Переходим к завершающему шагу
                showStep(4);
            }, 1500);
        }
        
        // Функция для проверки сложности пароля
        function checkPasswordStrength() {
            const password = document.getElementById('newPassword').value;
            const strengthMeter = document.getElementById('passwordStrengthMeter');
            const lengthRule = document.getElementById('lengthRule');
            const uppercaseRule = document.getElementById('uppercaseRule');
            const numberRule = document.getElementById('numberRule');
            const specialRule = document.getElementById('specialRule');
            
            let strength = 0;
            let color = '#ff4444';
            
            // Проверка длины
            if (password.length >= 8) {
                strength += 25;
                lengthRule.classList.add('valid');
                lengthRule.innerHTML = '<i class="fas fa-check-circle"></i> Не менее 8 символов';
            } else {
                lengthRule.classList.remove('valid');
                lengthRule.innerHTML = '<i class="fas fa-circle"></i> Не менее 8 символов';
            }
            
            // Проверка заглавных букв
            if (/[A-ZА-Я]/.test(password)) {
                strength += 25;
                uppercaseRule.classList.add('valid');
                uppercaseRule.innerHTML = '<i class="fas fa-check-circle"></i> Содержит заглавные буквы';
            } else {
                uppercaseRule.classList.remove('valid');
                uppercaseRule.innerHTML = '<i class="fas fa-circle"></i> Содержит заглавные буквы';
            }
            
            // Проверка цифр
            if (/\d/.test(password)) {
                strength += 25;
                numberRule.classList.add('valid');
                numberRule.innerHTML = '<i class="fas fa-check-circle"></i> Содержит цифры';
            } else {
                numberRule.classList.remove('valid');
                numberRule.innerHTML = '<i class="fas fa-circle"></i> Содержит цифры';
            }
            
            // Проверка специальных символов
            if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
                strength += 25;
                specialRule.classList.add('valid');
                specialRule.innerHTML = '<i class="fas fa-check-circle"></i> Содержит специальные символы';
            } else {
                specialRule.classList.remove('valid');
                specialRule.innerHTML = '<i class="fas fa-circle"></i> Содержит специальные символы';
            }
            
            // Определение цвета
            if (strength >= 75) {
                color = '#4CAF50';
                passwordValid = true;
            } else if (strength >= 50) {
                color = '#FFD700';
                passwordValid = false;
            } else if (strength >= 25) {
                color = '#ff9800';
                passwordValid = false;
            } else {
                passwordValid = false;
            }
            
            // Обновление индикатора
            strengthMeter.style.width = strength + '%';
            strengthMeter.style.background = color;
            
            // Проверка совпадения паролей
            checkPasswordMatch();
        }
        
        // Функция для проверки совпадения паролей
        function checkPasswordMatch() {
            const password = document.getElementById('newPassword').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            const matchElement = document.getElementById('passwordMatch');
            
            if (confirmPassword.length === 0) {
                matchElement.textContent = '';
                passwordsMatch = false;
                return;
            }
            
            if (password === confirmPassword) {
                matchElement.innerHTML = '<i class="fas fa-check-circle" style="color:#4CAF50"></i> Пароли совпадают';
                matchElement.style.color = '#4CAF50';
                passwordsMatch = true;
            } else {
                matchElement.innerHTML = '<i class="fas fa-times-circle" style="color:#ff4444"></i> Пароли не совпадают';
                matchElement.style.color = '#ff4444';
                passwordsMatch = false;
            }
        }
        
        // Функция для повторной отправки кода
        function resendCode() {
            // Генерируем новый код
            resetCode = Math.floor(100000 + Math.random() * 900000).toString();
            
            // В реальном приложении здесь был бы код отправки email
            showMessage(`Новый код подтверждения отправлен на ${userEmail}. Для демонстрации: ${resetCode}`, 'success');
            
            // Сбрасываем и перезапускаем таймер
            clearInterval(countdownInterval);
            startTimer(5 * 60); // 5 минут
        }
        
        // Функция для запуска таймера
        function startTimer(duration) {
            const timerElement = document.getElementById('timer');
            let timer = duration;
            let minutes, seconds;
            
            countdownInterval = setInterval(function() {
                minutes = parseInt(timer / 60, 10);
                seconds = parseInt(timer % 60, 10);
                
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;
                
                timerElement.textContent = "Код действителен: " + minutes + ":" + seconds;
                timerElement.style.color = "#FFD700";
                
                if (--timer < 0) {
                    clearInterval(countdownInterval);
                    timerElement.textContent = "Код устарел";
                    timerElement.style.color = "#ff4444";
                }
            }, 1000);
        }
        
        // Функция для отображения сообщения
        function showMessage(message, type) {
            // Удаляем предыдущие сообщения
            const existingMessages = document.querySelectorAll('.message');
            existingMessages.forEach(msg => msg.remove());
            
            // Создаем новое сообщение
            const messageElement = document.createElement('div');
            messageElement.className = `message ${type}`;
            messageElement.innerHTML = message;
            
            // Вставляем сообщение в начало контента
            const content = document.querySelector('.content');
            const activeStep = content.querySelector('.step.active');
            content.insertBefore(messageElement, activeStep);
            
            // Автоматически скрываем сообщение через 5 секунд
            if (type !== 'info') {
                setTimeout(() => {
                    messageElement.remove();
                }, 5000);
            }
        }
        
        // Функция для переключения между шагами
        function showStep(stepNumber) {
            // Скрываем все шаги
            document.querySelectorAll('.step').forEach(step => {
                step.classList.remove('active');
            });
            
            // Показываем выбранный шаг
            document.getElementById(`step${stepNumber}`).classList.add('active');
        }
        
        // Функция для перехода к форме входа
        function showLogin() {
            // В реальном приложении здесь был бы переход на страницу входа
            alert('В реальном приложении здесь будет переход на страницу входа');
            // Обычно это: window.location.href = 'login.html';
        }
        
        // Инициализация при загрузке страницы
        window.onload = function() {
            // Показываем первый шаг
            showStep(1);
            
            // Проверяем, есть ли email в URL параметрах
            const urlParams = new URLSearchParams(window.location.search);
            const email = urlParams.get('email');
            
            if (email) {
                document.getElementById('email').value = email;
            }
        };
    </script>
</body>
</html>
