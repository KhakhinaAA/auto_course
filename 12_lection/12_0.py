# Авторизоваться на сайте https://fix-online.sbis.ru/                                                                  (Например, "Регламент123"/"Регламент1231")
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили

from atf.ui import *
from atf import log, info
from atf import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
#sbis_site = 'https://fix-sso.saby.ru/auth-online/fix-online.sbis.ru/?ret=fix-online.sbis.ru/'
sbis_title = 'Saby (ex СБИС) вход в личный кабинет системы'

class MainSbisRu(Region):
    tabs = CustomList(By.CSS_SELECTOR, '.sbisru-Header__menu-item', 'Вкладки')
    start_work = Button(By.CSS_SELECTOR, '.sbisru-Button--primary', 'Начать работу')

class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR,[], 'логин')
    password_inp = TextField(By.CSS_SELECTOR, [], 'пароль')

class MainOnline(Region):
    news_title = CustomList(By.CSS_SELECTOR, '.feed-Title', 'Заголовки новостей')
    popup_menu = Element(By.CSS_SELECTOR, '[]', 'контекстное меню')
class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
       self.browser.open(sbis_site)
       sleep(4)
       log('Проверить адрес сайта и заголовок страницы')
       self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))

       log('проверить отображение четырех вкладок')
       sbis_ru = MainSbisRu(self.driver)
       sbis_ru.tabs.should_be(CountElements(4))

       log('Проверить текст, атрибут и видимость кнопки Начать работу')
       button_txt = 'Начать работу'
       sbis_ru.start_work.should_be(ExactText(button_txt), Attribute(title=button_txt)).click()

       log('Перейти на страницу авторизации')
       self.browser.switch_to_new_window(sbis_ru.start_work.click)

       log('Проверить адрес сайта и заголовок страницы')
       self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact('Вход в личный кабинет'))

       log('Авторизоваться')
       user_login, user_password = '',''
       auth = AuthOnline(self.driver)
       auth.login_inp.type_in(user_login+Keys.ENTER).should_be(ExactText(user_login))
       auth.password_inp.type_in(user_password+Keys.ENTER).should_be(Not(Visible))

       log('Навести курсор на новость и сделать контекстный клик')
       main_online = MainOnline(self.driver)
       main_online.news_title.item(3).scroll_into_view().context_click()

       log('Проверить отображение контекстного меню')
       main_online.popup_menu.should_be(Visible)

       assert_that(1, equal_to(2), 'Не верное количество')
       assert_that('a', is_in(dict(a=1)), 'Не найден нужный ключ')

       assert_that(lambda: sbis_ru.tabs.count_elements, equal_to(4), 'Не верное количество табов', and_wait()) ,будет каждый раз высчитывать новое количество табов, если без лямбда, то вернет текущее
