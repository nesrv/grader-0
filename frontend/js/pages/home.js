// Логика для главной страницы
async function initHomePage() {
  const professionsContainer = document.getElementById('professions-container');
  professionsContainer.innerHTML = '<div class="loading">Загрузка данных...</div>';
  
  // Маппинг профессий на SVG иконки
  const professionIcons = {
    1: 'assets/images/professions/backend_developer.svg',
    2: 'assets/images/professions/data_scientist.svg',
    3: 'assets/images/professions/ml_engineer.svg',
    4: 'assets/images/professions/devops_engineer.svg',
    5: 'assets/images/professions/qa_automation.svg',
    6: 'assets/images/professions/game_dev.svg',
    7: 'assets/images/professions/iot_developer.svg'
  };
  
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
    // Получаем данные для главной страницы с API
    let professions = [];
    
    try {
      const homeData = await getHomePageData();
      if (homeData && homeData.professions && homeData.professions.length > 0) {
        professions = homeData.professions.map(item => item.profession);
      }
    } catch (homeError) {
      console.warn('Не удалось получить данные через /home API:', homeError);
    }
    
    // Если данные не получены через /home, используем запросы к отдельным эндпоинтам
    if (professions.length === 0) {
      try {
        professions = await getProfessions();
      } catch (profError) {
        console.error('Не удалось получить данные о профессиях:', profError);
      }
    }
    
    // Очищаем контейнер
    professionsContainer.innerHTML = '';
    
    if (professions.length === 0) {
      professionsContainer.innerHTML = '<div class="error">Не удалось загрузить данные о профессиях</div>';
      return;
    }
    
    // Отображаем профессии
    professions.forEach(profession => {
      // Генерируем случайный рейтинг от 1 до 5
      const randomRating = Math.floor(Math.random() * 5) + 1;
      
      // Создаем карточку профессии как ссылку
      const card = document.createElement('a');
      card.className = 'profession-card';
      card.href = `profession.html?id=${profession.profession_id}`;
      card.dataset.id = profession.profession_id;
      
      const imagePath = professionIcons[profession.profession_id] || 'assets/images/default-profession.jpg';
      
      card.innerHTML = `
        <div class="profession-image">
          <img src="${imagePath}" alt="${profession.name}" class="profession-svg">
        </div>
        <div class="profession-info">
          <h3>${profession.name}</h3>
          <p>${profession.description || 'Описание отсутствует'}</p>
          ${createRating(randomRating)}
        </div>
      `;
      
      professionsContainer.appendChild(card);
    });
    
  } catch (error) {
    console.error('Ошибка при инициализации главной страницы:', error);
    professionsContainer.innerHTML = '<div class="error">Произошла ошибка при загрузке данных</div>';
  }
}

// Инициализация страницы при загрузке
document.addEventListener('DOMContentLoaded', initHomePage);