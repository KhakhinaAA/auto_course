# Авторизоваться на сайте https://fix-online.sbis.ru/                                                                  (Например, "Регламент123"/"Регламент1231")
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили

from atf.ui import *
from atf import *
from time import sleep
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By


class List_contacts(Region):
    search_inp = Element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area-content [inputmode="search"]', 'строка поиска')
    plus_cont = Button(By.CSS_SELECTOR, '.controls-icon_size-s.controls-BaseButton__icon.icon-RoundPlus.controls-icon', 'Выбор Получателя')
    recipient = Element(By.CSS_SELECTOR, '.ws-flexbox.addressee-selector-popup__view-item-wrapper.addressee-selector-popup__view-item-wrapper-buttons-container.msg-combined-addressees__button-wrapper', 'Получатель в списке')
    plus_letter = Element(By.CSS_SELECTOR, '.controls-icon_svg.controls-icon_size-m.controls-icon_style-contrast.controls-fontsize-4xl.controls-margin_left-2xs', 'создание сообщения')
class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR,'.controls-InputBase__field.controls-InputBase__field_margin-null.controls-InputBase__field_theme_default_margin-null.controls-Render__field.controls-Render__field_textAlign_left.ws-ellipsis.controls-Render__field_zIndex>[inputmode="text"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-Password__nativeField_caretFilled.controls-Password__nativeField_caretFilled_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder', 'пароль')

class Contacts(Region):
    contacts = Element(By.CSS_SELECTOR, '[data-qa="Контакты"]>.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1', 'Раздел контакты')
    plus = Element(By.CSS_SELECTOR, '.controls-icon_size-m.extControls-addButton-icon-brand.icon-RoundPlus.controls-icon', 'плюс')

class Letter(Region):
    text_letter = TextField(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph.textEditor_Viewer__Paragraph_empty', 'ввод текста')
    button_send = Button(By.CSS_SELECTOR, '.controls-icon_size-s.controls-BaseButton__icon.icon-BtArrow.controls-icon', 'кнопка отправки сообщения')

class List_Letters(Region):
    letter_in_list = Element(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee"][title="Дмитрюков Сергей Викторович"]', 'полученное сообщение')
    del_letter = CustomList(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]', 'кнопка удаления')
    letter_in_list_2 = CustomList(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee"][title="Дмитрюков Сергей Викторович"]', 'полученное сообщение')
class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)

       # log('Проверить адрес сайта и заголовок страницы')
       # self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))
       #
       # log('проверить отображение четырех вкладок')
       # sbis_ru = MainSbisRu(self.driver)
       # sbis_ru.tabs.should_be(CountElements(4))
       #
       # log('Проверить текст, атрибут и видимость кнопки Начать работу')
       # button_txt = 'Начать работу'
       # sbis_ru.start_work.should_be(ExactText(button_txt), Attribute(title=button_txt)).click()
       #
       # log('Перейти на страницу авторизации')
       # self.browser.switch_to_new_window(sbis_ru.start_work.click)
       #
       # log('Проверить адрес сайта и заголовок страницы')
       # self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact('Вход в личный кабинет'))
       #
        log('Авторизоваться')
        user_login, user_password = 'svdmitriukov','Faraon88'
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in(user_login+Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password+Keys.ENTER).should_be(Not(Visible))

        log('Навести курсор на контакты и сделать контекстный клик')
        contacts_button = Contacts(self.driver)
        contacts_button.contacts.double_click()

        log('создать сообщение')
        plus_button = Contacts(self.driver)
        plus_button.plus.click()

        log('Указать сотрудника для отправки письма')
        search_inp_rec = List_contacts(self.driver)
        recip = 'Дмитрюков Сергей Викторович'
        search_inp_rec.search_inp.type_in(recip)
        sleep(2)
        search_inp_rec.search_inp.type_in(Keys.ENTER)

        log('навести и выбрать получателя')
        rec_in_list = List_contacts(self.driver)
        rec_in_list.recipient.mouse_over()
        rec_in_list.plus_cont.click()

        log('создать сообщение')
        plus_lttr = List_contacts(self.driver)
        plus_lttr.plus_letter.click()

        log('ввод текста в сообщение')
        text_lttr = Letter(self.driver)
        text = 'Привет'
        text_lttr.text_letter.type_in(text, clear_txt=False)

        log('отправка сообщения')
        btn_send = Letter(self.driver)
        btn_send.button_send.click()

        log('Проверяем наличие сообщения в списке')
        lttr_in_list = List_Letters(self.driver)
        lttr_in_list.letter_in_list.should_be(Visible)

        log('наведение и удаление сообщения')
        lttr_in_list.letter_in_list.mouse_over()
        lttr_in_list.del_letter.item(1).click()
        #lttr_in_list.del_letter.item(contains_text='').click()


        log('Проврка, что сообщение удалилось')
        lttr_in_list.letter_in_list_2.should_be(CountElements(0))

        #Не сделала:
           #1) не выставила фильтр, если фильтр изменится, то всё упадет
           #2) не удаляю корзину
           #3) не удаляю сообщения, которые остаются при прерывании теста


       # main_online.popup_menu.should_be(Visible)
       #
       # assert_that(1, equal_to(2), 'Не верное количество')
       # assert_that('a', is_in(dict(a=1)), 'Не найден нужный ключ')
       #
       # assert_that(lambda: sbis_ru.tabs.count_elements, equal_to(4), 'Не верное количество табов', and_wait()) ,будет каждый раз высчитывать новое количество табов, если без лямбда, то вернет текущее
