import allure
from pages.base_page import BasePage
from urls import main_page_url as url
from data import rent_info_time as options
import locators.order_page_locators as locators
import random

class OrderPage(BasePage):
    @allure.step('Открываем страницу заказа нажатием на верхнюю/нижнюю кнопку "Заказать"')
    def open_order_page(self,init_order_button):
        # прокрутили страницу до элемента
        self.scroll_to_element(init_order_button)
        # нажали на полученную кнопку инициации оформления заказа
        self.click_on_element(init_order_button)

    @allure.step('Заполняем данные')
    def fill_order_fields(self, data):
        self.fill_text_to_field(locators.name_field, data['name'])
        self.fill_text_to_field(locators.surname_field, data['surname'])
        self.fill_text_to_field(locators.address_field, data['address'])
        self.click_on_element(locators.metro_station_field)
        self.click_on_element(locators.metro_station_select)
        self.fill_text_to_field(locators.phone_field, data['phone'])


    @allure.step('Нажимаем кнопку "Далее"')
    def click_on_next_button(self):
        self.click_on_element(locators.next_button)

    @allure.step('Заполняем данные аренды')
    def fill_rent_info_fields(self, data):
        # так как у нас не стоит задача тестирования календаря, а логика выбора даты потенциально сложна,
        # возьмем дату с запасом по времени из набора тестовых данных, введем ее в поле и нажмем Enter
        self.fill_the_field_and_click_enter(locators.rent_info_data_field, data['rent_info_data'])

        # так как количество вариантов ограничено, целесообразно реализовать случайный выбор значения
        self.click_on_element(locators.rent_info_time_field)

        random_time_option_locator = self.format_rent_time_locator(locators.rent_info_time_options, random.choice(options))
        self.click_on_element(random_time_option_locator)

        # цвет тоже выберем случайным образом
        random_color_locator = random.choice([locators.rent_info_color_black, locators.rent_info_color_gray])
        self.click_on_element(random_color_locator)

        # поле с комментарием будет заполненным или пустым в зависимости от значения 'rent_info_comment' в наборе тестовых данных
        self.fill_text_to_field(locators.rent_info_comment_field, data['rent_info_comment'])


    @allure.step('Нажимаем кнопку "Заказать"')
    def click_on_finish_order_button(self):
        self.click_on_element(locators.rent_info_final_order_button)

    @allure.step("Подтверждаем создание заказа")
    def confirm_order(self):
        self.click_on_element(locators.confirm_order_button)

    @allure.step('Проверяем, что отображается окно об успешном заказе (появился текст с информацией о заказе)')
    def check_change_modal_window(self):
        self.find_element_with_wait(locators.success_created_order_text)

    @allure.step("Получаем текст сообщения об успешном заказе")
    def get_successful_create_order_title(self):
        return self.get_text_from_element(locators.success_created_order_text)


    @staticmethod
    def format_rent_time_locator(rent_time_option_locator, option):
        by, locator_for_format = rent_time_option_locator
        format_locator = locator_for_format.format(option)
        return by, format_locator