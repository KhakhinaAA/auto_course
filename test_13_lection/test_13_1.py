from atf.ui import *
from pages.auth_page import AuthPage
from pages.task_13_1 import ContactRegistry


class TestRegLesson(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))
        cls.page = ContactRegistry(cls.driver)

    def test_1_relocate(self):
        self.page.check_load()
        contact_text = 'Вес Марс 95,3 МБ (1).png'
        menu_text = 'Перенести в папку'
        tab = 'Папка 1'
        self.page.search_contact(contact_text)
        self.page.start_check()
        self.page.relocate_massage(menu_text, tab)
        self.page.check_relocate(tab)
        self.page.bring_it_back()

    def test_data(self):
        dialog = 'Диалоги'
        chats = 'Чаты'
        interloc = 'Смирнова Маргарита Алексеевна'
        contact_text = 'Вес Марс 95,3 МБ (1).png'
        self.page.search_contact(contact_text)
        self.page.data_tab(dialog, chats, interloc)

    def test_teg(self):
        contact_text = 'Вес Марс 95,3 МБ (1).png'
        text_butn = "Пометить"
        dialog = 'Диалоги'
        self.page.change_tab_dialog(dialog)
        self.page.search_contact(contact_text)
        self.page.notice_tab(text_butn)
        self.page.bring_notice_back()
