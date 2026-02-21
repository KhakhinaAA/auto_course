from atf.ui import *
from pages.auth_page import AuthPage
from pages.saby_pages.WorkScheduleDocuments import WorkScheduleDocuments
from test_14_lection.pages.libraries.WorkTimeDocuments.timeoff import Dialog


class TestControls2(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        cls.browser.open(cls.config.get('SITE'))
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

    def setUp(self):
        WorkScheduleDocuments(self.driver).open()

    def test_1(self):
        """В карточке отгула заполнить: сотрудника (автодополнение), дату на завтра, причину
                   Запустить на выполнение
                   Убедиться, что появился в реестре
                   При переоткрытии значения в полях сохранились
                   Удалить"""
        task_data = {'Сотрудник': 'Пчелкин Егор', 'Причина': 'Отгул домашнее задание'}
        task = 'Пчелкин Егор'
        task_page = WorkScheduleDocuments(self.driver)
        task_page.create_document('Отгул')
        task_card = Dialog(self.driver)
        task_card.fill_employee(**task_data)
        task_card.fill_time_off(**task_data)
        task_card.run_task(**task_data)
        task_page.re_open()
        task_card.check_completion(**task_data)
        task_page.search_task(task)
        task_page.pmo_delete()

    def test_2(self):
        """В карточке отгула заполнить: сотрудник (из справочника)
            время завтра с 12 до 14 часов
            описание
            Убедиться, что появился в реестре
            При переоткрытии значения в полях сохранились
            Удалить"""
        task_data = {'Сотрудник': 'Пчелкин Егор', 'Причина': 'Отгул домашнее задание'}
        task = 'Пчелкин Егор'
        task_page = WorkScheduleDocuments(self.driver)
        task_page.create_document('Отгул')
        task_card = Dialog(self.driver)
        task_card.employee_cl.click().select(task)
        task_card.fill_time_off(**task_data)
        # task_card.clock_time_off()
        task_card.run_task(**task_data)
        task_page.re_open()
        task_card.check_completion(**task_data)
        task_page.search_task(task)
        task_page.pmo_delete()



