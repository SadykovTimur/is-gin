from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(css='[class="logo"]')
    home = Component(xpath="//a[text()='Главная']")
    settings = Component(xpath="//a[text()='Настройки']")
    document = Component(xpath="//a[text()='Документация']")
    list = Component(xpath="//a[text()='Списки']")
    project = Component(xpath="//a[text()='Проектные инициативы']")
    notification = Component(id="navbar-notification")
    info = Component(id="navbar-user-info")
    exit = Component(css='[class*="logout"]')
    pwd = Component(css='[class*="key"]')

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.home.visible
        assert self.settings.visible
        assert self.document.visible
        assert self.project.visible
        assert self.notification.visible
        assert self.info.visible
        assert self.exit.visible

        return self.pwd.visible

    @property
    def is_visible_header(self) -> bool:
        assert self.home.visible
        assert self.settings.visible
        assert self.document.visible
        assert self.list.visible
        assert self.project.visible
        assert self.notification.visible
        assert self.exit.visible

        return self.pwd.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
