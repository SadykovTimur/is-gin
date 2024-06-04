from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.component.header import Header

__all__ = ['ObjectBuildingPage']


class ObjectBuildingPage(Page):
    header = Header(css='[class*="navbar"]')
    footer = Component(css='[class*="footer"]')
    title = Text(css="[class='page-content'] h1")
    title_card = Text(css="[class='page-content'] h2")
    table = Component(css='[class*="table-bordered"]')
    map = Component(id="reonmap")
    photos = Component(id="photosContainer_UploadPhotos")
    documents = Component(id="documentsTableContainer")
    panel_control = Component(css='[class*="control-panel"] ')
    fix = Component(class_name="clear-fix")
    check_btn = Components(css="[class*='btn-info']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible_header

                assert self.title in 'Список земельных участков с нецелевым использованием'
                assert self.fix.visible
                assert self.table.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_object_building_card(self) -> None:
        def condition() -> bool:
            try:
                assert self.title_card in 'Карточка объекта самовольного строительства'
                assert self.map.visible
                assert self.photos.visible
                assert self.panel_control.visible

                return self.documents.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
