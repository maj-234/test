from pprint import pprint
import requests
from dotenv import load_dotenv
import os
import xml.etree.ElementTree as ET
from notion_client import Client
from notion_client.helpers import collect_paginated_api

load_dotenv()
client = Client(auth="secret_t1Y58csDcqIFnpEhBFstYgZZJszNaSFpLz8rDn0wqou")

def stand4(word):
    url = os.getenv("SYNO_STAND4") + os.getenv("USERID_STAND4") + os.getenv("TOKEN_STAND4") + "word="
    response = requests.get(url + word)
    tree = ET.fromstring(response.content)
    for child in tree:
        for e in child:
            print(e.tag, ":", e.text)
    # print(response.text)


def notionapi():
    users = client.users.list()
    pprint(users)
    page = client.pages.properties.parent
    pprint(page)
    print(type(page))
    response = client.pages.retrieve(
        **{
            "page_id": "4147ff0c32cb4b719be6380172c3c73b",
            "properties": [
                "Title"
            ]
        }
    )
    """database = client.databases.query(
        **{
            "database_id": "fb1f0e79eb974e5fb13d825a4e433544",
        }
    )
    print(database)
    print(type(database)) """


if __name__ == "__main__":
    # stand4("subsist")
    notionapi()
