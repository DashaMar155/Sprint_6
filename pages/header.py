import allure
import logging
from pages.base_page import BasePage
from locators.header_locators import logo_yandex_locator, logo_samokat_locator

logger = logging.getLogger(__name__)


class Header(BasePage):
    @allure.step("Кликаем на логотип Яндекса")
    def click_on_yandex_logo(self):
        self.click(logo_yandex_locator)

    @allure.step("Кликаем на логотип Самоката")
    def click_on_samokat_logo(self):
        self.click(logo_samokat_locator)

    @allure.step("Переходим на последнюю открытую вкладку и ждём загрузки")
    def go_to_the_last_open_page(self):
        self.switch_to_tab(-1)
        self.wait_until_url_changes_from("about:blank")

    @allure.step("Проверяем, что URL ведёт на Яндекс или Дзен")
    def check_is_location_on_yandex_page(self):
        current_url = self.get_current_url()
        logger.info(f"Текущий URL: {current_url}")
        return any(sub in current_url for sub in ("yandex.ru", "dzen.ru", "ya.ru"))
