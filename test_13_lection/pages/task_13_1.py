from atf import *
from atf.ui import *
from controls import *
from test_13_lection.pages.libraries.Message.dialogsMove import DialogTemplate as Dialog
from test_13_lection.pages.libraries.Controls.menu import Popup
from test_13_lection.pages.libraries.Controls.operationsPanel import OperationsPanel


class ContactRegistry(Region):
    folders = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="gridWrapper"].controls-Grid_master', 'Папки')
    contacts = ControlsTreeView(By.CSS_SELECTOR, '.controls-ListViewV .msg-dialogs-item', 'Сообщения')
    search = ControlsSearchInput()
    search_button = Element(By.CSS_SELECTOR, '[data-qa="Search__searchButton"]', 'Начать поиск')
    folder1_mark_elm = Element(By.CSS_SELECTOR, '[title="Папка 1"].tag-base .icon-Close', 'Папка 1')
    more = Element(By.CSS_SELECTOR, '[data-qa="item"] [title="Ещё"]', 'кнопка еще')
    close_elem = Element(By.CSS_SELECTOR, '.tags-base__close', 'сброс папки')
    tabs = ControlsTabsButtons(By.CSS_SELECTOR, '.controls-Tabs-wrapper__horizontal', 'Вкладки')
    chat_contact = ControlsTreeView(By.CSS_SELECTOR, '.controls-ListViewV .controls-BaseControl_showActions_delayed',
                                    'Контакты в чатах')
    massage_chat = ControlsTreeView(By.CSS_SELECTOR, '.controls-ListViewV .msg-Correspondence__DialogItem',
                                    'Сообщения чатов')
    pmo_open = ControlsButton(By.CSS_SELECTOR, '.controls-BaseButton .icon-Check2', 'Отметить в аккордеоне')
    notice = ControlsToolbarsView(By.CSS_SELECTOR, '.controls-Toolbar.controls-operationsPanelV__toolbar',
                                  'Действия в ПМО')
    papka_2 = ControlsTreeGridView(By.CSS_SELECTOR, '[title="Папка 2"].controls-fontsize-m', 'Папка 2')
    folder2_mark_elm = Element(By.CSS_SELECTOR, '[name="simpleContainer"] [title="Папка 2"] .icon-Close',
                               'маркер на сообщении')

    def check_load(self):
        """Поверка загрузки реестра """
        self.folders.check_load()
        self.contacts.check_load()

    def search_contact(self, contact_text):
        """Поиск сообщения"""
        delay(2)
        self.search.search(contact_text)
        self.search_button.click()
        self.contacts.item(css_selector='[title="Вес Марс 95,3 МБ (1).png"]').should_be(Displayed)

    def relocate_massage(self, menu_text, tab):
        """Перенос сообщения в папку"""
        reloc = Dialog(self.driver)
        self.contacts.mouse_over()
        self.more.click()
        delay(2)
        cont = Popup(self.driver)
        cont.context_menu.select(menu_text)
        reloc.folder_relocate.item(contains_text=tab).click()

    def check_relocate(self, tab):
        self.folder1_mark_elm.should_be(Displayed)
        self.folders.item(with_text=tab).click()
        self.contacts.item(css_selector='[title="Вес Марс 95,3 МБ (1).png"]').should_be(Displayed)

    def start_check(self):
        self.folder1_mark_elm.should_not_be(Displayed)

    def bring_it_back(self):
        self.folder1_mark_elm.click()
        self.folder1_mark_elm.should_not_be(Displayed)
        self.folders.cell(contains_text='Все').click()

    def data_tab(self, dialog, chats, interloc):
        self.tabs.select_by_contains_text(dialog)
        self.contacts.item(css_selector='.msg-dialogs-item__date').should_be(ContainsText("2 июл'24"))
        self.tabs.select_by_contains_text(chats)
        self.chat_contact.item(contains_text=interloc).click()
        self.massage_chat.item(css_selector='.msg-dialogs-item__date').should_be(ContainsText("2 июл'24"))

    def notice_tab(self, text_butn):
        self.pmo_open.click()
        # self.pmo.open()
        oper = OperationsPanel(self.driver)
        oper.pmo.mark_from_mass_operation('Всё', open_form=False)
        self.notice.select(contains_text=text_butn)
        delay(2)
        self.papka_2.click()
        delay(2)
        self.folder2_mark_elm.should_be(Displayed)

    def bring_notice_back(self):
        self.folder2_mark_elm.click()
        self.folder2_mark_elm.should_not_be(Displayed)

    def change_tab_dialog(self, dialog):
        self.tabs.select_by_contains_text(dialog)
