import os
from utils.requests_helper import BaseSession


def demoqa() -> BaseSession:
    demo_url = os.getenv('demo_shop_url')
    return BaseSession(base_url=demo_url)


def reqres() -> BaseSession:
    reqres_url = os.getenv('reqres_api')
    return BaseSession(base_url=reqres_url)