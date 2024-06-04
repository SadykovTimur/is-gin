from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    search = Component(css='[class*="searchBarWrapper"]')
    notification = Component(css='[class*="notifications"]')
    question = Component(css='[class*="question-circle"]')
    settings = Component(css='[class*="setting"]')
    user_block = Component(css='[class*="userblock"]')

    def is_visible(self) -> bool:
        assert self.search.visible
        assert self.notification.visible
        assert self.question.visible
        assert self.settings.visible

        return self.user_block.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
