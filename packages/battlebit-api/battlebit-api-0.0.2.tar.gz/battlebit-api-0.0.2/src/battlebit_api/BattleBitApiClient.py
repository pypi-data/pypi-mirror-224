import logging

import requests

from battlebit_api.ServerBuilder import build_servers
from battlebit_api.model.ServerList import ServerList

logging.basicConfig(level=logging.ERROR)


class BattleBitApiClientException(Exception):
    """
    Thrown for unexpected exceptions.

    :note: If you encounter this, please send an error report to this packages' maintainer.
    """
    def __init__(self, msg: str):
        self.msg = msg


class BattleBitApiRateLimitExceeded(Exception):
    """ Thrown if the rate limit for the BattleBit API is reached """
    def __init__(self):
        self.msg = "You've reached the API's rate limit. Consider limiting your update cycles."


class BattleBitApiClient:
    """
    Entrypoint class for the package. Obtain an instance of this class to make API calls.
    """
    ENDPOINTS: dict = {
        "server_list": "Servers/GetServerList"
    }

    def __init__(self, root_endpoint: str = "https://publicapi.battlebit.cloud") -> None:
        """
        :param root_endpoint: Endpoint URL to the BattleBit API, should point to the correct one by default.
        """
        self._root_endpoint = root_endpoint.rstrip("/")
        self._server_list = ServerList()

    def get_server_list(self, with_update: bool = True) -> ServerList:
        """
        Returns a ServerList object. This does only pull from the BattleBit API if the server list has never
        been polled, or if forced to by the with_update switch.

        :param with_update: If True, this method will get data from the API, if not it will return the cached ServerList.
        :return: A ServerList object
        """
        if with_update or not self._server_list.last_updated:
            r = requests.get(f"{self._root_endpoint}/{self.ENDPOINTS['server_list']}")
            if r.status_code != 200:
                if r.status_code == 429:
                    raise BattleBitApiRateLimitExceeded()
                raise BattleBitApiClientException(f"Could not connect with BattleBit API. Status Code was: {r.status_code}")
            self._server_list.update(build_servers(r.json()))
        return self._server_list
