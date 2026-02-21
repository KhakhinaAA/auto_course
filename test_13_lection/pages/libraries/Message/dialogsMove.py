from controls import *


@templatename('Message/dialogsMove:DialogTemplate')
class DialogTemplate(DialogTemplate):
    """Список папок в окне Переноса"""
    folder_relocate = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="gridWrapper"]', 'папка  для переноса')
