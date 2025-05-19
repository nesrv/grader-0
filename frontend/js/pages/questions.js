document.addEventListener('DOMContentLoaded', async () => {
    // Получаем параметры из URL
    const urlParams = new URLSearchParams(window.location.search);
    const topicId = urlParams.get('topic_id');
    const moduleId = urlParams.get('module_id');
    const gradeId = urlParams.get('grade_id');
    const professionId = urlParams.get('profession_id');
    
    if (!topicId) {
        showError('Не указан ID темы');
        return;
    }

    // Устанавливаем хлебные крошки
    setupBreadcrumbs(professionId, gradeId, moduleId);
    
    try {
        // Загружаем информацию о теме, модуле и грейде
        const topic = await fetchTopic(topicId);
        document.getElementById('topic-title').textContent = topic.title;
        document.getElementById('topic-name').textContent = topic.title;
        document.getElementById('page-title').textContent = `Теоретические вопросы: ${topic.title}`;
        
        // Загружаем информацию о модуле
        if (moduleId) {
            const module = await fetchModule(moduleId);
            document.getElementById('module-name').textContent = module.title;
        }
        
        // Загружаем информацию о грейде
        if (gradeId) {
            const grade = await fetchGrade(gradeId);
            document.getElementById('grade-name').textContent = grade.level_name;
        }
        
        // Загружаем теоретические вопросы для темы
        const theories = await fetchTheories(topicId);
        renderTheories(theories);
        
        // Устанавливаем прогресс
        updateProgress(theories);
        
    } catch (error) {
        console.error('Ошибка при загрузке данных:', error);
        showError('Не удалось загрузить данные. Пожалуйста, попробуйте позже.');
    }
    
    // Настраиваем кнопки навигации
    setupNavigationButtons(moduleId, topicId);
});

async function fetchTopic(topicId) {
    const response = await fetch(`/api/v1/topics/topics/${topicId}`);
    if (!response.ok) {
        throw new Error(`Ошибка HTTP: ${response.status}`);
    }
    return await response.json();
}

async function fetchModule(moduleId) {
    const response = await fetch(`/api/v1/modules/${moduleId}`);
    if (!response.ok) {
        throw new Error(`Ошибка HTTP: ${response.status}`);
    }
    return await response.json();
}

async function fetchGrade(gradeId) {
    const response = await fetch(`/api/v1/grades/${gradeId}`);
    if (!response.ok) {
        throw new Error(`Ошибка HTTP: ${response.status}`);
    }
    return await response.json();
}

async function fetchTheories(topicId) {
    const response = await fetch(`/api/v1/topics/topics/${topicId}/theories/`);
    if (!response.ok) {
        throw new Error(`Ошибка HTTP: ${response.status}`);
    }
    return await response.json();
}

function renderTheories(theories) {
    const container = document.getElementById('theories-container');
    container.innerHTML = '';
    
    if (theories.length === 0) {
        container.innerHTML = '<div class="no-data">Для этой темы пока нет теоретических вопросов</div>';
        return;
    }
    
    theories.forEach(theory => {
        const theoryCard = document.createElement('div');
        theoryCard.className = 'theory-card';
        
        const title = document.createElement('h3');
        title.className = 'theory-title';
        title.textContent = theory.title;
        
        const description = document.createElement('div');
        description.className = 'theory-description';
        description.textContent = theory.description || '';
        
        theoryCard.appendChild(title);
        theoryCard.appendChild(description);
        
        if (theory.code_question) {
            const codeBlock = document.createElement('pre');
            codeBlock.className = 'code-block';
            
            const codeElement = document.createElement('code');
            codeElement.className = 'language-python';
            codeElement.textContent = theory.code_question;
            
            codeBlock.appendChild(codeElement);
            theoryCard.appendChild(codeBlock);
        }
        
        container.appendChild(theoryCard);
    });
    
    // Подсветка синтаксиса после добавления всех элементов в DOM
    if (window.Prism) {
        Prism.highlightAll();
    }
}

function updateProgress(theories) {
    // Фейковый прогресс для демонстрации
    const progressPercent = theories.length > 0 ? Math.floor(Math.random() * 100) : 0;
    document.getElementById('progress-bar').style.width = `${progressPercent}%`;
    document.getElementById('progress-percent').textContent = `${progressPercent}%`;
}

function setupBreadcrumbs(professionId, gradeId, moduleId) {
    if (professionId) {
        document.getElementById('profession-link').href = `profession.html?id=${professionId}`;
    }
    
    if (gradeId) {
        document.getElementById('grade-link').href = `grade.html?id=${gradeId}&profession_id=${professionId}`;
    }
    
    if (moduleId) {
        document.getElementById('module-link').href = `learning.html?id=${moduleId}&grade_id=${gradeId}&profession_id=${professionId}`;
    }
}

function setupNavigationButtons(moduleId, topicId) {
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    
    prevBtn.addEventListener('click', () => {
        // Возвращаемся на страницу с темами
        window.location.href = `learning.html?id=${moduleId}`;
    });
    
    nextBtn.addEventListener('click', () => {
        // Здесь можно добавить переход к следующему типу вопросов или заданий
        alert('Переход к следующему разделу (в разработке)');
    });
}

function showError(message) {
    const container = document.getElementById('theories-container');
    container.innerHTML = `<div class="error-message">${message}</div>`;
}