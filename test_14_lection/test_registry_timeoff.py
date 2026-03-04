from atf.ui import *
from atf import *
from pages.auth_page import AuthPage
from pages.saby_pages.WorkScheduleDocuments import WorkScheduleDocuments
from test_14_lection.pages.libraries.WorkTimeDocuments.timeoff import Dialog
from atf.api.json_rpc import JsonRpcClient
from api.wrappers.wtd_functions import WTDFunctions


class TestControls2(TestCaseUI):
    client = None
    autotest_mask = "Пчелкин Егор"

    @classmethod
    def setUpClass(cls):
        cls.browser.open(cls.config.get('SITE'))
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

        cls.client = JsonRpcClient(url="https://fix-online.sbis.ru/", verbose_log=2)
        cls.client.auth(login='khakhinaNastya', password="khakhinaNastya123")

        log("Удаляем отгул через api")
        WTDFunctions(cls.client).delete_wtd_forever(cls.autotest_mask)

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
        log('Создаем отгул')
        task_page = WorkScheduleDocuments(self.driver)
        task_page.create_document('Отгул')
        log('Заполняем отгул')
        task_card = Dialog(self.driver)
        task_card.fill_employee(**task_data)
        task_card.fill_time_off(**task_data)
        task_card.run_task(**task_data)
        log('Проверяем отгул')
        task_page.re_open(task)
        task_card.check_completion(**task_data)
        task_page.search_task(task)
        # log('Удаляем отгул')
        # task_page.pmo_delete()

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
        log('Создаем отгул')
        task_page.create_document('Отгул')
        task_card = Dialog(self.driver)
        task_card.employee_cl.click().select(task)
        log('Заполняем отгул')
        task_card.fill_time_off(**task_data)
        # task_card.clock_time_off()
        task_card.run_task(**task_data)
        log('Проверяем отгул')
        task_page.re_open(task)
        task_card.check_completion(**task_data)
        log('Находим отгул')
        task_page.search_task(task)
        # task_page.pmo_delete()

    @classmethod
    def tearDownClass(cls):
        log("Удаляем отгул через api")
        WTDFunctions(cls.client).delete_wtd_forever(cls.autotest_mask)
