// Общие функции для всех страниц

// Функция для отображения уведомлений
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Показываем уведомление
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    // Скрываем и удаляем через 3 секунды
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Функция для логирования ошибок
function logError(error, context = '') {
    console.error(`Ошибка ${context ? 'в ' + context : ''}:`, error);
    // Здесь можно добавить отправку ошибок на сервер для анализа
}

// Функция для получения параметров из URL
function getUrlParams() {
    return new URLSearchParams(window.location.search);
}

// Обработчик ошибок для fetch запросов
async function handleFetchResponse(response) {
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
    }
    return await response.json();
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    console.log('Страница загружена');
    
    // Добавляем обработчик для всех ссылок с классом 'debug-link'
    document.querySelectorAll('.debug-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Debug link clicked:', this.href);
            showNotification('Отладочная ссылка: ' + this.href, 'info');
        });
    });
});