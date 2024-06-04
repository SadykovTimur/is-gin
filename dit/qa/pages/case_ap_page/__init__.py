from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.component.header import Header

__all__ = ['CaseApPage']


class CaseApPage(Page):
    header = Header(css='[class*="navbar"]')
    footer = Component(css='[class*="footer"]')
    title = Text(css='[class="page-content"] h1')
    table = Component(id="gbox_gridTable")
    panel_control = Component(css='[class*="control-panel"]')
    tab = Component(id="tabApDelo")
    main = Component(id="mainApDelo")
    fix = Component(class_name="clear-fix")
    check_btn = Components(css="[class*='btn-info']")
    loader = Component(css='[class*="spinner"]')

    @property
    def is_loader_hide(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible_header

                assert self.title in 'Дела АП'
                assert self.fix.visible
                assert self.table.visible
                assert self.is_loader_hide

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_case_card(self) -> None:
        def condition() -> bool:
            try:
                assert self.title in 'Карточка дела'
                assert self.tab.visible
                assert self.main.visible

                return self.panel_control.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Card was not loaded')
        self.app.restore_implicitly_wait()
