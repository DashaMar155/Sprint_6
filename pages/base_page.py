from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Ждем, пока элемент появится и возвращаем его
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    # Ждем, пока элемент станет кликабельным и нажимаем на него
    def click_on_element(self, locator):
        element = (WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)))
        element.click()

    # Получаем текст элемента и возвращаем его
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    # Заполняем поле текстом
    def fill_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Переходим по полученному url
    def go_to_url(self, url):
        self.driver.get(url)

    # Прокручиваем страницу до выбранного элемента и ждем пока все прогрузится
    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.find_element_with_wait(locator))
        self.find_element_with_wait(locator)

    # Прокручиваем страницу до конца
    def scroll_down(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # Вводим данные в поле и подтверждаем ввод кнопкой ENTER
    def fill_the_field_and_click_enter(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
