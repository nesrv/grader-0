// Логика для главной страницы
async function initHomePage() {
  const professionsContainer = document.getElementById('professions-container');
  professionsContainer.innerHTML = '<div class="loading">Загрузка данных...</div>';
  
  // Маппинг профессий на SVG иконки
  const professionIcons = {
    1: '/professions/backend_developer.svg',
    2: '/professions/data_scientist.svg',
    3: '/professions/ml_engineer.svg',
    4: '/professions/devops_engineer.svg',
    5: '/professions/qa_automation.svg',
    6: '/professions/game_dev.svg',
    7: '/professions/iot_developer.svg'
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
    const homeData = await getHomePageData();
    
    // Очищаем контейнер
    professionsContainer.innerHTML = '';
    
    // Если данные получены успешно
    if (homeData && homeData.professions && homeData.professions.length > 0) {
      // Отображаем профессии с грейдами
      homeData.professions.forEach(item => {
        const profession = item.profession;
        
        // Генерируем случайный рейтинг от 1 до 5
        const randomRating = Math.floor(Math.random() * 5) + 1;
        
        // Создаем карточку профессии как ссылку
        const card = document.createElement('a');
        card.className = 'profession-card';
        card.href = `profession.html?id=${profession.profession_id}`;
        card.dataset.id = profession.profession_id;
        
        card.innerHTML = `
          <div class="profession-image">
            <img src="${professionIcons[profession.profession_id] || '/images/default-profession.jpg'}" alt="${profession.name}" class="profession-svg">
          </div>
          <div class="profession-info">
            <h3>${profession.name}</h3>
            <p>${profession.description}</p>
            ${createRating(randomRating)}
          </div>
        `;
        
        professionsContainer.appendChild(card);
      });
    } else {
      // Если данные не получены через /home, используем запросы к отдельным эндпоинтам
      const professions = await getProfessions();
      
      if (professions.length === 0) {
        professionsContainer.innerHTML = '<div class="error">Не удалось загрузить данные о профессиях</div>';
        return;
      }
      
      for (const profession of professions) {
        // Генерируем случайный рейтинг от 1 до 5
        const randomRating = Math.floor(Math.random() * 5) + 1;
        
        // Создаем карточку профессии как ссылку
        const card = document.createElement('a');
        card.className = 'profession-card';
        card.href = `profession.html?id=${profession.profession_id}`;
        card.dataset.id = profession.profession_id;
        
        card.innerHTML = `
          <div class="profession-image">
            <img src="${professionIcons[profession.profession_id] || '/images/default-profession.jpg'}" alt="${profession.name}" class="profession-svg">
          </div>
          <div class="profession-info">
            <h3>${profession.name}</h3>
            <p>${profession.description}</p>
            ${createRating(randomRating)}
          </div>
        `;
        
        professionsContainer.appendChild(card);
      }
    }
  } catch (error) {
    console.error('Ошибка при инициализации главной страницы:', error);
    professionsContainer.innerHTML = '<div class="error">Произошла ошибка при загрузке данных</div>';
  }
}

// Инициализация страницы при загрузке
document.addEventListener('DOMContentLoaded', initHomePage);