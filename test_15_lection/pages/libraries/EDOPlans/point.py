from atf import *
from atf.ui import *
from controls import *


@templatename('EDOPlans/point:Dialog')
class Dialog(DocumentTemplate):
    """Карточка пункта плана"""

    description = TextField(By.CSS_SELECTOR, '.plan-PointDialog__panel [inputmode="text"]', 'Описание')
    executor_btn = Element(By.CSS_SELECTOR, '.plan-PointDialog__panel [title="Добавить исполнителя"]', 'Добавить исполнителя')
    save_point_btn = Element(By.CSS_SELECTOR, '.extControls-doubleButton_same_style-success', 'Сохранить план')

