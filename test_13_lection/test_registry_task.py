from atf import *
from atf.ui import *
from pages.auth_page import AuthPage
from pages.task_page import TaskRegistry
class TestRegistryTask(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASWORD'))
        cls.page = page = TaskRegistry(cls.driver)

    def setUp(self):
        self.page.check_load()
    def test_01_check_task(self):
        page.folders.row(contains_text='Папка 1').click()
        page.tasks.check_rows_number(1)

        page.folders.row(contains_text='Папака 2').expand_folders()
        page.folders.should_be(ContainsText('папка 3'))

    def test_02_search(self):
        task = 'Тестовые задачи, для тестовой зоны'
        self.page.search_task(task)
        self.page.tasks.find_cell_by_column_number(task, 5).should_be(ContainsText('29.09.15'))

        actio_1 = lambda: self.page.tasks.row(contains_text=task).select_menu_actions('Открыть в новой вкладке')
        delay(1)
        self.browser.switch_to_new_window(actio_1)

    def test_03_select(self):
        for row in range (1, 4):
            self.page.tasks.row(row).select()

        for row in range(1, 4):
            self.page.tasks.row(row).unselect()

    def test_04_delete_folder(self):
        folder = 'test_grid'
        self.page.folders.row(contains_text=folder).select_menu_actions('Удалить папку')
        self.page.popup_confirmation.confirm()
        self.page.folders.should_not_be(ContainsText(folder))

    def test_05_check_tab(self, tab):
        self.page.select_tab('На контроле')
