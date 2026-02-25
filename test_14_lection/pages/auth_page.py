from atf.ui import *


class AuthPage(Region):

    login_inp = TextField(By.CSS_SELECTOR, '.controls-InputBase__field_theme_default_margin-null>input', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')

    def auth(self, login: str, password: str):
        """Авторизация"""

        self.browser.open(self.config.get('SBIS_SITE'))
        self.login_inp.type_in(login + Keys.ENTER)
        self.login_inp.should_be(ExactText(login))
        self.password_inp.type_in(password + Keys.ENTER)
        self.password_inp.should_not_be(Displayed, wait_time=True)
        self.check_page_load_wasaby()
