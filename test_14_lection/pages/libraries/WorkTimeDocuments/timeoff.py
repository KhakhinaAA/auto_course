from controls import *
from atf.ui import *
from test_14_lection.pages.libraries.EDO3.passage import Panel
from test_14_lection.pages.libraries.Staff.selectionNew import Stack


@templatename('WorkTimeDocuments/timeoff:Dialog')
class Dialog(DocumentTemplate):
    add_ab = ExtControlsDropdownAddButton(SabyBy.DATA_QA, 'sabyPage-addButton', 'Создать отгул')
    employee_cl = ControlsLookupInput(By.CSS_SELECTOR, '[data-qa="staff-Lookup__input"] .controls-Render__wrapper',
                                      'сотрудник', catalog=Stack)
    date_elm = Element(By.CSS_SELECTOR, '.wtd-dayTimeSelector--hover-cursor-pointer', 'дата')
    reason_re = RichEditorExtendedEditor(By.CSS_SELECTOR, '.textEditor__textField', 'причина')
    phase_db = Element(By.CSS_SELECTOR, '[title="На выполнение"] span', 'На выполнение')
    open_elm = Element(By.CSS_SELECTOR, '.controls-InputBase__stretcher-block_margin-null', 'дата сегодня')
    reason = Element(By.CSS_SELECTOR, '.richEditor_Base_textContainer', 'Описание')
    clock_elm = Element(By.CSS_SELECTOR, '.icon-TimeSkinny', 'часы')
    time_el_start = ControlsInputText(By.CSS_SELECTOR, '[data-qa="wtd-TimeIntervalMinutes__start"] input', 'старт')
    time_el_end = Element(By.CSS_SELECTOR, '[data-qa="wtd-TimeIntervalMinutes__end"]', 'конец отгула')
    close_elm = Element(By.CSS_SELECTOR, '.controls-CloseButton__close__icon_functionalButton', 'закрыть карточку')

    def fill_employee(self, **kwargs):
        """Заполняем отгул
        сотрудник из автодополнения"""
        # self.open_elm.click()
        if 'Сотрудник' in kwargs.keys():
            self.employee_cl.autocomplete_search(kwargs['Сотрудник'])

    def fill_time_off(self, **kwargs):
        """Заполнение в отгуле
        причины
        дата"""
        if 'Причина' in kwargs.keys():
            self.reason_re.type_in(kwargs['Причина'])
        # cal = (self.driver)
        # cal.calendar_1()

    def run_task(self, **kwargs):
        """Отправить на выполнение"""
        self.phase_db.click()
        pan = Panel(self.driver)
        pan.panel_stage(**kwargs)
        self.phase_db.should_not_be(Displayed)

    def check_completion(self, **kwargs):
        """Проверяем заполнение Сотрудника, причины"""
        self.employee_cl.should_be(ContainsText(kwargs['Сотрудник']))
        self.reason.should_be(ContainsText(kwargs['Причина']))
        self.close_elm.click()

    def clock_time_off(self):
        """Заполняем время отгула (не справилась)"""
        self.clock_elm.click()
        self.time_el_start.type_in(1200)
        self.time_el_end.type_in('1400')
