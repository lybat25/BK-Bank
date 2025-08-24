<script>
    // Глобальные переменные
    let users = JSON.parse(localStorage.getItem('bankUsers')) || {};
    let currentUser = null;
    let resetTokens = JSON.parse(localStorage.getItem('resetTokens')) || {};

    // Функция для удаления всех аккаунтов
    function deleteAllAccounts() {
        if (confirm("Вы уверены, что хотите удалить ВСЕ аккаунты? Это действие нельзя отменить.")) {
            localStorage.removeItem('bankUsers');
            localStorage.removeItem('currentSession');
            localStorage.removeItem('resetTokens');
            users = {};
            resetTokens = {};
            currentUser = null;
            
            alert("Все аккаунты были успешно удалены.");
            
            // Перезагружаем страницу для применения изменений
            location.reload();
        }
    }

    // Добавляем кнопку удаления аккаунтов в интерфейс (только для администратора)
    function addAdminControls() {
        // Проверяем, является ли текущий пользователь администратором
        if (currentUser === 'admin') {
            const adminButton = document.createElement('button');
            adminButton.textContent = 'Удалить все аккаунты';
            adminButton.style.background = '#ff4444';
            adminButton.style.color = 'white';
            adminButton.style.padding = '10px';
            adminButton.style.margin = '10px';
            adminButton.style.borderRadius = '4px';
            adminButton.style.border = 'none';
            adminButton.style.cursor = 'pointer';
            adminButton.onclick = deleteAllAccounts;
            
            // Добавляем кнопку в заголовок
            document.querySelector('header nav').appendChild(adminButton);
        }
    }

    // Инициализация при загрузке страницы
    window.onload = function() {
        // Проверяем, есть ли активная сессия
        const session = localStorage.getItem('currentSession');
        if (session) {
            const sessionData = JSON.parse(session);
            // Проверяем, не истекла ли сессия (24 часа)
            if (Date.now() - sessionData.timestamp < 24 * 60 * 60 * 1000) {
                currentUser = sessionData.username;
                showMainContent();
                showWelcomeMessage(users[currentUser].name);
                addAdminControls(); // Добавляем админ-контролы если пользователь вошел как admin
                return;
            } else {
                // Удаляем просроченную сессию
                localStorage.removeItem('currentSession');
            }
        }
        
        // Если нет активной сессии, показываем форму входа
        showLoginForm();
    };

    // ... остальной код без изменений ...
</script>
