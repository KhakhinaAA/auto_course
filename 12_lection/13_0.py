from atf.ui import *
from atf import *
#from selenium.webdriver.common.by import By

class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR,'.controls-InputBase__field.controls-InputBase__field_margin-null.controls-InputBase__field_theme_default_margin-null.controls-Render__field.controls-Render__field_textAlign_left.ws-ellipsis.controls-Render__field_zIndex>[inputmode="text"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-Password__nativeField_caretFilled.controls-Password__nativeField_caretFilled_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder', 'пароль')


class Test(TestCaseUI):
    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)
