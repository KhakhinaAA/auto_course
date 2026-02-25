from atf import *
from atf.ui import *
from controls import *


class TaskInWork(Region):
    """Реестр Графики работ/Документы в работе"""

    create_dwbtn = ExtControlsDropdownAddButton()

    def open(self):

        log('Переходим в Документы Графиков')
        sbis_site = self.config.get('SITE_TEST')
        self.browser.open(sbis_site)
        self.check_page_load_wasaby()

    def create_document(self, regulation='Отгул'):
        """:param regulation:"""

        from pages.taskDialog import Dialog

        self.create_dwbtn.select(regulation)
        task_card = Dialog(self.driver)
        task_card.check_open()
        return task_card
