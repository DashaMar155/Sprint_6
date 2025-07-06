from selenium.webdriver.common.by import By

# Локаторы главной страницы с заделом на форматирование
# для вопросов
question_locator = [By.ID, 'accordion__heading-{}']
# для ответов
answer_locator = [By.ID, 'accordion__panel-{}']

# По этому элементу проверяем, что страница прогрузилась после прокрутки
scroll_locator = (By.ID, 'accordion__heading-7')