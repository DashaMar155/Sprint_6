from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    # Ожидаем появления элемента и возвращаем его
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # Ожидаем кликабельности элемента и кликаем
    def click_on_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # Получаем текст из элемента
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Вводим текст в поле (с предварительной очисткой)
    def fill_text_to_field(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    # Вводим текст и нажимаем ENTER
    def fill_the_field_and_click_enter(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    # Открываем указанный URL
    def go_to_url(self, url):
        self.driver.get(url)

    # Скроллим страницу до элемента
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    # Скроллим в конец страницы
    def scroll_down(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # Переключаемся на вкладку по индексу
    def switch_to_tab(self, index: int):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: len(d.window_handles) > abs(index) if index < 0 else index < len(d.window_handles)
        )
        self.driver.switch_to.window(self.driver.window_handles[index])

    # Ожидаем смены URL
    def wait_until_url_changes_from(self, url: str):
        WebDriverWait(self.driver, self.timeout).until(lambda d: d.current_url != url)

    # Получаем текущий URL
    def get_current_url(self):
        return self.driver.current_url

    # Универсальное ожидание видимости элемента (по смыслу, а не по названию)
    def wait_for_element(self, locator):
        return self.find_element_with_wait(locator)

    # Проверка, отображается ли элемент на странице
    def is_element_visible(self, locator):
        try:
            self.find_element_with_wait(locator)
            return True
        except:
            return False

