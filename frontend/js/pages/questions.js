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
        theoryCard.dataset.id = theory.theory_id;
        
        // Заголовок
        const title = document.createElement('h3');
        title.className = 'theory-title';
        title.textContent = theory.title;
        theoryCard.appendChild(title);
        
        // Описание
        if (theory.description) {
            const description = document.createElement('div');
            description.className = 'theory-description';
            description.textContent = theory.description;
            theoryCard.appendChild(description);
        }
        
        // Блок с кодом
        if (theory.code_question) {
            const codeBlock = document.createElement('pre');
            codeBlock.className = 'code-block';
            
            const codeElement = document.createElement('code');
            codeElement.className = 'language-python';
            // Экранируем HTML-символы для корректного отображения
            codeElement.textContent = theory.code_question;
            
            codeBlock.appendChild(codeElement);
            theoryCard.appendChild(codeBlock);
            
            // Применяем подсветку синтаксиса к этому конкретному блоку
            if (window.Prism) {
                Prism.highlightElement(codeElement);
            }
        }
        
        // Текстовый вопрос
        if (theory.text_question) {
            const textQuestion = document.createElement('div');
            textQuestion.className = 'text-question';
            textQuestion.textContent = theory.text_question;
            theoryCard.appendChild(textQuestion);
            
            // Варианты ответов
            if (theory.variants && Object.keys(theory.variants).length > 0) {
                const variantsContainer = document.createElement('div');
                variantsContainer.className = 'variants-container';
                
                // Создаем элементы для каждого варианта
                Object.entries(theory.variants).forEach(([key, value]) => {
                    const variantItem = document.createElement('div');
                    variantItem.className = 'variant-item';
                    variantItem.dataset.key = key;
                    
                    const variantKey = document.createElement('div');
                    variantKey.className = 'variant-key';
                    variantKey.textContent = key;
                    
                    const variantValue = document.createElement('div');
                    variantValue.className = 'variant-value';
                    
                    // Проверяем тип значения
                    if (typeof value === 'object' && value !== null) {
                        variantValue.textContent = JSON.stringify(value);
                    } else {
                        variantValue.textContent = value;
                    }
                    
                    variantItem.appendChild(variantKey);
                    variantItem.appendChild(variantValue);
                    
                    // Добавляем обработчик клика для выбора варианта
                    variantItem.addEventListener('click', () => {
                        // Снимаем выделение со всех вариантов
                        variantsContainer.querySelectorAll('.variant-item').forEach(item => {
                            item.classList.remove('selected');
                        });
                        
                        // Выделяем выбранный вариант
                        variantItem.classList.add('selected');
                        
                        // Активируем кнопку проверки
                        checkButton.disabled = false;
                    });
                    
                    variantsContainer.appendChild(variantItem);
                });
                
                theoryCard.appendChild(variantsContainer);
                
                // Кнопка проверки ответа
                const checkButton = document.createElement('button');
                checkButton.className = 'check-answer-btn';
                checkButton.textContent = 'Проверить ответ';
                checkButton.disabled = true;
                
                checkButton.addEventListener('click', () => {
                    const selectedVariant = variantsContainer.querySelector('.variant-item.selected');
                    if (!selectedVariant) return;
                    
                    const selectedKey = selectedVariant.dataset.key;
                    const correctAnswers = theory.answer || [];
                    
                    // Создаем элемент для отображения результата
                    const resultMessage = document.createElement('div');
                    resultMessage.className = 'result-message';
                    
                    // Проверяем правильность ответа
                    if (correctAnswers.includes(selectedKey)) {
                        selectedVariant.classList.add('correct');
                        resultMessage.textContent = 'Правильно!';
                        resultMessage.classList.add('correct-message');
                    } else {
                        selectedVariant.classList.add('incorrect');
                        
                        // Показываем правильный ответ
                        correctAnswers.forEach(correctKey => {
                            const correctVariant = variantsContainer.querySelector(`.variant-item[data-key="${correctKey}"]`);
                            if (correctVariant) {
                                correctVariant.classList.add('correct');
                            }
                        });
                        
                        resultMessage.textContent = 'Неправильно. Попробуйте еще раз!';
                        resultMessage.classList.add('incorrect-message');
                    }
                    
                    // Добавляем сообщение после вариантов ответов
                    variantsContainer.appendChild(resultMessage);
                    
                    // Деактивируем кнопку после проверки
                    checkButton.disabled = true;
                });
                
                theoryCard.appendChild(checkButton);
            }
        }
        
        container.appendChild(theoryCard);
    });
    
    // Подсветка синтаксиса после добавления всех элементов в DOM
    setTimeout(() => {
        if (window.Prism) {
            Prism.highlightAll();
        }
    }, 100);
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