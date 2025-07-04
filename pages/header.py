import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.header_locators import logo_yandex_locator, logo_samokat_locator


class Header(BasePage):
    @allure.step("Кликаем на логотип Яндекса")
    def click_on_yandex_logo(self):
        # клик по <a href="...yandex.ru">
        self.click_on_element(logo_yandex_locator)

    @allure.step("Кликаем на логотип Самоката")
    def click_on_samokat_logo(self):
        self.click_on_element(logo_samokat_locator)

    @allure.step("Переходим на последнюю открытую вкладку и ждём загрузки")
    def go_to_the_last_open_page(self):
        # ждём, что вкладка появится
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        # переключаемся
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # ждём, что URL перестанет быть about:blank
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != "about:blank")

    @allure.step("Проверяем, что URL ведёт на Яндекс или Дзен")
    def check_is_location_on_yandex_page(self):
        current_url = self.driver.current_url
        print("🌐 Текущий URL:", current_url)
        return any(sub in current_url for sub in ("yandex.ru", "dzen.ru", "ya.ru"))
