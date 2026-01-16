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
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()

options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2,  # disable all notice
    "profile.default_content_setting_values.media_stream_mic": 2,  # disable microphone
    "profile.default_content_setting_values.media_stream_camera": 2,  # disable camera
    "profile.default_content_setting_values.geolocation": 2,  # disable geolocations
})

driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

sbis_site = 'https://fix-online.sbis.ru/'
my_login = 'svdmitriukov'


try:
    driver.get(sbis_site)
    login = driver.find_element(By.CSS_SELECTOR, '.controls-InputBase__field.controls-InputBase__field_margin-null.controls-InputBase__field_theme_default_margin-null.controls-Render__field.controls-Render__field_textAlign_left.ws-ellipsis.controls-Render__field_zIndex>[inputmode="text"]')
    login.send_keys('svdmitriukov', Keys.ENTER)
    #assert login.get_attribute('value') == 'my_login'
    password = driver.find_element(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-Password__nativeField_caretFilled.controls-Password__nativeField_caretFilled_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder')
    password.send_keys('Faraon88', Keys.ENTER)
    driver.maximize_window()
    sleep(6)


    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]>.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1')
    actions = ActionChains(driver)
    actions.double_click(contacts).perform()
    sleep(6)

    plus = driver.find_element(By.CSS_SELECTOR, '.controls-icon_size-m.extControls-addButton-icon-brand.icon-RoundPlus.controls-icon')
    plus.click()
    sleep(6)

    search_recipient = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area-content [inputmode="search"]')
    search_recipient.send_keys('Дмитрюков Сергей Викторович', Keys.ENTER)
    sleep(2)

    recipient = driver.find_element(By.CSS_SELECTOR, '.ws-flexbox.addressee-selector-popup__view-item-wrapper.addressee-selector-popup__view-item-wrapper-buttons-container.msg-combined-addressees__button-wrapper')
    actions.move_to_element(recipient)
    sleep(1)
    recipient_click = driver.find_element(By.CSS_SELECTOR, '.controls-icon_size-s.controls-BaseButton__icon.icon-RoundPlus.controls-icon')
    actions.click(recipient_click).perform()
    sleep(2)
    add_to_massage = driver.find_element(By.CSS_SELECTOR, '.controls-icon_svg.controls-icon_size-m.controls-icon_style-contrast.controls-fontsize-4xl.controls-margin_left-2xs')
    add_to_massage.click()
    sleep(2)

    add_text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph.textEditor_Viewer__Paragraph_empty')
    add_text.send_keys('Привет')
    send_massage = driver.find_element(By.CSS_SELECTOR,'.controls-icon_size-s.controls-BaseButton__icon.icon-BtArrow.controls-icon')
    send_massage.click()
    sleep(2)
    list_massages = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee"][title="Дмитрюков Сергей Викторович"]')
    assert list_massages.is_displayed()
    list_massages_2 = driver.find_elements(By.CSS_SELECTOR, '.controls-ListView__itemContent.controls-ListView__item_default-topPadding_s.controls-ListView__item_default-bottomPadding_s.controls-ListView__item-rightPadding_m.controls-ListView__itemContent_withCheckboxes.controls-ListView__itemContent_withCheckboxes_default [title="Дмитрюков Сергей Викторович"]')
    actions.move_to_element(list_massages_2[0]).perform()
    sleep(1)
    delete_massage = driver.find_elements(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    actions.click(delete_massage[0]).perform()
    sleep(3)
    delete_massage_2 = driver.find_elements(By.CSS_SELECTOR, '.controls-ListView__itemContent.controls-ListView__item_default-topPadding_s.controls-ListView__item_default-bottomPadding_s.controls-ListView__item-rightPadding_m.controls-ListView__itemContent_withCheckboxes.controls-ListView__itemContent_withCheckboxes_default [title="Дмитрюков Сергей Викторович"]')
    assert delete_massage_2 == [], 'список не пуст'
    # actions.context_click(element).perform()
finally:
    while delete_massage_2 != []:
        list_massages_2 = driver.find_elements(By.CSS_SELECTOR,
                                               '.controls-ListView__itemContent.controls-ListView__item_default-topPadding_s.controls-ListView__item_default-bottomPadding_s.controls-ListView__item-rightPadding_m.controls-ListView__itemContent_withCheckboxes.controls-ListView__itemContent_withCheckboxes_default [title="Дмитрюков Сергей Викторович"]')
        actions.move_to_element(list_massages_2[0]).perform()
        sleep(1)
        delete_massage = driver.find_elements(By.CSS_SELECTOR,
                                              '[data-qa="controls-itemActions__action deleteToArchive"]')
        actions.click(delete_massage[0]).perform()


    driver.quit()
