from abc import ABCMeta

from notion.block import PageBlock, TodoBlock, Block
from notion.client import NotionClient

from lib.copy import copy_block
from .hook import TodoHook, PageHook


class AutomatedClient(object):
    def __init__(self, token_v2: str):
        self.notion_client = NotionClient(token_v2=token_v2)

    def get_page(self, url) -> PageBlock:
        block = self.notion_client.get_block(url)
        if not isinstance(block, PageBlock):
            print("Warning: This block is notPageBlock.")
        return block


class ArchiveClient(AutomatedClient):
    """Archive current page status by copying blocks recursively and make this  """
    def __init__(self, token_v2: str):
        super().__init__(token_v2)

    def copy_page(self, page: PageBlock, parent: Block = None, hook: PageHook = None):
        # copy page under parent recursively, after that hook will be called
        copied_page = copy_block(page, parent)
        if hook is not None:
            hook.execute(copied_page)
        return copied_page