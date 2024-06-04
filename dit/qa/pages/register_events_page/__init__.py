from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.register_events_page.component.header import Header

__all__ = ['RegisterEventsPage']


class RegisterEventsPage(Page):
    title = Text(css='h4[class*="typography"]')
    info = Component(css='[class*="contentInfo"]')
    map = Component(id="reonmap")
    header = Header(css='[class*="styles_header"]')
    breadcrumb = Text(css='[class*="ant-breadcrumb"] ')
    item = Components(css='[role="menuitem"]')
    table = Component(css='[class="ant-table-content"]')
    tasks = Components(css='[class*="RegistriesContainer"] ')
    loader = Component(css='[class*="spinning"]')

    @property
    def is_loader_hide(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible()

                assert 'Главная' in self.breadcrumb
                assert 'Планирование' in self.breadcrumb
                assert 'Задачи' in self.breadcrumb
                assert 'Функциональные' in self.breadcrumb
                assert self.is_loader_hide
                assert self.item[0].visible

                return self.table.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=90, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_register_events_card(self) -> None:
        def condition() -> bool:
            try:
                assert self.title in 'Задача'
                assert self.info.visible
                assert self.is_loader_hide

                return self.map.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=85, msg='Card was not loaded')
        self.app.restore_implicitly_wait()
