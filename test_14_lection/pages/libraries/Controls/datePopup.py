from controls import *
from atf.ui import *
from datetime import date, timedelta
from atf import *
from test_14_lection.pages.saby_pages.WorkScheduleDocuments import WorkScheduleDocuments


@templatename('Controls/datePopup')
class DatePopup(StickyTemplate):
    """Выбор даты в отгуле"""

    date_inp = ControlsInputDate(By.CSS_SELECTOR, '.controls-Input-DatePicker input', 'дата')

    def calendar_1(self):
        op_cal = WorkScheduleDocuments(self.driver)
        op_cal.open_calendar.double_click()
        today = date.today()
        tomorrow_date = today + timedelta(days=1)
        log({tomorrow_date})
        self.date_inp.input_date(tomorrow_date, clear_txt=True, human=True)
