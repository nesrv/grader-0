// Создание подвала сайта
function createFooter() {
  const footer = document.getElementById('footer');
  footer.innerHTML = `
    <div class="container">
      <p>&copy; 2023 Грейдер. Все права защищены.</p>
    </div>
  `;
}

// Инициализация подвала
document.addEventListener('DOMContentLoaded', createFooter);