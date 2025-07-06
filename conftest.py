import pytest
import logging
from selenium import webdriver

from pages.base_page import BasePage
from urls import main_page_url, order_page_url

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s %(message)s')

@pytest.fixture
def driver():
    logging.info("Запуск браузера Firefox")
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver  # здесь нужен yield, потому что после него driver.quit()
    logging.info("Закрытие браузера Firefox")
    driver.quit()

@pytest.fixture
def driver_main_page(driver):
    base_page = BasePage(driver)
    logging.info(f"Переход на главную страницу: {main_page_url}")
    base_page.go_to_url(main_page_url)
    return driver  # заменили yield на return

@pytest.fixture
def driver_order_page(driver):
    base_page = BasePage(driver)
    logging.info(f"Переход на страницу заказа: {order_page_url}")
    base_page.go_to_url(order_page_url)
    return driver  # заменили yield на return
