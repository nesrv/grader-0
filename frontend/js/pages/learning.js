// Логика для страницы обучения
async function initLearningPage() {
  console.log('Инициализация страницы обучения');
  
  const topicsContainer = document.getElementById('topics-container');
  const moduleTitle = document.getElementById('module-title');
  const moduleDescription = document.getElementById('module-description');
  const totalProgress = document.getElementById('total-progress');
  const progressFill = document.getElementById('progress-fill');
  const prevModuleBtn = document.getElementById('prev-module');
  const nextModuleBtn = document.getElementById('next-module');
  
  topicsContainer.innerHTML = '<div class="loading">Загрузка данных...</div>';
  
  // Получаем ID модуля из URL
  const urlParams = new URLSearchParams(window.location.search);
  const moduleId = urlParams.get('module_id') || urlParams.get('id');
  
  console.log('ID модуля из URL:', moduleId);
  
  // Получаем дополнительные параметры из URL
  const gradeId = urlParams.get('grade_id');
  const professionId = urlParams.get('profession_id');
  
  if (!moduleId) {
    topicsContainer.innerHTML = '<div class="error">Не указан ID модуля</div>';
    return;
  }
  
  try {
    // Здесь должен быть запрос к API для получения данных о модуле
    // Пока используем фейковые данные
    const module = {
      module_id: moduleId,
      title: "Основы Python",
      description: "Базовые концепции языка Python для начинающих разработчиков",
      topics: [
        {
          topic_id: 1,
          title: "Простые неизменяемые типы данных",
          description: "Изучение основных типов данных в Python: int, float, bool, str",
          progress: 100, // процент выполнения
          status: "completed" // completed, current, locked
        },
        {
          topic_id: 2,
          title: "Переменные и именование",
          description: "Правила создания и именования переменных в Python",
          progress: 75,
          status: "current"
        },
        {
          topic_id: 3,
          title: "Ссылочная модель в Python",
          description: "Функция id(), оператор is и понимание ссылочной модели",
          progress: 0,
          status: "locked"
        },
        {
          topic_id: 4,
          title: "Ввод/вывод данных",
          description: "Работа с функциями input() и print()",
          progress: 0,
          status: "locked"
        },
        {
          topic_id: 5,
          title: "Форматирование данных",
          description: "Методы форматирования строк: %, str.format(), f-strings",
          progress: 0,
          status: "locked"
        },
        {
          topic_id: 6,
          title: "Арифметические и логические операции",
          description: "Основные операторы для работы с числами и логическими значениями",
          progress: 0,
          status: "locked"
        }
      ]
    };
    
    // Обновляем заголовок и описание
    moduleTitle.textContent = module.title;
    moduleDescription.textContent = module.description;
    
    // Вычисляем общий прогресс
    const totalTopics = module.topics.length;
    const completedTopics = module.topics.filter(topic => topic.progress === 100).length;
    const inProgressTopics = module.topics.filter(topic => topic.progress > 0 && topic.progress < 100).length;
    
    const totalProgressPercent = Math.round((completedTopics + inProgressTopics * 0.5) / totalTopics * 100);
    
    totalProgress.textContent = `${totalProgressPercent}%`;
    progressFill.style.width = `${totalProgressPercent}%`;
    
    // Очищаем контейнер
    topicsContainer.innerHTML = '';
    
    // Отображаем темы
    module.topics.forEach(topic => {
      const topicCard = document.createElement('div');
      topicCard.className = `topic-card ${topic.status}`;
      topicCard.dataset.id = topic.topic_id;
      
      // Иконка статуса
      let statusIcon = '';
      if (topic.status === 'completed') statusIcon = '✓';
      if (topic.status === 'current') statusIcon = '→';
      
      topicCard.innerHTML = `
        ${statusIcon ? `<div class="topic-status ${topic.status}">${statusIcon}</div>` : ''}
        <div class="topic-title">${topic.title}</div>
        <div class="topic-description">${topic.description}</div>
        <div class="topic-progress">
          <div class="topic-progress-bar">
            <div class="topic-progress-fill" style="width: ${topic.progress}%"></div>
          </div>
          <div class="topic-percentage">${topic.progress}%</div>
        </div>
      `;
      
      // Добавляем обработчик клика только для доступных тем
      if (topic.status !== 'locked') {
        topicCard.addEventListener('click', () => {
          // Переход на страницу с теоретическими вопросами
          window.location.href = `questions.html?topic_id=${topic.topic_id}&module_id=${moduleId}${gradeId ? `&grade_id=${gradeId}` : ''}${professionId ? `&profession_id=${professionId}` : ''}`;
        });
      }
      
      topicsContainer.appendChild(topicCard);
    });
    
    // Настраиваем кнопки навигации
    prevModuleBtn.classList.add('disabled');
    prevModuleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      alert('Переход к предыдущему модулю');
    });
    
    nextModuleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      alert('Переход к следующему модулю');
    });
    
  } catch (error) {
    console.error('Ошибка при инициализации страницы обучения:', error);
    topicsContainer.innerHTML = '<div class="error">Произошла ошибка при загрузке данных</div>';
  }
}

// Инициализация страницы при загрузке
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM загружен, запуск initLearningPage');
  initLearningPage();
});