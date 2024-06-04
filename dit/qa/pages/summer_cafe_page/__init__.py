from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.component.header import Header

__all__ = ['SummerCafePage']


class SummerCafePage(Page):
    header = Header(css='[class*="navbar"]')
    footer = Component(css='[class*="footer"]')
    title = Text(css="[class='page-content'] h1")
    title_card = Text(css="[class='page-content'] h2")
    search = Component(id="searchFormDiv")
    main = Component(id="main-form")
    table = Component(css='[class*="table-bordered"]')
    panel_control = Component(css='[class*="control-panel"] ')
    fix = Component(class_name="clear-fix")
    check_btn = Components(css="[class*='btn-info']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible_header

                assert self.title in 'Нестационарные торговые объекты'
                assert self.fix.visible
                assert self.table.visible
                assert self.search.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_summer_cafe_card(self) -> None:
        def condition() -> bool:
            try:
                assert self.title_card in 'Карточка летнего кафе'
                assert self.main.visible

                return self.panel_control.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
