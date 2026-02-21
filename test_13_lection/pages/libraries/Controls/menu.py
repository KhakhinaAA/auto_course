from controls import *


@templatename('Controls/menu:Popup')
class Popup(StickyTemplate):
    """Доп меню сообщения"""
    context_menu = ControlsPopup(By.CSS_SELECTOR, '.controls_popupTemplate_theme-default.controls-Zoom', 'диалог меню')
