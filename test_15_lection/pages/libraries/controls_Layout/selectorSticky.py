from controls import *


@templatename('Controls-Layout/selectorSticky:Template')
class Template(StickyTemplate):
    """Выпадающий список регламентов планов по кнопке + в реестре планов"""

    menu = ControlsTreeGridView(By.CSS_SELECTOR, '[template="Controls-Layout/selectorSticky:Template"] .controls-Grid',
                                'Регламенты планов')
    