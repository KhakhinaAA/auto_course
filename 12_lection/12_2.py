# Авторизоваться на сайте
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf.ui import *
from atf import *
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR,'.controls-InputBase__field.controls-InputBase__field_margin-null.controls-InputBase__field_theme_default_margin-null.controls-Render__field.controls-Render__field_textAlign_left.ws-ellipsis.controls-Render__field_zIndex>[inputmode="text"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-Password__nativeField_caretFilled.controls-Password__nativeField_caretFilled_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder', 'пароль')

class OnlineMain(Region):
    tasks = Element(By.CSS_SELECTOR, '[data-qa="Задачи"] [data-qa="NavigationPanels-Accordion__title"]', 'Задачи')

class Tasks(Region):
    task_in_work = Element(By.CSS_SELECTOR, '[data-qa="controls-Tabs__item-element"] [href="/page/tasks-in-work"]', 'В работе')
    highlighting_incoming = Element(By.CSS_SELECTOR, '[style="top: 0px; bottom: 0px; z-index: 3;"]>[title="Входящие"]', 'Стиль выделения')
    marker = Element(By.CSS_SELECTOR, '[style="top: 0px; bottom: 0px; z-index: 3;"] [data-qa="marker"]', 'маркер на входящих')
    list_tasks = CustomList(By.CSS_SELECTOR, '.edws-MainColumn.ws-ellipsis.ws-flexbox.edws-MainColumn-unreaded', 'Список задач')
    regular = Element(By.CSS_SELECTOR, '[title="Регулярные"]', 'регулярные')
    highlighting_regular = Element(By.CSS_SELECTOR, '[style]>[title="Регулярные"]', 'выделение регулярных')
    marker_regular = Element(By.CSS_SELECTOR, '[style]>[data-qa="marker"]', 'маркер регулярных')


class PlusCreate(Region):
    plus = Element(By.CSS_SELECTOR, '.controls-icon_size-m.extControls-addButton-icon-brand.icon-RoundPlus.controls-icon', 'плюс для создания')
    folder = Element(By.CSS_SELECTOR, '.edws-AddButtonItem.ws-flexbox.ws-align-items-center.ws-ellipsis', 'Создани папки')

class CreateFolder(Region):
    txt_input = TextField(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]>[inputmode="text"]', 'Название новой папки')
    save_folder = Element(By.CSS_SELECTOR, '.controls-BaseButton.controls-Button_clickable.controls-Button_bg-same.controls-button-style.controls-button_outlined-style.controls-button_size-m.controls-button_outlined-primary-style.controls-Button_notCircle.controls-fontsize-m.controls-button_fontsize-m.controls-notFocusOnEnter.edws-UserFolderDialog__buttonSave', 'Сохранить')

class NewFolder(Region):
    new_folder = Element(By.CSS_SELECTOR, '[title="Отправленные"]', 'Новая папка')
    empty_folder = Element(By.CSS_SELECTOR, '[data-qa="hint-Template-Wrapper"] [data-qa="hint-EmptyView__title"]', 'Пустая заглушка')
    delete_folder = Element(By.CSS_SELECTOR, '[title="Удалить папку"]', 'Кнопка удалить папку')
    yes_delete = Element(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Да, удалить')
    menu = CustomList(By.CSS_SELECTOR, '.controls-itemActionsV.js-controls-ListView__visible-on-hoverFreeze.controls-itemActionsV_style_master.controls-itemActionsV_outside.controls-itemActionsV__outside_bottom_size-default.undefined', 'список меню')
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
        tasks_adv.highlighting_incoming.should_be(Visible)
        tasks_adv.marker.should_be(Visible)

        log('Убедиться, что папка не пустая (в реестре есть задачи)')
        tasks_adv.list_tasks.should_not_be(CountElements(0))

        log('Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято')
        tasks_adv.regular.click()

        tasks_adv.highlighting_incoming.should_not_be(Visible)
        tasks_adv.marker.should_not_be(Visible)

        tasks_adv.highlighting_regular.should_be(Visible)
        tasks_adv.marker_regular.should_be(Visible)

        log('Создать новую папку и перейти в неё')
        plus_btn = PlusCreate(self.driver)
        plus_btn.plus.click()
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

        #если тест упал, то нужно удалять за собой папку, если она есть






