<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БК-Банк - Ваш надежный банк</title>
    <link rel="stylesheet" href="styles.css"> <!-- Подключите свой CSS файл -->
    <style>
        /* Ваши стили остаются без изменений */
        /* ... */
        .feedback-section {
            margin-top: 20px;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        .feedback-section input, .feedback-section textarea {
            margin-bottom: 10px;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
            width: 100%;
        }
        .feedback-section button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
        }
        .feedback-section button:hover {
            background: #ffcc00; /* Более светлый желтый при наведении */
        }
        .user-list {
            margin-top: 20px;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        .user-item {
            margin-bottom: 10px;
            padding: 10px;
            background: #1e1e1e;
            border-radius: 4px;
        }
        .offers-section {
            margin-top: 20px;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        .offer-item {
            margin-bottom: 15px;
            padding: 10px;
            background: #1e1e1e;
            border-radius: 4px;
        }
        .offer-item h4 {
            color: #FFD700;
        }
        .add-offer-form {
            margin-top: 20px;
            padding: 10px;
            background: #1e1e1e;
            border-radius: 4px;
        }
        .add-offer-form input {
            margin-bottom: 10px;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #1e1e1e;
            color: #ffffff;
            width: 100%;
        }
        .add-offer-form button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background: #FFD700;
            color: #000;
            cursor: pointer;
        }
        .add-offer-form button:hover {
            background: #ffcc00; /* Более светлый желтый при наведении */
        }
        .transaction-history {
            margin-top: 20px;
            padding: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        .transaction-item {
            margin-bottom: 10px;
            padding: 10px;
            background: #1e1e1e;
            border-radius: 4px;
        }
        .download-report {
            margin-top: 20px;
            padding: 10px;
            background: #FFD700;
            color: #000;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .download-report:hover {
            background: #ffcc00; /* Более светлый желтый при наведении */
        }
    </style>
    <script>
        const translations = {
            ru: {
                title: "БК-Банк - Ваш надежный банк",
                welcome: "Добро пожаловать, {name}! Мы рады видеть вас на нашем сайте.",
                registration: "Регистрация",
                namePlaceholder: "Ваш никнейм",
                emailPlaceholder: "Ваша электронная почта",
                passwordPlaceholder: "Пароль",
                registerButton: "Зарегистрироваться",
                profileTitle: "Ваш Кабинет",
                emailLabel: "Email:",
                logoutButton: "Выйти",
                servicesTitle: "Наши услуги",
                servicesList: [
                    "Кредитование",
                    "Депозиты",
                    "Инвестиционные услуги",
                    "Консультации по финансовым вопросам",
                    "Онлайн-банкинг"
                ],
                contactInfoTitle: "Контактная информация",
                contactEmail: "bkbank636@gmail.com",
                discord: "БК-Банк server",
                telegram: "БК-Банк channel",
                youtube: "БК-Банк YouTube",
                token: "БК-Банк Token (ещё не вышел)",
                faqTitle: "Часто задаваемые вопросы",
                faqList: [
                    { question: "Как открыть счет?", answer: "Чтобы открыть счет, вам нужно заполнить форму регистрации на нашем сайте." },
                    { question: "Как получить кредит?", answer: "Для получения кредита необходимо подать заявку через наш онлайн-сервис." },
                    { question: "Как связаться с поддержкой?", answer: "Вы можете связаться с нашей службой поддержки по электронной почте или через чат на сайте." }
                ],
                reviewsTitle: "Отзывы клиентов",
                reviewsList: [
                    { name: "Иван", text: "Отличный банк! Удобный интерфейс и быстрая поддержка." },
                    { name: "Мария", text: "Я довольна услугами. Рекомендую всем!" },
                    { name: "Алексей", text: "Хорошие условия по кредитам." }
                ],
                newsTitle: "Новости",
                newsList: [
                    { title: "Запуск новой кредитной карты", content: "Мы рады сообщить о запуске новой кредитной карты с низкими процентными ставками." },
                    { title: "Обновление мобильного приложения", content: "Наше мобильное приложение теперь стало еще удобнее и функциональнее." },
                    { title: "Новая программа лояльности", content: "Запускаем новую программу лояльности для наших постоянных клиентов." }
                ],
                partnersTitle: "Наши партнеры",
                partnersList: [
                    { name: "Компания А", description: "Лидер в области финансовых технологий." },
                    { name: "Компания Б", description: "Надежный поставщик услуг." },
                    { name: "Компания В", description: "Партнер в области кредитования." }
                ],
                privacyPolicyTitle: "Политика конфиденциальности",
                privacyPolicyContent: "Мы уважаем вашу конфиденциальность и обязуемся защищать ваши личные данные. Мы не будем передавать ваши данные третьим лицам без вашего согласия.",
                calculatorTitle: "Калькулятор кредита",
                loanAmountPlaceholder: "Сумма кредита",
                interestRatePlaceholder: "Процентная ставка (%)",
                loanTermPlaceholder: "Срок кредита (лет)",
                calculateButton: "Рассчитать",
                monthlyPaymentLabel: "Ежемесячный платеж:",
                offersTitle: "Акции и предложения",
                addOfferButton: "Добавить акцию",
                offerNamePlaceholder: "Название акции",
                offerDescriptionPlaceholder: "Описание акции",
                feedbackTitle: "Обратная связь",
                feedbackMessagePlaceholder: "Ваше сообщение",
                sendFeedbackButton: "Отправить",
                userListTitle: "Список пользователей",
                transactionHistoryTitle: "История операций",
                downloadReportButton: "Скачать отчет",
                // Добавьте другие переводы по мере необходимости
            },
            en: {
                title: "BK-Bank - Your Reliable Bank",
                welcome: "Welcome, {name}! We are glad to see you on our site.",
                registration: "Registration",
                namePlaceholder: "Your nickname",
                emailPlaceholder: "Your email",
                passwordPlaceholder: "Password",
                registerButton: "Register",
                profileTitle: "Your Profile",
                emailLabel: "Email:",
                logoutButton: "Logout",
                servicesTitle: "Our Services",
                servicesList: [
                    "Lending",
                    "Deposits",
                    "Investment Services",
                    "Financial Consulting",
                    "Online Banking"
                ],
                contactInfoTitle: "Contact Information",
                contactEmail: "bkbank636@gmail.com",
                discord: "BK-Bank server",
                telegram: "BK-Bank channel",
                youtube: "BK-Bank YouTube",
                token: "BK-Bank Token (not released yet)",
                faqTitle: "Frequently Asked Questions",
                faqList: [
                    { question: "How to open an account?", answer: "To open an account, you need to fill out the registration form on our website." },
                    { question: "How to get a loan?", answer: "To get a loan, you need to apply through our online service." },
                    { question: "How to contact support?", answer: "You can contact our support service via email or through the chat on the website." }
                ],
                reviewsTitle: "Customer Reviews",
                reviewsList: [
                    { name: "Ivan", text: "Great bank! Convenient interface and quick support." },
                    { name: "Maria", text: "I am satisfied with the services. I recommend it to everyone!" },
                    { name: "Alexey", text: "Good loan conditions." }
                ],
                newsTitle: "News",
                newsList: [
                    { title: "Launch of a new credit card", content: "We are pleased to announce the launch of a new credit card with low interest rates." },
                    { title: "Mobile app update", content: "Our mobile app has become even more convenient and functional." },
                    { title: "New loyalty program", content: "We are launching a new loyalty program for our regular customers." }
                ],
                partnersTitle: "Our Partners",
                partnersList: [
                    { name: "Company A", description: "Leader in financial technology." },
                    { name: "Company B", description: "Reliable service provider." },
                    { name: "Company C", description: "Partner in lending." }
                ],
                privacyPolicyTitle: "Privacy Policy",
                privacyPolicyContent: "We respect your privacy and are committed to protecting your personal data. We will not share your data with third parties without your consent.",
                calculatorTitle: "Loan Calculator",
                loanAmountPlaceholder: "Loan Amount",
                interestRatePlaceholder: "Interest Rate (%)",
                loanTermPlaceholder: "Loan Term (years)",
                calculateButton: "Calculate",
                monthlyPaymentLabel: "Monthly Payment:",
                offersTitle: "Offers and Promotions",
                addOfferButton: "Add Offer",
                offerNamePlaceholder: "Offer Name",
                offerDescriptionPlaceholder: "Offer Description",
                feedbackTitle: "Feedback",
                feedbackMessagePlaceholder: "Your message",
                sendFeedbackButton: "Send",
                userListTitle: "User  List",
                transactionHistoryTitle: "Transaction History",
                downloadReportButton: "Download Report",
                // Добавьте другие переводы по мере необходимости
            }
            // Добавьте другие языки по мере необходимости
        };

        let currentLanguage = 'ru'; // Установите язык по умолчанию

        window.onload = function() {
            // Проверка, есть ли сохраненные данные в localStorage
            const savedUser        = localStorage.getItem('user');
            if (savedUser       ) {
                const user = JSON.parse(savedUser       );
                showProfile(user.name, user.email);
            } else {
                // Скрываем все содержимое, кроме формы регистрации
                document.querySelectorAll('.container, header').forEach(el => el.classList.add('hidden'));
                // Показ формы регистрации
                showRegistrationForm();
            }

            // Всегда показываем главную страницу
            toggleSection('about');
            updateLanguage();
        };

        function updateLanguage() {
            document.title = translations[currentLanguage].title;
            // Обновите другие элементы на странице в зависимости от языка
            // Например, заголовки, текст кнопок и т.д.
            document.querySelector('.welcome-message').innerHTML = translations[currentLanguage].welcome.replace("{name}", user.name);
            // Обновление FAQ
            const faqSection = document.getElementById('faq');
            faqSection.innerHTML = `<h2>${translations[currentLanguage].faqTitle}</h2>`;
            translations[currentLanguage].faqList.forEach(item => {
                faqSection.innerHTML += `
                    <div class="faq-item">
                        <h4 onclick="toggleFAQ(this)">${item.question}</h4>
                        <div class="faq-answer">${item.answer}</div>
                    </div>
                `;
            });

            // Обновление отзывов
            const reviewsSection = document.getElementById('reviews');
            reviewsSection.innerHTML = `<h2>${translations[currentLanguage].reviewsTitle}</h2>`;
            translations[currentLanguage].reviewsList.forEach(review => {
                reviewsSection.innerHTML += `
                    <div class="review">
                        <strong>${review.name}</strong>: ${review.text}
                    </div>
                `;
            });

            // Обновление новостей
            const newsSection = document.getElementById('news');
            newsSection.innerHTML = `<h2>${translations[currentLanguage].newsTitle}</h2>`;
            translations[currentLanguage].newsList.forEach(news => {
                newsSection.innerHTML += `
                    <div class="news-item">
                        <h4 onclick="toggleNews(this)">${news.title}</h4>
                        <div class="news-content">${news.content}</div>
                    </div>
                `;
            });

            // Обновление партнеров
            const partnersSection = document.getElementById('partners');
            partnersSection.innerHTML = `<h2>${translations[currentLanguage].partnersTitle}</h2>`;
            translations[currentLanguage].partnersList.forEach(partner => {
                partnersSection.innerHTML += `
                    <div class="partner-item">
                        <h4>${partner.name}</h4>
                        <div class="partner-content">${partner.description}</div>
                    </div>
                `;
            });

            // Обновление политики конфиденциальности
            const privacyPolicySection = document.getElementById('privacy-policy');
            privacyPolicySection.innerHTML = `<h2>${translations[currentLanguage].privacyPolicyTitle}</h2>
                <p>${translations[currentLanguage].privacyPolicyContent}</p>`;

            // Обновление калькулятора кредита
            const calculatorSection = document.getElementById('calculator');
            calculatorSection.innerHTML = `
                <h2>${translations[currentLanguage].calculatorTitle}</h2>
                <input type="number" id="loanAmount" placeholder="${translations[currentLanguage].loanAmountPlaceholder}" required>
                <input type="number" id="interestRate" placeholder="${translations[currentLanguage].interestRatePlaceholder}" required>
                <input type="number" id="loanTerm" placeholder="${translations[currentLanguage].loanTermPlaceholder}" required>
                <button onclick="calculateLoan()">${translations[currentLanguage].calculateButton}</button>
                <div class="calculator-result" id="calculatorResult"></div>
            `;

            // Обновление акций и предложений
            const offersSection = document.getElementById('offers');
            offersSection.innerHTML = `<h2>${translations[currentLanguage].offersTitle}</h2>`;
            offersSection.innerHTML += `
                <div class="add-offer-form">
                    <input type="text" id="offerName" placeholder="${translations[currentLanguage].offerNamePlaceholder}" required>
                    <input type="text" id="offerDescription" placeholder="${translations[currentLanguage].offerDescriptionPlaceholder}" required>
                    <button onclick="addOffer()">${translations[currentLanguage].addOfferButton}</button>
                </div>
            `;

            // Обновление обратной связи
            const feedbackSection = document.getElementById('feedback');
            feedbackSection.innerHTML = `
                <h2>${translations[currentLanguage].feedbackTitle}</h2>
                <textarea id="feedbackMessage" placeholder="${translations[currentLanguage].feedbackMessagePlaceholder}" required></textarea>
                <button onclick="sendFeedback()">${translations[currentLanguage].sendFeedbackButton}</button>
            `;

            // Обновление списка пользователей
            const userListSection = document.getElementById('userList');
            userListSection.innerHTML = `<h2>${translations[currentLanguage].userListTitle}</h2>`;
            // Здесь можно добавить существующих пользователей, если они есть
            const users = JSON.parse(localStorage.getItem('users')) || []; // Получаем список пользователей из localStorage
            users.forEach(user => {
                userListSection.innerHTML += `
                    <div class="user-item">
                        <strong>${user.name}</strong> - ${user.email}
                    </div>
                `;
            });

            // Обновление истории операций
            const transactionHistorySection = document.getElementById('transactionHistory');
            transactionHistorySection.innerHTML = `<h2>${translations[currentLanguage].transactionHistoryTitle}</h2>`;
            // Здесь можно добавить существующие транзакции, если они есть
            const transactions = JSON.parse(localStorage.getItem('transactions')) || []; // Получаем список транзакций из localStorage
            transactions.forEach(transaction => {
                transactionHistorySection.innerHTML += `
                    <div class="transaction-item">
                        <strong>${transaction.date}</strong>: ${transaction.description} - ${transaction.amount} руб.
                    </div>
                `;
            });

            // Кнопка для загрузки отчета
            const downloadReportSection = document.getElementById('downloadReport');
            downloadReportSection.innerHTML = `
                <button class="download-report" onclick="downloadReport()">${translations[currentLanguage].downloadReportButton}</button>
            `;
        }

        function toggleFAQ(element) {
            const answer = element.nextElementSibling;
            answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
        }

        function toggleNews(element) {
            const content = element.nextElementSibling;
            content.style.display = content.style.display === 'block' ? 'none' : 'block';
        }

        function changeLanguage(lang) {
            currentLanguage = lang;
            updateLanguage();
        }

        function showRegistrationForm() {
            const registrationForm = document.createElement('div');
            registrationForm.className = 'registration-form';
            registrationForm.innerHTML = 
                `<h2><strong>${translations[currentLanguage].registration}</strong></h2>
                <input type="text" id="name" placeholder="${translations[currentLanguage].namePlaceholder}" required>
                <input type="email" id="email" placeholder="${translations[currentLanguage].emailPlaceholder}" required>
                <input type="password" id="password" placeholder="${translations[currentLanguage].passwordPlaceholder}" required>
                <button onclick="register()"><strong>${translations[currentLanguage].registerButton}</strong></button>`;
            document.body.appendChild(registrationForm);
        }

        function calculateLoan() {
            const loanAmount = parseFloat(document.getElementById('loanAmount').value);
            const interestRate = parseFloat(document.getElementById('interestRate').value) / 100 / 12; // месячная ставка
            const loanTerm = parseInt(document.getElementById('loanTerm').value) * 12; // месяцы

            const monthlyPayment = (loanAmount * interestRate) / (1 - Math.pow(1 + interestRate, -loanTerm));
            document.getElementById('calculatorResult').innerText = `${translations[currentLanguage].monthlyPaymentLabel} ${monthlyPayment.toFixed(2)} руб.`;
        }

        function addOffer() {
            const offerName = document.getElementById('offerName').value.trim();
            const offerDescription = document.getElementById('offerDescription').value.trim();

            if (offerName && offerDescription) {
                const offersSection = document.getElementById('offers');
                const newOffer = document.createElement('div');
                newOffer.className = 'offer-item';
                newOffer.innerHTML = `<h4>${offerName}</h4><p>${offerDescription}</p>`;
                offersSection.appendChild(newOffer);

                // Очистка полей ввода
                document.getElementById('offerName').value = '';
                document.getElementById('offerDescription').value = '';
            } else {
                alert("Пожалуйста, заполните все поля.");
            }
        }

        function sendFeedback() {
            const feedbackMessage = document.getElementById('feedbackMessage').value.trim();

            if (feedbackMessage) {
                alert("Ваше сообщение отправлено! Спасибо за обратную связь.");
                document.getElementById('feedbackMessage').value = ''; // Очистка поля ввода
            } else {
                alert("Пожалуйста, введите ваше сообщение.");
            }
        }

        function downloadReport() {
            alert("Отчет будет загружен в формате PDF."); // Здесь можно добавить логику для загрузки отчета
        }

        // Остальные функции остаются без изменений, но добавьте обновление текста в зависимости от языка
        // Например, в функции showProfile, toggleSection и т.д.
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
    <select onchange="changeLanguage(this.value)">
        <option value="ru">Русский</option>
        <option value="en">English</option>
        <!-- Добавьте другие языки по мере необходимости -->
    </select>
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
        <h2><strong>${translations[currentLanguage].servicesTitle}</strong></h2>
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <ul>
            ${translations[currentLanguage].servicesList.map(service => `<li><strong>${service}</strong></li>`).join('')}
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
        <h2><strong>${translations[currentLanguage].contactInfoTitle}</strong></h2>
        <div class="yellow-line"></div> <!-- Желтая полоска под заголовком -->
        <p><strong>Email:</strong> <a href="mailto:${translations[currentLanguage].contactEmail}">${translations[currentLanguage].contactEmail}</a></p> <!-- Изменена электронная почта -->
        <p><strong>Discord:</strong> <a href="https://discord.gg/q8kRuKebKH" target="_blank">${translations[currentLanguage].discord}</a></p> <!-- Добавлена ссылка на Discord -->
        <p><strong>Telegram:</strong> <a href="https://t.me/+NE8aj5oiHJhjYjgy" target="_blank">${translations[currentLanguage].telegram}</a></p> <!-- Добавлена ссылка на Telegram -->
        <p><strong>YouTube:</strong> <a href="https://www.youtube.com/channel/UCnFbE5v1nzlonhsk9wX16Yw" target="_blank">${translations[currentLanguage].youtube}</a></p> <!-- Добавлена ссылка на YouTube -->
        <p><strong>Token:</strong> <a href="#" target="_blank">${translations[currentLanguage].token}</a></p>
    </div>

    <div id="faq" class="faq-section"></div> <!-- Секция FAQ -->
    <div id="reviews" class="reviews-section"></div> <!-- Секция отзывов -->
    <div id="news" class="news-section"></div> <!-- Секция новостей -->
    <div id="partners" class="partners-section"></div> <!--
    
