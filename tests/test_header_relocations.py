import allure
from pages.header import Header
from pages.main_page import MainPage


class TestHeaderRelocations:
    @allure.title("Переадресация при клике на лого Самоката")
    @allure.description("Проверяем, что если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»")
    def test_click_on_samokat_logo_redirect_on_main(self, driver_order_page):
        header = Header(driver_order_page)
        header.click_on_samokat_logo()
        redirect_page = MainPage(driver_order_page)
        control_text = redirect_page.get_text_from_last_question()
        # переиспользуем уже созданный для скролла страницы локатор
        # в тексте вопроса по этому локатору опечатка, "жизу" вместо "живу", потенциально текст будет изменяться
        # поэтому не будем привязываться к полному совпадению, проверим включение части текста,
        # для проверки правильной страницы этого достаточно
        assert "МКАД" in control_text

    @allure.title("Переадресация в новой вкладке при клике на лого Яндекса")
    @allure.description("Проверяем, что если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена")
    def test_click_on_yandex_logo_redirect_on_dzen_in_new_page(self, driver_main_page):
        header = Header(driver_main_page)
        header.click_on_yandex_logo()
        header.go_to_the_last_open_page()

        assert header.check_is_location_on_yandex_page()