from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    logo = Component(css='[src*="logo"]')
    title = Component(xpath="//div[contains(text(),'АИС ГИН')]")
    title_auth = Component(xpath="//h4[contains(text(),'Авторизация в системе')]")
    login = TextField(id="Login")
    password = TextField(id="Password")
    submit = Button(id="login-btn")
    submit_sudir = Button(id="sudir-auth-btn")
    submit_login = Button(id="forms-auth-btn")
    footer = Component(css='[class*="copyright"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.title.visible
                assert self.title_auth.visible
                assert self.submit_sudir.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
