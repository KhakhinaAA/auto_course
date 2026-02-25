# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By


options = Options()

options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2,  # disable all notice
    "profile.default_content_setting_values.media_stream_mic": 2,  # disable microphone
    "profile.default_content_setting_values.media_stream_camera": 2,  # disable camera
    "profile.default_content_setting_values.geolocation": 2,  # disable geolocations
})

driver = webdriver.Chrome(options=options)
# Автоматическая установка ChromeDriver
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


sbis_site = 'https://sbis.ru/'
tenzor_site = 'https://tensor.ru/'
block_news = 'Сила в людях'
tenzor_about = 'https://tensor.ru/about'


try:
    driver.get(sbis_site)
    contacts_tab = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contacts_tab.click()
    sleep(2)
    more_office = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    more_office.click()
    tenzor = driver.find_element(By.CSS_SELECTOR,
                                 '.sbisru-Contacts__border-left--border-xm>[href="https://tensor.ru/"]')
    tenzor.click()
    sleep(2)

    driver.switch_to.window(driver.window_handles[1])
    strong = driver.find_element(By.CSS_SELECTOR, ".s-Grid-col--6 .tensor_ru-Index__card-title")
    assert strong.text == block_news, 'Не верный текст'
    assert strong.is_displayed()
    about = driver.find_element(By.CSS_SELECTOR, '.s-Grid-col.s-Grid-col--6.s-Grid-col--sm12 [href="/about"]')
    about.click()
    sleep(2)
    assert driver.current_url == 'https://tensor.ru/about', 'Не верно открыт сайт'

finally:
    driver.quit()
