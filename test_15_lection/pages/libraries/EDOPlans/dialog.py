from atf import *
from atf.ui import *
from controls import *
from test_15_lection.pages.libraries.EDOPlans._scheduling.selector import Selector
from test_15_lection.pages.libraries.Addressee.popup import Stack
from test_15_lection.pages.libraries.EDOPlans.point import Dialog as CardPointPlan
from test_15_lection.pages.libraries.StaffCommon.selectionNew import Stack as Executor



@templatename('EDOPlans/dialog:Dialog')
@parent_element('.edo3-Dialog__controller')
class Dialog(DocumentTemplate):
    """Карточка плана работ"""
    burger_object = Element(By.CSS_SELECTOR, '[data-qa="Lookup__showSelector"]', 'бургер списка объектов')
    customer_btn = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"]', 'Заказчик')
    point_plan_btn = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-menu .controls-Grid', 'Добавить пункт плана')
    save_plan_btn = Button(By.CSS_SELECTOR, '[title="На выполнение"] .extControls-doubleButton__captionContent-start-mt.ws-ellipsis', 'На выполнение')
    point = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Grid', 'пункт плана')
    close_btn = Button(By.CSS_SELECTOR, '[data-qa="controls-stack-Button__close"]', 'Закрыть')


    def completion_object(self, object_text):
        self.burger_object.click()
        object = Selector(self.driver)
        object.search.search(object_text)
        delay(1)
        object.list_object.row(contains_text=object_text).click()
        delay(2)

    def completion_customer(self, customer_fio):
        self.customer_btn.click()
        cust = Stack(self.driver)
        cust.search.search(customer_fio)
        cust.list_customer.item(contains_text=customer_fio).click()

    def completion_point_plan(self, point_text):
        self.point_plan_btn.item(contains_text='Пункт плана').click()
        card = CardPointPlan(self.driver)
        card.description.type_in(point_text)
        # card.executor_btn.click()
        # executor = Executor(self.driver)
        # executor.search.search(excecutor)
        # executor.list_executor.item(contains_text=excecutor).click()
        card.save_point_btn.click()

    def save_plan(self):
        self.save_plan_btn.click()

    def check_point_plan(self, point_text):
        self.customer_btn.should_be(ExactText('Пчелкин Е.'))
        self.point.item(contains_text=point_text).should_be(Visible)
        # self.point.item(contains_text='Бэггинс Б.и.').should_be(Visible)
        self.close_btn.click()








