# Авторизоваться на сайте
# Откройте эталонную задачу по прямой ссылке в новой вкладке браузера
# Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",
# где ДАТА и НОМЕР - это ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями

from atf.ui import *
from atf import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

excecutor_txt = 'Хахина А.А.'
date_txt = '25 янв, вс'
number_txt = '879'
descrub_txt = 'Купить всем игристого'


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] [inputmode="text"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')


class TaskOpt(Region):
    executor = Element(By.CSS_SELECTOR, '[data-qa="SelectedCollection__item__caption"]', 'Исполнитель')
    date = Element(By.CSS_SELECTOR, ' [data-qa="edo3-Document_docDate"] [class="controls-EditableArea__Text__inner"]',
                   'Дата')
    number = Element(By.CSS_SELECTOR,
                     '[data-qa="edo3-Document_docNumber"] [class="controls-EditableArea__Text__inner"]',
                     'Номер')
    descrubtion = Element(By.CSS_SELECTOR, ' [data-qa="mte"] [class="mte-formattedText__part text-style"]', 'Описание')
    author = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"][title="Хахина А.А."]', 'Автор')


# class UrlTask(Region):
#     url_task = Link(By.LINK_TEXT,
#     'https://fix-online.sbis.ru/doc/95af7896-630f-4e68-b9ca-ae8f1b1b7ef8?client=6242047',
#     'ссылка на задачу')

class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)

        log('Авторизоваться')
        user_login, user_password = 'khakhinaNastya', 'khakhinaNastya123'
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password + Keys.ENTER).should_be(Not(Visible))

        log('Переход по прямой ссылке')
        url_task_txt = 'https://fix-online.sbis.ru/doc/95af7896-630f-4e68-b9ca-ae8f1b1b7ef8?client=6242047'
        self.browser.create_new_tab(url_task_txt)
        self.browser.switch_to_opened_window()

        log('Проверка заголовка')
        sbis_title = 'Задача №879 от 25.01.26'
        self.browser.should_be(TitleExact(sbis_title))

        log('Проверка исполнителя, даты, номера, описания, автора')
        txt = TaskOpt(self.driver)
        txt.date.should_be(ExactText(date_txt))
        txt.executor.should_be(ExactText(excecutor_txt))
        txt.number.should_be(ExactText(number_txt))
        txt.descrubtion.should_be(ExactText(descrub_txt))
        txt.author.should_be(ExactText(excecutor_txt))
