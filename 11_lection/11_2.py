# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
try:
    login = driver.find_element(By.CSS_SELECTOR, '[name = "Login"]')
    login.send_keys('svd', Keys.ENTER)
    assert login.get_attribute('value') == 'my_login'
    password = driver.find_element(By.CSS_SELECTOR, '[name = password]')
    password.send_keys('discus_admin123', Keys.ENTER)
    driver.maximize_window()

    recipient = driver.find_elements(By.CSS_SELECTOR, '')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(recipient[1])
    action_chains.context_click(news[1])
    action_chains.perform()

    # actions.context_click(element).perform()
finally:
    driver.quit()
