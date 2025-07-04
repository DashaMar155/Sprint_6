import allure
from pages.base_page import BasePage
import locators.main_page_locators as locators
from urls import main_page_url as url


class MainPage(BasePage):
    @allure.step('Кликаем на вопрос {num}')
    def click_to_question(self, num):
        final_question_locator = self.format_locator(locators.question_locator, num)
        self.click_on_element(final_question_locator)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, num):
        final_answer_locator = self.format_locator(locators.answer_locator, num)
        return self.get_text_from_element(final_answer_locator)

    @allure.step("Прокручиваем страницу до последнего вопроса и ждём, пока он появится")
    def scroll_to_down(self):
        self.scroll_down()
        self.wait_for_element(locators.scroll_locator)

    @allure.step("Получаем текст вопроса (проверка, что мы на главной)")
    def get_text_from_last_question(self):
        self.scroll_down()
        return self.get_text_from_element(locators.scroll_locator)

    # статический метод для форматирования локаторов
    @staticmethod
    def format_locator(locator, num):
        by, locator_template = locator
        return by, locator_template.format(num)
