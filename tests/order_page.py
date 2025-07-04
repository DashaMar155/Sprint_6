import allure
import pytest
import locators.order_page_locators as locators
import data
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title("Заказ самоката с параметризацией")
    @allure.description("Позитивный сценарий: проверка оформления заказа с двумя наборами данных. "
                        "Проверяются две кнопки «Заказать» на Главной странице.")
    @pytest.mark.parametrize('init_order_button, order_data', [
        [locators.init_order_button_top_on_main, data.order_from_ivan],
        [locators.init_order_button_down_on_main, data.order_from_galina]
    ])
    def test_create_order_with_valid_data_successful_message(self, driver_main_page, init_order_button, order_data):
        order_page = OrderPage(driver_main_page)
        order_page.open_order_page(init_order_button)
        order_page.fill_order_fields(order_data)
        order_page.click_on_next_button()
        order_page.fill_rent_info_fields(order_data)
        order_page.click_on_finish_order_button()
        order_page.confirm_order()
        order_page.check_change_modal_window()

        title_text = order_page.get_successful_create_order_title()
        assert 'Номер заказа' in title_text
