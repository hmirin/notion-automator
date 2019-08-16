import os
from datetime import datetime, timedelta, timezone
from sys import argv

from notion.block import PageBlock

from src.client import ArchiveClient
from src.hook import PageHook


def archiver(client: ArchiveClient, from_url: str, to_url: str):
    jst = timezone(timedelta(hours=9), 'JST')
    current_date = str(datetime.now(jst).date())

    def hook(page: PageBlock):
        page.title = current_date + "_" + page.title

    from_page = client.get_page(from_url)
    to_page = client.get_page(to_url)
    client.copy_page(from_page, to_page, hook=PageHook(hook))


if __name__ == '__main__':
    token = os.environ["NOTION_TOKEN"]
    from_url = argv[1]
    to_url = argv[2]
    client = ArchiveClient(token)
    archiver(client, from_url, to_url)
