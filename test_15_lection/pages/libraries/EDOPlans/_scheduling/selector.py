from atf import *
from atf.ui import *
from controls import *


@templatename('EDOPlans/_scheduling/Selector')
class Selector(StackTemplate):
    """Карточка Объекта планирования"""
    list_object = ControlsTreeGridView(By.CSS_SELECTOR, '.plan-Scheduling-Selector__stack .controls-Grid', 'список объектов')
    search = ControlsSearchInput()
