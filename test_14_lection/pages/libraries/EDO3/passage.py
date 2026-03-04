from controls import *
from atf.ui import *
from atf import *


@templatename('EDO3/passage:Panel')
class Panel(DialogTemplate):
    """Карточка запуска в ДО документа"""
    approve_elm = Element(By.CSS_SELECTOR, '.controls-Button_textAlign-left', 'Согласовать отгул')
    employee_lc = ControlsLookupInput(By.CSS_SELECTOR, "[data-qa='controls-Render__field']", 'сотруд для соглос')

    def panel_stage(self, **kwargs):

        """Заполняет с кем согласовать
        и запускает согласование отгула
        :param kwargs: словарь с ключом Сотрудник"""

        log("Выбираем сотрудника из автодополнения")
        if 'Сотрудник' in kwargs.keys():
            name = kwargs['Сотрудник']
            self.employee_lc.autocomplete_search(name)

        log("Отправляем отгул на согласование")
        self.approve_elm.click()
        self.approve_elm.should_not_be(Displayed)
