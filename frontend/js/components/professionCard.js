// Создание карточки профессии
function createProfessionCard(profession) {
  const card = document.createElement('div');
  card.className = 'profession-card';
  card.dataset.id = profession.profession_id;
  
  card.innerHTML = `
    <div class="profession-image">
      <img src="${profession.image_path || 'assets/images/default-profession.jpg'}" alt="${profession.name}">
    </div>
    <div class="profession-info">
      <h3>${profession.name}</h3>
      <p>${profession.description}</p>
      <button class="show-grades-btn">Показать грейды</button>
    </div>
    <div class="grades-container" id="grades-${profession.profession_id}" style="display: none;"></div>
  `;
  
  // Добавляем обработчик для кнопки "Показать грейды"
  const showGradesBtn = card.querySelector('.show-grades-btn');
  showGradesBtn.addEventListener('click', async () => {
    const gradesContainer = card.querySelector(`.grades-container`);
    
    // Если грейды уже загружены, просто переключаем видимость
    if (gradesContainer.children.length > 0) {
      gradesContainer.style.display = gradesContainer.style.display === 'none' ? 'block' : 'none';
      showGradesBtn.textContent = gradesContainer.style.display === 'none' ? 'Показать грейды' : 'Скрыть грейды';
      return;
    }
    
    // Загружаем грейды для профессии
    const grades = await getGradesByProfession(profession.profession_id);
    
    // Отображаем грейды
    grades.forEach(grade => {
      const gradeCard = createGradeCard(grade);
      gradesContainer.appendChild(gradeCard);
    });
    
    // Показываем контейнер с грейдами
    gradesContainer.style.display = 'block';
    showGradesBtn.textContent = 'Скрыть грейды';
  });
  
  return card;
}