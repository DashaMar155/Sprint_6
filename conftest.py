import allure
import pytest
from selenium import webdriver
from urls import main_page_url, order_page_url  # <- исправлено

@allure.title("Открываем браузер Firefox на главной странице")
@pytest.fixture
def driver_main_page():
    driver = webdriver.Firefox()
    driver.get(main_page_url)
    yield driver
    driver.quit()

@allure.title("Открываем браузер Firefox на странице оформления заказа")
@pytest.fixture
def driver_order_page():
    driver = webdriver.Firefox()
    driver.get(order_page_url)
    yield driver
    driver.quit()
