// Создание карточки грейда
function createGradeCard(grade) {
  const card = document.createElement('div');
  card.className = 'grade-card';
  card.dataset.id = grade.grade_id;
  
  // Преобразуем уровень грейда для отображения
  const levelDisplay = {
    'intern': 'Стажер',
    'junior': 'Джуниор',
    'junior+': 'Джуниор+',
    'middle': 'Мидл',
    'senior': 'Синьор'
  };
  
  // Получаем название уровня
  let levelName = grade.level_name;
  if (typeof levelName === 'object' && levelName !== null) {
    levelName = levelName.name || levelName;
  }
  
  card.innerHTML = `
    <div class="grade-header">
      <h4>${levelDisplay[levelName] || levelName}</h4>
    </div>
    <div class="grade-description">
      <p>${grade.description}</p>
    </div>
  `;
  
  return card;
}