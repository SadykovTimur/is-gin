from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.component.header import Header

__all__ = ['MainPage']


class MainPage(Page):
    header = Header(css='[class*="navbar"]')
    footer = Component(css='[class*="footer"]')
    monitoring = Component(id="outdated-stats-container")
    search_form = Component(id="searchFormDiv")
    subsystem = Components(css='[class*="subsystem-gin-panel"]')
    iframe = Component(tag='iframe')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible

                assert self.subsystem[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=110, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_frame(self) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)

        def condition() -> bool:
            try:
                assert self.monitoring.visible

                return self.search_form.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=110, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
        self.driver.switch_to.default_content()
