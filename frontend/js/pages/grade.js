// Логика для страницы грейда
async function initGradePage() {
  console.log('Инициализация страницы грейда');
  
  const modulesContainer = document.getElementById('modules-container');
  const gradeTitle = document.getElementById('grade-title');
  const gradeDescription = document.getElementById('grade-description');
  
  modulesContainer.innerHTML = '<div class="loading">Загрузка данных...</div>';
  
  // Получаем ID грейда из URL
  const urlParams = new URLSearchParams(window.location.search);
  const gradeId = urlParams.get('id');
  
  console.log('ID грейда из URL:', gradeId);
  
  if (!gradeId) {
    modulesContainer.innerHTML = '<div class="error">Не указан ID грейда</div>';
    return;
  }
  
  try {
    // Получаем данные о грейде
    console.log('Запрос данных о грейде:', gradeId);
    const grade = await getGradeById(gradeId);
    console.log('Получены данные о грейде:', grade);
    
    if (!grade) {
      modulesContainer.innerHTML = '<div class="error">Грейд не найден</div>';
      return;
    }
    
    // Обновляем заголовок и описание
    gradeTitle.textContent = `Модули грейда "${grade.level_name}"`;
    gradeDescription.textContent = grade.description || '';
    
    // Получаем модули для грейда
    console.log('Запрос модулей для грейда:', gradeId);
    const modules = await getModulesByGrade(gradeId);
    console.log('Получены модули:', modules);
    
    // Очищаем контейнер
    modulesContainer.innerHTML = '';
    
    if (modules.length === 0) {
      modulesContainer.innerHTML = '<div class="error">Для данного грейда нет доступных модулей</div>';
      return;
    }
    
    // Создаем контейнер для пути модулей
    const modulesPath = document.createElement('div');
    modulesPath.className = 'modules-path';
    modulesContainer.appendChild(modulesPath);
    
    // Отображаем модули
    modules.forEach((module, index) => {
      // Определяем статус модуля (для демонстрации)
      let status = 'locked';
      if (index === 0) status = 'current'; // Первый модуль активный
      if (index === 1) status = 'locked';
      
      const moduleCard = document.createElement('div');
      moduleCard.className = `module-card ${status}`;
      moduleCard.dataset.id = module.module_id;
      
      // Иконка для модуля
      let iconContent = '🔒'; // Замок для заблокированных модулей
      if (status === 'completed') iconContent = '✓'; // Галочка для завершенных
      if (status === 'current') iconContent = (index + 1).toString(); // Номер для текущего
      
      // Текст статуса
      let statusText = 'Заблокировано';
      if (status === 'completed') statusText = 'Завершено';
      if (status === 'current') statusText = 'В процессе';
      
      moduleCard.innerHTML = `
        <div class="module-icon ${status}">${iconContent}</div>
        <div class="module-content">
          <div class="module-title">${module.title}</div>
          <div class="module-description">${module.description || 'Описание отсутствует'}</div>
          <div class="module-status ${status}">${statusText}</div>
        </div>
        <div class="module-footer">
          <div class="module-order">${module.order}</div>
        </div>
      `;
      
      // Добавляем обработчик клика только для доступных модулей
      if (status !== 'locked') {
        moduleCard.addEventListener('click', () => {
          if (status === 'current') {
            // Переход на страницу обучения для текущего модуля
            window.location.href = `learning.html?module_id=${module.module_id}`;
          } else {
            // Для завершенных модулей просто показываем сообщение
            alert(`Модуль "${module.title}" уже завершен`);
          }
        });
      }
      
      modulesPath.appendChild(moduleCard);
    });
    
  } catch (error) {
    console.error('Ошибка при инициализации страницы грейда:', error);
    modulesContainer.innerHTML = '<div class="error">Произошла ошибка при загрузке данных</div>';
  }
}

// Инициализация страницы при загрузке
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM загружен, запуск initGradePage');
  initGradePage();
});