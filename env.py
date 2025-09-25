"""
Environment -related: class and methods.
E.g. the site URL
"""
import pytest
import requests
# import json


class Env:
    def __init__(self, name: str, host_url: str):
        self.name = name
        self.host_url = host_url
        self.session = None


    def get(self, url):
        return requests.get(url)

    def get_endpoint(self, endpoint: str):
        """
        endpoint is part of URL to be applied with host
        return requests.Response
        """
        return requests.get(f'{self.host_url}{endpoint}')   #  "data": json.loads(res.text)


def env_():
    """ To be used in fixture as well as outside"""
    return Env("w3", "https://www.w3.org/")


@pytest.fixture()
def env():
    return env_()
