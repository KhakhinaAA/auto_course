from atf import *
from atf.ui import *
from controls import *


@templatename('Addressee/popup:Stack')
@parent_element('[data-qa="addressee-selector-root"]')
class Stack(StackTemplate):
    """Список заказчиков"""
    list_customer = ControlsTreeGridView()
    search = ControlsSearchInput()
