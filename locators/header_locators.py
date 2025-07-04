from selenium.webdriver.common.by import By

# Локатор логотипа самоката
logo_samokat_locator = [By.XPATH, './/img[@alt="Scooter"]']

# Локатор логотипа Яндекса — именно ссылка <a>, а не <img>
logo_yandex_locator = [By.XPATH, './/a[contains(@href, "yandex.ru")]']
