# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()

options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2,  # disable all notice
    "profile.default_content_setting_values.media_stream_mic": 2,  # disable microphone
    "profile.default_content_setting_values.media_stream_camera": 2,  # disable camera
    "profile.default_content_setting_values.geolocation": 2,  # disable geolocations
})

driver = webdriver.Chrome(options=options)

sbis_site = 'https://fix-online.sbis.ru/'
my_login = 'svdmitriukov'


try:
    # Авторизоваться на сайте https://fix-online.sbis.ru/
    driver.get(sbis_site)
    login = driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] [inputmode="text"]')
    login.send_keys('svdmitriukov', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default')
    password.send_keys('Faraon88', Keys.ENTER)
    driver.maximize_window()
    sleep(6)

    # Перейти в реестр Контакты
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]>.NavigationPanels-Accordion__title_level-1')
    actions = ActionChains(driver)
    actions.double_click(contacts).perform()
    sleep(6)

    # Создать сообщение
    plus = driver.find_element(By.CSS_SELECTOR, '.extControls-addButton-icon-brand')
    plus.click()
    sleep(6)

    # Найти получателя
    search_recipient = driver.find_element(By.CSS_SELECTOR,
                                           '.controls-StackTemplate__top-area-content [inputmode="search"]')
    search_recipient.send_keys('Дмитрюков Сергей Викторович', Keys.ENTER)
    sleep(2)

    # Выбрать получателя
    recipient = driver.find_element(By.CSS_SELECTOR, '.addressee-selector-popup__view-item-wrapper')
    actions.move_to_element(recipient)
    sleep(1)
    recipient_click = driver.find_element(By.CSS_SELECTOR,
                                          '.addressee-selector-popup__view-item-wrapper '
                                          '.controls-icon_size-s.controls-BaseButton__icon')
    actions.click(recipient_click).perform()
    sleep(2)

    # Добавить в сообщение получателя
    add_to_massage = driver.find_element(By.CSS_SELECTOR, '.controls-fontsize-4xl.controls-margin_left-2xs')
    add_to_massage.click()
    sleep(2)

    # Добавить текст сообщения
    add_text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph.textEditor_Viewer__Paragraph_empty')
    add_text.send_keys('Привет')

    # Отправить сообщение
    send_massage = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    send_massage.click()
    sleep(2)

    # Проверить отображение сообщения
    list_massages = driver.find_element(By.CSS_SELECTOR,
                                        '[data-qa="msg-dialogs-item__addressee"][title="Дмитрюков Сергей Викторович"]')
    assert list_massages.is_displayed()

    # Удалить сообщение
    list_massages_2 = driver.find_elements(By.CSS_SELECTOR,
                                           '.controls-ListView__itemContent_withCheckboxes_default '
                                           '[title="Дмитрюков Сергей Викторович"]')
    actions.move_to_element(list_massages_2[0]).perform()
    sleep(1)
    delete_massage = driver.find_elements(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    actions.click(delete_massage[0]).perform()
    sleep(3)
    delete_massage_2 = driver.find_elements(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    assert delete_massage_2 == [], 'список не пуст'

finally:
    # Удалить сообщения, если тест упал
    delete_massage_2 = driver.find_elements(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    while delete_massage_2:
        # Находим элементы сообщений конкретного автора
        messages = driver.find_elements(
            By.CSS_SELECTOR,
            '.controls-ListView__itemContent_withCheckboxes_default [title="Дмитрюков Сергей Викторович"]'
        )

        if not messages:
            break

        # Перемещаем мышь над первым сообщением
        action_chains = ActionChains(driver)
        action_chains.move_to_element(messages[0])

        sleep(1)

        # Находим кнопку удаления первого сообщения
        delete_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')

        # Нажимаем на кнопку удаления
        action_chains.click(delete_button).perform()

    driver.quit()
