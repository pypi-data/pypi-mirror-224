import logging

import requests

from battlebit_api.ServerBuilder import build_servers
from battlebit_api.model.ServerList import ServerList

logging.basicConfig(level=logging.ERROR)


class BattleBitApiClientException(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class BattleBitApiRateLimitExceeded(Exception):
    def __init__(self):
        self.msg = "You've reached the API's rate limit. Consider limiting your update cycles."


class BattleBitApiClient:
    ENDPOINTS: dict = {
        "server_list": "Servers/GetServerList"
    }

    def __init__(self, root_endpoint: str = "https://publicapi.battlebit.cloud") -> None:
        self._root_endpoint = root_endpoint.rstrip("/")
        self._server_list = ServerList()

    def get_server_list(self, with_update: bool = True) -> ServerList:
        if with_update or not self._server_list.last_updated:
            r = requests.get(f"{self._root_endpoint}/{self.ENDPOINTS['server_list']}")
            if r.status_code != 200:
                if r.status_code == 429:
                    raise BattleBitApiRateLimitExceeded()
                raise BattleBitApiClientException(f"Could not connect with BattleBit API. Status Code was: {r.status_code}")
            self._server_list.update(build_servers(r.json()))
        return self._server_list
