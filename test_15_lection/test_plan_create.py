from atf.ui import *
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
        plan_page = Plans(self.driver)
        object_text = 'Палм-Спрингс'
        customer_fio = 'Пчелкин Егор'
        point_text = 'Выполнение ДЗ'
        excecutor = 'Бэггинс Бильбо из Шира'
        plan_page.create_plan(object_text, customer_fio, point_text)
        plan_page.check_plan(object_text, point_text)
        plan_page.delete(object_text)



        """Добавьте пункт плана, указав описание и исполнителя
        Запустите план в документооборот
        Откройте созданный план и убедитесь, что пункт плана, заказчик и исполнитель отображаются согласно введенным ранее данным
        Удалите созданный план через реестр
        Убедитесь, что план не отображается в реестре."""
