// Инициализация при загрузке страницы
window.onload = function() {
    // Проверка, есть ли сохраненные данные в localStorage
    const savedUser  = localStorage.getItem('user');
    if (savedUser ) {
        const user = JSON.parse(savedUser );
        showProfile(user.name, user.email, user.accessCode);
    } else {
        // Показ формы регистрации, если пользователь не найден
        showRegistrationForm();
    }

    // Подключение к WebSocket для считывания количества пользователей
    const userCountElement = document.getElementById('currentUser Count');
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

// Функция для отображения формы регистрации
function showRegistrationForm() {
    const registrationForm = document.createElement('div');
    registrationForm.className = 'registration-form';
    registrationForm.innerHTML = `
        <h2>Регистрация</h2>
        <input type="text" id="name" placeholder="Ваш никнейм" required>
        <input type="email" id="email" placeholder="Ваша электронная почта" required>
        <input type="password" id="password" placeholder="Пароль" required>
        <input type="text" id="accessCode" placeholder="Код доступа" required>
        <button onclick="register()">Зарегистрироваться</button>
        <p><a href="#" onclick="showPasswordRecoveryForm()">Забыли пароль?</a></p>
    `;
    document.body.appendChild(registrationForm);
}

// Функция для регистрации пользователя
function register() {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const accessCode = document.getElementById('accessCode').value;

    // Валидация данных
    if (!name || !email || !password || !accessCode) {
        alert("Пожалуйста, заполните все поля.");
        return;
    }

    // Сохранение данных в localStorage
    const user = {
        name: name,
        email: email,
        accessCode: accessCode,
        balance: 0 // Инициализируем баланс
    };
    localStorage.setItem('user', JSON.stringify(user));

    alert(`Добро пожаловать, ${name}!`);
    showProfile(name, email, accessCode);
}

// Функция для отображения профиля пользователя
function showProfile(name, email, accessCode) {
    const profileSection = document.createElement('div');
    profileSection.className = 'profile-section';
    profileSection.innerHTML = `
        <h2>Ваш Кабинет</h2>
        <p>Имя: ${name}</p>
        <p>Email: ${email}</p>
        <p>Код доступа: ${accessCode}</p>
        <button onclick="logout()">Выйти</button>
    `;
    document.body.appendChild(profileSection);
}

// Функция для выхода из аккаунта
function logout() {
    localStorage.removeItem('user');
    alert("Вы вышли из аккаунта.");
    document.body.innerHTML = ''; // Очищаем содержимое страницы
    showRegistrationForm(); // Показываем форму регистрации снова
}

// Функция для восстановления пароля
function showPasswordRecoveryForm() {
    const recoveryForm = document.createElement('div');
    recoveryForm.className = 'recovery-form';
    recoveryForm.innerHTML = `
        <h2>Восстановление пароля</h2>
        <input type="email" id="recoveryEmail" placeholder="Введите вашу электронную почту" required>
        <button onclick="recoverPassword()">Восстановить пароль</button>
        <p><a href="#" onclick="showRegistrationForm()">Назад к регистрации</a></p>
    `;
    document.body.innerHTML = ''; // Очищаем содержимое страницы
    document.body.appendChild(recoveryForm);
}

// Функция для обработки восстановления пароля
function recoverPassword() {
    const email = document.getElementById('recoveryEmail').value;
    alert(`Ссылка для восстановления пароля отправлена на ${email}.`);
