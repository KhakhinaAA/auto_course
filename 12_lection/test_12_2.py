# Авторизоваться на сайте.
# Перейти в реестр Задачи на вкладку "В работе".
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи).
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято.
# Создать новую папку и перейти в неё.
# Убедиться, что она пустая.
# Удалить новую папку, проверить, что её нет в списке папок.
# Для сдачи задания пришлите код и запись с экрана прохождения теста.

from atf.ui import *
from atf import *
from controls import *


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] [inputmode="text"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')


class OnlineMain(Region):
    tasks = Element(By.CSS_SELECTOR, '[data-qa="Задачи"] [data-qa="NavigationPanels-Accordion__title"]', 'Задачи')


class Tasks(Region):
    task_in_work = Element(By.CSS_SELECTOR, '[title="В работе"]', 'В работе')
    hligh_incom = Element(By.CSS_SELECTOR, '.controls-Grid__row-cell_selected-master [title="Входящие"]', 'фокус вход')
    marker = Element(By.CSS_SELECTOR, '.controls-Grid__row-cell_selected-master [data-qa="marker"]', 'маркер')
    list_tasks = CustomList(By.CSS_SELECTOR, '.edws-MainColumn-unreaded', 'Задачи')
    regular = Element(By.CSS_SELECTOR, '[title="Регулярные"]', 'регулярные')
    hlgh_reg = Element(By.CSS_SELECTOR, '.controls-Grid__row-cell_selected-master [title="Регулярные"]', 'фокус регул')


class PlusCreate(Region):
    plus = Element(By.CSS_SELECTOR, '.extControls-addButton-icon-brand', 'плюс')
    folder = Element(By.CSS_SELECTOR, '.edws-AddButtonItem.ws-flexbox.ws-align-items-center.ws-ellipsis', 'плюс папка')


class CreateFolder(Region):
    txt_input = TextField(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]>[inputmode="text"]', 'Название')
    save_folder = Element(By.CSS_SELECTOR, '.edws-UserFolderDialog__buttonSave', 'Сохранить')


class NewFolder(Region):
    new_folder = Element(By.CSS_SELECTOR, '[title="Отправленные"]', 'Новая папка')
    empty_folder = Element(By.CSS_SELECTOR, '[data-qa="hint-Template-Wrapper"] [data-qa="hint-EmptyView__title"]',
                           'заглушка')
    delete_folder = Element(By.CSS_SELECTOR, '[title="Удалить папку"]', 'Кнопка удалить папку')
    yes_delete = Element(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Да, удалить')
    menu = CustomList(By.CSS_SELECTOR, '.controls-itemActionsV__outside_bottom_size-default', 'список меню')


class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)

        log('Авторизоваться')
        user_login, user_password = 'khakhinaNastya', 'khakhinaNastya123'
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password + Keys.ENTER).should_be(Not(Visible))

        log('Навести курсор на задачи и сделать контекстный клик')
        tasks_bttn = OnlineMain(self.driver)
        tasks_bttn.tasks.double_click()

        log('Перейти на вкладку "В работе"')
        tasks_adv = Tasks(self.driver)
        tasks_adv.task_in_work.click()

        log('Убедиться, что выделена папка "Входящие" и стоит маркер.')
        tasks_adv.hligh_incom.should_be(Visible)
        tasks_adv.marker.should_be(Visible)

        log('Убедиться, что папка не пустая (в реестре есть задачи)')
        tasks_adv.list_tasks.should_not_be(CountElements(0))

        log('Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято')
        tasks_adv.regular.click()

        log('Выделение снято с Входящих')
        tasks_adv.hligh_incom.should_not_be(Visible)

        tasks_adv.hlgh_reg.should_be(Visible)
        tasks_adv.marker.should_be(Visible)

        log('Создать новую папку и перейти в неё')
        plus_btn = PlusCreate(self.driver)
        delay(1)
        plus_btn.plus.click()
        delay(2)
        plus_btn.folder.click()

        log('Ввод названия новой папки и сохранение')
        new_folder = CreateFolder(self.driver)
        txt = 'Отправленные'
        new_folder.txt_input.type_in(txt)
        new_folder.save_folder.click()

        log('Переключаемся на новую папку')
        sent_folder = NewFolder(self.driver)
        sent_folder.new_folder.click()
        sent_folder.empty_folder.should_be(Visible)
        sent_folder.new_folder.mouse_over()
        sent_folder.menu.item(2).click()
        sent_folder.delete_folder.click()
        sent_folder.yes_delete.click()

        sent_folder.new_folder.should_not_be(Visible)

        '''#если тест упал, то нужно удалять за собой папку, если она есть'''
