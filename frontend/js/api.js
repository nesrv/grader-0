// API-клиент для взаимодействия с бэкендом

const API_BASE_URL = '/api/v1';

// Функции для работы с главной страницей
async function getHomePageData() {
    try {
        const response = await fetch(`${API_BASE_URL}/home/`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Ошибка при получении данных для главной страницы:', error);
        throw error;
    }
}

// Функции для работы с профессиями
async function getProfessions() {
    try {
        const response = await fetch(`${API_BASE_URL}/professions/`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Ошибка при получении списка профессий:', error);
        throw error;
    }
}

async function fetchProfessions() {
    return getProfessions();
}

async function fetchProfession(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/professions/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Ошибка при получении профессии с ID ${id}:`, error);
        throw error;
    }
}

// Функции для работы с грейдами
async function fetchGrades(professionId) {
    try {
        const response = await fetch(`${API_BASE_URL}/grades/?profession_id=${professionId}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Ошибка при получении грейдов для профессии ${professionId}:`, error);
        throw error;
    }
}

async function fetchGrade(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/grades/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Ошибка при получении грейда с ID ${id}:`, error);
        throw error;
    }
}

// Функции для работы с модулями
async function fetchModules(gradeId) {
    try {
        const response = await fetch(`${API_BASE_URL}/modules/grade/${gradeId}/modules`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Ошибка при получении модулей для грейда ${gradeId}:`, error);
        throw error;
    }
}

async function fetchModule(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/modules/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Ошибка при получении модуля с ID ${id}:`, error);
        throw error;
    }
}

// Функции для работы с темами
async function fetchTopics(moduleId) {
    try {
        const response = await fetch(`${API_BASE_URL}/topics/topics/?module_id=${moduleId}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Ошибка при получении тем для модуля ${moduleId}:`, error);
        throw error;
    }
}

async function fetchTopic(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/topics/topics/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Ошибка при получении темы с ID ${id}:`, error);
        throw error;
    }
}

// Функции для работы с теоретическими вопросами
async function fetchTheories(topicId) {
    try {
        const response = await fetch(`${API_BASE_URL}/topics/topics/${topicId}/theories/`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Ошибка при получении теоретических вопросов для темы ${topicId}:`, error);
        throw error;
    }
}