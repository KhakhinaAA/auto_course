from atf.ui import *
from controls import *
class ContactRegistry(Region):
    folders = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MasterDetail .ControlGrid', 'Папки')
    contacts = ControlsTreeGridView(By.CSS_SELECTOR, '.briaskOnMe .ControlGrid', 'Контакты')
    search = ControlsSearchInput()
    tabs = ControlsTabsButtons()
    tasks_ctrl = ControlsTreeGridView(By.CSS_SELECTOR, '.hjj .Controls-Grid', 'Задача на контроле')
    def check_load(self):
        """Поверка загрузки реестра """
        self.folders.check_load()
        self.tasks.check_load()

    def search_task(self, task):
        """Поиск задачи"""
        self.search.search(task, search_btn_click=True)
        self.tasks.row(contains_text=task).should_be(Displayed)

    def select_tab(self, tab):
        self.tabs.select(tab)
        self.tasks_ctrl.check_load()