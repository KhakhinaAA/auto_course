from atf.ui import *
from atf import *
from time import sleep


class ListContacts(Region):
    search_inp = Element(By.CSS_SELECTOR, '.addressee-selector-popup__browser-search [inputmode="search"]', 'поиск')
    plus_cont = Button(By.CSS_SELECTOR, '[data-qa="addressee-selector-popup__button-add-selection"]', 'Добавить')
    recipient = Element(By.CSS_SELECTOR, '.msg-combined-addressees__button-wrapper', 'Получатель')
    plus_letter = Element(By.CSS_SELECTOR, '[data-qa="msg-create-theme-btn__public"]', 'создание сообщения')


class AuthOnline(Region):
    login = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] [inputmode="text"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')


class Contacts(Region):
    contacts = Element(By.CSS_SELECTOR, '[data-qa="Контакты"]>.NavigationPanels-Accordion__title_level-1', 'Раздел')
    plus = Element(By.CSS_SELECTOR, '.extControls-addButton-icon-brand', 'плюс')


class Letter(Region):
    text_letter = TextField(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph_empty', 'ввод текста')
    button_send = Button(By.CSS_SELECTOR, '.msg-send-editor__send .controls-BaseButton__wrapper', 'Отправить')


class ListLetters(Region):
    letter_in_list = Element(By.CSS_SELECTOR,
                             '[data-qa="msg-dialogs-item__addressee"][title="Дмитрюков Сергей Викторович"]',
                             'сообщение')
    del_letter = CustomList(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]', 'Удалить')
    letter_in_list_2 = CustomList(By.CSS_SELECTOR,
                                  '[data-qa="msg-dialogs-item__addressee"][title="Дмитрюков Сергей Викторович"]',
                                  'сообщение')


class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)

        log('Авторизоваться')
        user_login, user_password = 'svdmitriukov', 'Faraon88'
        auth = AuthOnline(self.driver)
        auth.login.type_in(user_login+Keys.ENTER).should_be(ExactText(user_login))
        auth.password.type_in(user_password+Keys.ENTER).should_be(Not(Visible))

        log('Навести курсор на контакты и сделать контекстный клик')
        contacts_button = Contacts(self.driver)
        contacts_button.contacts.double_click()

        log('создать сообщение')
        plus_button = Contacts(self.driver)
        plus_button.plus.click()

        log('Указать сотрудника для отправки письма')
        search_inp_rec = ListContacts(self.driver)
        recip = 'Дмитрюков Сергей Викторович'
        search_inp_rec.search_inp.type_in(recip)
        sleep(2)
        search_inp_rec.search_inp.type_in(Keys.ENTER)

        log('навести и выбрать получателя')
        rec_in_list = ListContacts(self.driver)
        rec_in_list.recipient.mouse_over()
        rec_in_list.plus_cont.click()

        log('создать сообщение')
        plus_lttr = ListContacts(self.driver)
        plus_lttr.plus_letter.click()

        log('ввод текста в сообщение')
        text_lttr = Letter(self.driver)
        text = 'Привет'
        text_lttr.text_letter.type_in(text, clear_txt=False)

        log('отправка сообщения')
        btn_send = Letter(self.driver)
        btn_send.button_send.click()

        log('Проверяем наличие сообщения в списке')
        lttr_in_list = ListLetters(self.driver)
        lttr_in_list.letter_in_list.should_be(Visible)

        log('наведение и удаление сообщения')
        lttr_in_list.letter_in_list.mouse_over()
        lttr_in_list.del_letter.item(1).click()

        log('Проверка, что сообщение удалилось')
        lttr_in_list.letter_in_list_2.should_be(CountElements(0))

        """Не сделала:
           #1) не выставила фильтр, если фильтр изменится, то всё упадет
           #2) не удаляю корзину
           #3) не удаляю сообщения, которые остаются при прерывании теста"""