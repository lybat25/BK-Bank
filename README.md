// Пример адаптации функции регистрации для Readmi
async function register() {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const accessCode = document.getElementById('accessCode').value;

    // Валидация данных
    if (!validateName(name) || !validateEmail(email) || !validatePassword(password) || !validateAccessCode(accessCode)) {
        return;
    }

    // Отправка данных на сервер Readmi
    try {
        const response = await fetch('https://api.readmi.com/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name,
                email,
                password,
                accessCode,
            }),
        });

        if (!response.ok) {
            throw new Error('Ошибка регистрации');
        }

        const user = await response.json();
        showProfile(user);
    } catch (error) {
        alert(error.message);
    }
}

// Пример адаптации функции входа в систему
async function login(email, password) {
    try {
        const response = await fetch('https://api.readmi.com/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                password,
            }),
        });

        if (!response.ok) {
            throw new Error('Ошибка входа');
        }

        const user = await response.json();
        showProfile(user);
    } catch (error) {
        alert(error.message);
    }
}

// Пример адаптации функции пополнения баланса
async function processPayment() {
    const cardNumber = document.getElementById('cardNumber').value.replace(/\s/g, '');
    const cardExpiry = document.getElementById('cardExpiry').value;
    const cardCvv = document.getElementById('cardCvv').value;
    const amount = parseFloat(document.getElementById('depositAmount').value);

    // Валидация данных
    if (!validateCardNumber(cardNumber) || !validateCardExpiry(cardExpiry) || !validateCardCvv(cardCvv) || !validateAmount(amount)) {
        return;
    }

    // Отправка данных на сервер Readmi
    try {
        const response = await fetch('https://api.readmi.com/payment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                cardNumber,
                cardExpiry,
                cardCvv,
                amount,
            }),
        });

        if (!response.ok) {
            throw new Error('Ошибка оплаты');
        }

        const result = await response.json();
        alert(`Платеж на сумму ${amount} руб. успешно обработан!`);
    } catch (error) {
        alert(error.message);
    }
}
