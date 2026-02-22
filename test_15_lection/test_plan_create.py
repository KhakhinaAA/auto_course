from atf.ui import *
from atf import *
from pages.auth_page import AuthPage
from pages.saby_pages.Plans import Plans


class TestControls2(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        cls.browser.open(cls.config.get('SITE'))
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

    def setUp(self):
        Plans(self.driver).open()

    def test_1(self):

        """Добавьте пункт плана, указав описание и исполнителя.
        Запустите план в документооборот.
        Откройте созданный план и убедитесь, что пункт плана,
        заказчик и исполнитель отображаются согласно введенным ранее данным.
        Удалите созданный план через реестр.
        Убедитесь, что план не отображается в реестре."""

        plan_page = Plans(self.driver)
        object_text = 'Палм-Спрингс'
        customer_fio = 'Пчелкин Егор'
        point_text = 'Выполнение ДЗ'
        # excecutor = 'Бэггинс Бильбо из Шира'
        log('Создание Плана')
        plan_page.create_plan(object_text, customer_fio, point_text)
        log('Проверка Плана')
        plan_page.check_plan(object_text, point_text)
        log('Удаление Плана из реестра')
        plan_page.delete(object_text)
