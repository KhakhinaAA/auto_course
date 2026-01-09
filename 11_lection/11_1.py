# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

sbis_site = 'https://sbis.ru/'
tenzor_site = 'https://tensor.ru/'
block_news = 'Сила в людях'
tenzor_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()


try:
    driver.get(sbis_site)
    contacts_tab = driver.find_element(By.CSS_SELECTOR,'')
    actions = ActionChains(driver)
    actions.double_click(contacts_tab).perform()
    sleep(2)
    tenzor_btn = driver.find_element(By.CSS_SELECTOR,'')
    tenzor_btn.click()
    sleep(2)

    driver.switch_to.window(driver.window_handles[1])


    assert driver.current_url == 'https://tensor.ru/about', 'Не верно открыт сайт'
    assert driver.title == block_news, 'Не верный заголовок'
    # assert len(tabs) == 4
    # assert start_btn.text == 'Начать работу'
    # assert start_btn.getattribute('title') == start_btn_text
    # свойство для скрола по списку news[5].location_once_scrolled_into_view
    assert block_news_tab.is_displayed()
finally:
    driver.quit()