from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.component.header import Header

__all__ = ['CheckListPage']


class CheckListPage(Page):
    header = Header(css='[class*="navbar"]')
    footer = Component(css='[class*="footer"]')
    title = Text(css="[class='page-content'] h2")
    table = Component(id="control-index-table")
    map = Component(id="reonmap")
    photos = Component(id="photosContainer_UploadPhotos")
    controls = Component(id="tabControls")
    panel_control = Component(css='[class*="control-panel"] ')
    fix = Component(class_name="clear-fix")
    check_btn = Components(css="[class*='btn-info']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible_header

                assert self.title in 'Проверки/Обследования/Инструментальный мониторинг'
                assert self.fix.visible
                assert self.table.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=90, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_checklist_card(self) -> None:
        def condition() -> bool:
            try:
                assert self.title in ['Карточка инструментального мониторинга', 'Карточка Мероприятия']
                assert self.map.visible
                assert self.photos.visible
                assert self.panel_control.visible

                return self.controls.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=85, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
