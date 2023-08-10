from datetime import datetime
from typing import Optional

from battlebit_api.model.Map import Map
from battlebit_api.model.MapSize import MapSize
from battlebit_api.model.Region import Region
from battlebit_api.model.Server import Server


class ServerList:
    def __init__(self) -> None:
        self._servers: list[Server] = []
        self._last_updated: Optional[datetime] = None

    def update(self, servers: list[Server]) -> None:
        self._servers = servers
        self._last_updated = datetime.now()

    @property
    def last_updated(self) -> Optional[datetime]:
        return self._last_updated

    @property
    def servers(self) -> list[Server]:
        return self._servers

    def get_servers_by_map(self, map_: Map) -> list[Server]:
        servers_with_matching_criteria = []
        for server in self._servers:
            if server.map.name == map_.name:
                servers_with_matching_criteria.append(server)

        return servers_with_matching_criteria

    def get_servers_by_region(self, region: Region) -> list[Server]:
        servers_with_matching_criteria = []
        for server in self._servers:
            if server.region == region:
                servers_with_matching_criteria.append(server)

        return servers_with_matching_criteria

    def get_servers_by_size(self, size: MapSize) -> list[Server]:
        servers_with_matching_criteria = []
        for server in self._servers:
            if server.map.size == size:
                servers_with_matching_criteria.append(server)

        return servers_with_matching_criteria

    def search_for_server_by_name(self, search_str: str) -> list[Server]:
        servers_with_matching_criteria = []

        for server in self._servers:
            if search_str in server.name:
                servers_with_matching_criteria.append(server)

        return servers_with_matching_criteria

    def get_servers_sorted_by_current_players(self, many_to_few: bool = True) -> list[Server]:
        return sorted(self._servers, key=lambda s: s.current_players, reverse=many_to_few)
