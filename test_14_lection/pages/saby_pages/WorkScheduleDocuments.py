from atf import *
from atf.ui import *
from controls import *


class WorkScheduleDocuments(Region):
    """Реестр Графики работ/Документы в работе"""

    create_dwbtn = ExtControlsDropdownAddButton()
    search_cit = ControlsInputText(By.CSS_SELECTOR, '.sabyPage-MainLayout__search-grow', 'Поиск')
    delete_op = ControlsOperationsPanel(By.CSS_SELECTOR, '[data-qa="deleteDocumentMass"]', 'Удалить')
    notice_op = ControlsOperationsPanel(By.CSS_SELECTOR, '[data-qa="controls-operationsPanelV"]', 'Отгул')
    time_off = ControlsTreeGridView(By.CSS_SELECTOR, '[class=" controls-ListView__itemV controls-GridReact__row tw-contents controls-GridReact__row__hoverMode_row js-controls-Grid__row_editable controls-GridView__item_showActions controls-GridView__item_showActions_row controls-ListView__item_showActions_inside controls-ListView__item_showCheckbox controls-ListView__item_highlightOnHover"]', 'Отгулы')
    search = ControlsSearchInput()
    filter_cds = ControlsDateSelector(SabyBy.DATA_QA, 'DateLinkView__closeButton', 'сброс фильтра')
    actual_time_off_elm = Element(By.CSS_SELECTOR, '[title="Пчелкин Егор"]', 'Пчелкин Егор')
    pmo_open_elm = Element(By.CSS_SELECTOR, '.icon-Check2', 'ПМО')
    pmo = ControlsOperationsPanel()
    delete = ControlsOperationsPanel(By.CSS_SELECTOR, '[title="Удалить"] .controls-BaseButton__text', 'Удалить')
    agree_delete_elm = Element(SabyBy.DATA_QA, 'controls-ConfirmationDialog__button-true', 'Да')
    empty_list_hev = HintTemplateEmptyView(By.CSS_SELECTOR, '.hint-EmptyView__title', 'Не найдено ни  одной записи')
    open_calendar = Button(By.CSS_SELECTOR, '[data-qa="wtd-DayTimeSelector__dateInput"]', 'пт')

    def open(self):

        log('Переходим в Документы Графиков')
        sbis_site = self.config.get('SITE_TEST')
        self.browser.open(sbis_site)
        self.check_page_load_wasaby()

    def create_document(self, regulation='Отгул'):
        """:param regulation:"""

        self.create_dwbtn.select('Отгул', regulation)

    def search_task(self, task):
        """Поиск отгула"""
        self.filter_cds.click()
        self.search.search(task, search_btn_click=True)
        # a = self.time_off.item(contains_text=task)
        # log({a})
        # self.time_off.row(contains_text=task).should_be(Displayed)

    def re_open(self):
        self.actual_time_off_elm.click()

    def pmo_delete(self):
        self.pmo_open_elm.click()
        # self.notice_all_op.click()
        # self.pmo.open()
        self.pmo.mark_from_mass_operation('Всё', open_form=False)
        self.delete.click()
        self.agree_delete_elm.click()
        self.empty_list_hev.should_be(Displayed)


