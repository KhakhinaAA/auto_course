from atf import *
from atf.ui import *
from controls import *
from test_15_lection.pages.libraries.controls_Layout.selectorSticky import Template
from test_15_lection.pages.libraries.EDOPlans.dialog import Dialog


class Plans(Region):
    """Реестр Планов"""

    plans = ControlsTreeGridView(By.CSS_SELECTOR, '.edo4-ListWrapper-scroll-container .controls-Grid', 'Планы')
    add_ab = ControlsDropdownButton(By.CSS_SELECTOR, '.extControls-addButton-icon-brand', 'Добавить')
    yes_btn = Element(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Да')
    search = ControlsSearchInput()

    def open(self):
        """Открывает реестр планов"""
        log('Переходим в реестр Планов')
        sbis_site = self.config.get('SITE_TEST')
        self.browser.open(sbis_site)
        self.check_page_load_wasaby()

    def create_plan(self, object_text, mask, customer_fio, point_text):
        """Создает и заполняет план

        :param object_text: строка, название объекта
        :param mask: строка, опозновательное дополнение к объекту
        :customer_fio: строка, ФИО сотрудника
        :point_text:  текст описания пункта плана"""
        self.add_ab.click()
        menu = Template(self.driver)
        menu.menu.item(contains_text='План работ').click()

        log('Заполнение объекта')
        card = Dialog(self.driver)
        card.completion_object(object_text, mask)

        log('Заполнение Заказчика')
        card.completion_customer(customer_fio)

        log('Создание/Заполнение пункта плана')
        card.completion_point_plan(point_text)
        card.save_plan()
        delay(1)

    def check_plan(self, object_text, point_text):
        """Проверяет заполнение плана
        :param object_text: строка, название объекта
        :point_text:  текст описания пункта плана"""
        self.plans.item(contains_text=object_text).click()
        card = Dialog(self.driver)
        card.check_point_plan(point_text)

    # def delete(self, object_text):
    # """Находит и удаляет план
    # :param object_text: строка, название объекта"""
    #     self.search.search(object_text)
    #     self.plans.row(contains_text=object_text).select_menu_actions('Удалить')
    #     self.yes_btn.click()
    #     self.search.search(object_text)
    #     self.plans.row(contains_text=object_text).should_not_be(Visible)
