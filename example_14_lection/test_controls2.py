from datetime import datetime
from atf import *
from atf.ui import *
from pages.auth_page import AuthPage
from pages.TaskInWork1 import TaskInWork

class TestControls2(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        cls.browser.open(cls.config.get('SITE'))
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

    def setUp(self):
        TaskInWork(self.driver).open()

    def test_1(self):
        """В карточке задачи заполнить: Описание, ответственного
           Запустить на выполнение
           Открыть на редактирование и добавить веху"""

        task_data = {'Исполнитель': 'Задач Автотест', 'Описание': 'Задача на вебинаре'}
        task_page = TaskInWork(self.driver)
        task_card = task_page.create_document('Задача')
        task_card.fill_task(**task_data)
        task_card.run_task()
        task_card.open_to_redaction()
        task_card.select_milestone('Смена вехи 1')

    def test_2(self):
        """Выбор из справочника"""
        task_page = TaskInWork(self.driver)
        task_card = task_page.create_document('Задача')
        task_card.executor_cl.click().select('Задача Автотест')
