from atf.ui import *


class AuthPage(Region):

    login_inp = TextField(By.CSS_SELECTOR, '.controls-InputBase__field_theme_default_margin-null>input', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')

    def auth(self, login: str, password: str):
        """Авторизация"""

        self.browser.open(self.config.get('SITE_CONTACTS'))
        self.login_inp.type_in(login + Keys.ENTER)
        self.login_inp.should_be(ExactText(login))
        self.password_inp.type_in(password + Keys.ENTER)
