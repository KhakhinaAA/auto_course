from atf import *
from atf.ui import *
from controls import *
from test_15_lection.pages.libraries.EDOPlans.scheduling.selector import Selector
from test_15_lection.pages.libraries.Addressee.popup import Stack
from test_15_lection.pages.libraries.EDOPlans.point import Dialog as CardPointPlan
# from test_15_lection.pages.libraries.StaffCommon.selectionNew import Stack as Executor


@templatename('EDOPlans/dialog:Dialog')
@parent_element('.edo3-Dialog__controller')
class Dialog(DocumentTemplate):

    """Карточка плана работ"""

    burger_object = Element(By.CSS_SELECTOR, '[data-qa="Lookup__showSelector"]', 'бургер списка объектов')
    customer_btn = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"]', 'Заказчик')
    point_plan_btn = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-menu .controls-Grid', 'Добавить пункт плана')
    save_plan_btn = Button(By.CSS_SELECTOR,
                           '[title="На выполнение"] .extControls-doubleButton__captionContent-start-mt.ws-ellipsis',
                           'На выполнение')
    point = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Grid', 'пункт плана')
    close_btn = Button(By.CSS_SELECTOR, '[data-qa="controls-stack-Button__close"]', 'Закрыть')
    obj_txt = Element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_hideCustomPlaceholder', 'Объект')

    def completion_object(self, object_text, mask):
        """Заполнение объекта из списка

        :param object_text: строка, название объекта
        :param mask: строка, опозновательное дополнение к объекту
        """
        self.burger_object.click()
        objects = Selector(self.driver)
        objects.search.search(object_text)
        delay(1)
        objects.list_object.row(contains_text=object_text).click()
        delay(2)
        self.obj_txt.type_in(mask)

    def completion_customer(self, customer_fio):
        """Выбор заказчика

        :param customer_fio: строка, ФИО сотрудника"""
        self.customer_btn.click()
        cust = Stack(self.driver)
        cust.search.search(customer_fio)
        cust.list_customer.item(contains_text=customer_fio).click()

    def completion_point_plan(self, point_text):
        """Создание и заполнение пункта плана

        :param point_text: строка, текст описания пункта плана"""
        self.point_plan_btn.item(contains_text='Пункт плана').click()

        log("Описание пункта плана")
        card = CardPointPlan(self.driver)
        card.description.type_in(point_text)

        # log("Выбор исполнителя")
        # card.executor_btn.click()
        # executor = Executor(self.driver)
        # executor.search.search(excecutor)
        # executor.list_executor.item(contains_text=excecutor).click()

        log("Сохранение пункта плана")
        card.save_point_btn.click()

    def save_plan(self):
        """Сохранение плана"""
        self.save_plan_btn.click()

    def check_point_plan(self, point_text):
        """Проверка заполнения пункта плана

        :param point_text: строка, текст описания пункта плана"""
        log("Проверяем заполнение заказчика")
        self.customer_btn.should_be(ExactText('Пчелкин Е.'))
        log("Проверяем отображение пункта плана")
        self.point.item(contains_text=point_text).should_be(Visible)
        # log("Проверяем заполнение исполнителя пункта плана")
        # self.point.item(contains_text='Бэггинс Б.и.').should_be(Visible)
        self.close_btn.click()
