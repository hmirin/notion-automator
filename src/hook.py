from abc import ABCMeta, abstractmethod

from notion.block import TodoBlock, PageBlock


class Hook(metaclass=ABCMeta):
    def __init__(self, func):
        self.hook = func

    @abstractmethod
    def execute(self, something):
        return self.hook(something)


class TodoHook(Hook):
    def execute(self, todo: TodoBlock):
        self.hook(todo)


class PageHook(Hook):
    def execute(self, page: PageBlock):
        self.hook(page)
