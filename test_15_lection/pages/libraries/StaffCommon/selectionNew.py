from atf import *
from atf.ui import *
from controls import *


@templatename('StaffCommon/selectionNew:Stack')
class Stack(StackTemplate):

    """Панель выбора исполнителя пункта плана"""

    list_executor = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"] [data-qa="staffCommon-List_view"] .controls-Grid', 'Исполнит')
    search = ControlsSearchInput(By.CSS_SELECTOR, '[data-qa="StaffWrapper-addresseeTab__search"].controls-Render input', 'поиск')

