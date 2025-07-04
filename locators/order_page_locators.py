# тут будут локаторы для проверок страницы заказов
from selenium.webdriver.common.by import By


# кнопка "Заказать" в хеадере на главной
init_order_button_top_on_main = [By.XPATH, './/div[contains(@class, "Header_Nav")]/button[text()="Заказать"]']

# кнопка "Заказать" внизу на главной
init_order_button_down_on_main = [By.XPATH, './/div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]']


# используем contains, так как это делает поиск полее гибким для случаев частичного изменения текста плейсхолдера
# например, при добавлении/убавлении символа "*" или изменении длинных текстов плейсхолдера

# Форма заполнения данных
# поле ввода Имени
name_field = [By.XPATH, './/input[contains(@placeholder, "Имя")]']

# поле ввода Фамилии
surname_field = [By.XPATH, './/input[contains(@placeholder, "Фамилия")]']

# поле ввода адреса
address_field = [By.XPATH, './/input[contains(@placeholder, "Адрес")]']

# поле ввода станции метро. Первую букву пропускаем, так как этого куска достаточно для нашего поиска ("метро")
# а если в плейсхолдере оставят только слово Метро, то первая буква изменится на заглавную, а у нас все продолжит работать
metro_station_field = [By.XPATH, './/input[contains(@placeholder, "етро")]']

# поле выбора станции метро. Так как у нас в кейсах нет цели тестировать выбор станции, будем выбирать конкретную станцию
metro_station_select = [By.XPATH, './/*[text()="Сокольники"]']

# поле ввода телефона
phone_field = [By.XPATH, './/input[contains(@placeholder, "Телефон")]']

# кнопка "Далее"
next_button = [By.XPATH, './/div[contains(@class, "Order_NextButton")]/button']


# Форма заполнения информации об аренде
# поле "Когда привезти самокат"
rent_info_data_field =[By.XPATH, './/input[contains(@placeholder, "Когда привезти самокат")]']

# поле "Срок аренды"
rent_info_time_field = [By.CLASS_NAME, "Dropdown-placeholder"]
# локатор для получения случайного варианта срока аренды (заготовка под форматирование)
rent_info_time_options = [By.XPATH, './/div[@class="Dropdown-option" and text()="{}"]']

# два варианта выбора цвета самоката
rent_info_color_black = [By.ID, "black"]
rent_info_color_gray = [By.ID, "grey"]

# поле для комментария
rent_info_comment_field = [By.XPATH, './/input[contains(@placeholder, "Комментарий")]']

# кнопка, завершающая процесс создания заказа
rent_info_final_order_button = [By.XPATH, './/div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]']

# Кнопка подтверждения создания заказа
confirm_order_button = [By.XPATH, './/div[contains(@class, "Order_Buttons")]/button[text()="Да"]']

# Локатор текста с подробностями о заказе
success_created_order_text = [By.XPATH, './/div[contains(@class, "Order_Text")]']
