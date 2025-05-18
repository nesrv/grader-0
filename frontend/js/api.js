// Функции для работы с API
const API_URL = 'http://localhost:8000/api/v1';

// Получение данных для главной страницы
async function getHomePageData() {
  try {
    const response = await fetch(`${API_URL}/home`);
    return await response.json();
  } catch (error) {
    console.error('Ошибка при получении данных для главной страницы:', error);
    return { professions: [] };
  }
}

// Получение списка профессий
async function getProfessions() {
  try {
    const response = await fetch(`${API_URL}/professions`);
    return await response.json();
  } catch (error) {
    console.error('Ошибка при получении профессий:', error);
    return [];
  }
}

// Получение профессии по ID
async function getProfessionById(professionId) {
  try {
    const response = await fetch(`${API_URL}/professions/${professionId}`);
    return await response.json();
  } catch (error) {
    console.error(`Ошибка при получении профессии ${professionId}:`, error);
    return null;
  }
}

// Получение грейдов для профессии
async function getGradesByProfession(professionId) {
  try {
    const response = await fetch(`${API_URL}/grades/profession/${professionId}`);
    return await response.json();
  } catch (error) {
    console.error(`Ошибка при получении грейдов для профессии ${professionId}:`, error);
    return [];
  }
}

// Получение грейда по ID
async function getGradeById(gradeId) {
  try {
    const response = await fetch(`${API_URL}/grades/${gradeId}`);
    return await response.json();
  } catch (error) {
    console.error(`Ошибка при получении грейда ${gradeId}:`, error);
    return null;
  }
}

// Получение модулей для грейда
async function getModulesByGrade(gradeId) {
  try {
    const response = await fetch(`${API_URL}/modules/grade/${gradeId}/modules`);
    return await response.json();
  } catch (error) {
    console.error(`Ошибка при получении модулей для грейда ${gradeId}:`, error);
    return [];
  }
}