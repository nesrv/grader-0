// Логика для страницы профессии
async function initProfessionPage() {
  const gradesContainer = document.getElementById('grades-container');
  const professionTitle = document.getElementById('profession-title');
  const professionDescription = document.getElementById('profession-description');
  
  gradesContainer.innerHTML = '<div class="loading">Загрузка данных...</div>';
  
  // Получаем ID профессии из URL
  const urlParams = new URLSearchParams(window.location.search);
  const professionId = urlParams.get('id');
  
  if (!professionId) {
    gradesContainer.innerHTML = '<div class="error">Не указан ID профессии</div>';
    return;
  }
  
  // Функция для создания рейтинга звездами
  function createRating(rating) {
    const maxRating = 5;
    let starsHtml = '';
    
    for (let i = 1; i <= maxRating; i++) {
      if (i <= rating) {
        starsHtml += '<span class="star filled">★</span>';
      } else {
        starsHtml += '<span class="star">★</span>';
      }
    }
    
    return `<div class="rating">${starsHtml}</div>`;
  }
  
  try {
    // Получаем данные о профессии
    const profession = await getProfessionById(professionId);
    
    if (!profession) {
      gradesContainer.innerHTML = '<div class="error">Профессия не найдена</div>';
      return;
    }
    
    // Обновляем заголовок и описание
    professionTitle.textContent = profession.name;
    professionDescription.textContent = profession.description;
    
    // Получаем грейды для профессии
    const grades = await getGradesByProfession(professionId);
    
    // Очищаем контейнер
    gradesContainer.innerHTML = '';
    
    if (grades.length === 0) {
      gradesContainer.innerHTML = '<div class="error">Для данной профессии нет доступных грейдов</div>';
      return;
    }
    
    // Отображаем грейды
    grades.forEach(grade => {
      // Генерируем случайный рейтинг от 1 до 5
      const randomRating = Math.floor(Math.random() * 5) + 1;
      
      const gradeCard = document.createElement('div');
      gradeCard.className = 'profession-card';
      gradeCard.dataset.id = grade.grade_id;
      
      gradeCard.innerHTML = `
        <div class="profession-info">
          <h3>${grade.level_name}</h3>
          <p>${grade.description || 'Описание отсутствует'}</p>
          ${createRating(randomRating)}
        </div>
      `;
      
      // Добавляем обработчик клика для перехода на страницу грейда
      gradeCard.addEventListener('click', function() {
        console.log(`Переход на grade.html?id=${grade.grade_id}`);
        window.location.href = `grade.html?id=${grade.grade_id}`;
      });
      
      gradesContainer.appendChild(gradeCard);
    });
    
    // Добавляем обработчики клика для всех карточек грейдов
    document.querySelectorAll('.profession-card').forEach(card => {
      card.addEventListener('click', function() {
        const gradeId = this.dataset.id;
        console.log(`Клик по карточке грейда ${gradeId}`);
        window.location.href = `grade.html?id=${gradeId}`;
      });
    });
    
  } catch (error) {
    console.error('Ошибка при инициализации страницы профессии:', error);
    gradesContainer.innerHTML = '<div class="error">Произошла ошибка при загрузке данных</div>';
  }
}

// Инициализация страницы при загрузке
document.addEventListener('DOMContentLoaded', initProfessionPage);