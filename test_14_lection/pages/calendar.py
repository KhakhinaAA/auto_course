from controls import *
from atf.ui import *
from datetime import date, timedelta
from atf import *


class Calendar(StickyTemplate):

    date_inp = ControlsInputDate(By.CSS_SELECTOR, '.controls-Input-DatePicker input', 'дата')
    open_calendar = Button(By.CSS_SELECTOR, '[templatename="WorkTimeDocuments/timeoff:Dialog"] [data-qa="wtd-DayTimeSelector__dateInput"]', 'пт')

    def calendar_1(self):
        self.open_calendar.double_click()
        today = date.today()
        tomorrow_date = today + timedelta(days=1)
        log({tomorrow_date})
        self.date_inp.input_date(tomorrow_date, clear_txt=True, human=True)
