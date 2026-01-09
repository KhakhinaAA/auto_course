from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

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
