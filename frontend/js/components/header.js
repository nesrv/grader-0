// Создание шапки сайта
function createHeader() {
  const header = document.getElementById('header');
  header.innerHTML = `
    <div class="container">
      <div class="logo">
        <img src="/images/logo_grader.png" alt="Грейдер">
        <a href="/">Грейдер</a>
      </div>
      <nav>
        <ul>
          <li><a href="/">Главная</a></li>
          <li><a href="/learning">Обучение</a></li>
          <li><a href="/profile">Профиль</a></li>
        </ul>
      </nav>
    </div>
  `;
}

// Инициализация шапки
document.addEventListener('DOMContentLoaded', createHeader);