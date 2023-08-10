from __future__ import annotations
from datetime import datetime
from typing import Optional

from battlebit_api.model.Server import Server
from battlebit_api.model.ServerFilter import ServerFilter


class ServerList:
    def __init__(self) -> None:
        self._servers: list[Server] = []
        self._last_updated: Optional[datetime] = None

    def update(self, servers: list[Server]) -> None:
        """
        Updates the ServerList with a new set of Servers. Updates the last_updated property to the current timestamp.

        :param servers: List of Server objects.
        :return: None
        """
        self._servers = servers
        self._last_updated = datetime.now()

    @property
    def last_updated(self) -> Optional[datetime]:
        return self._last_updated

    @property
    def servers(self) -> list[Server]:
        return self._servers

    def search_for_server_by_name(self, search_str: str) -> list[Server]:
        """
        Returns all Servers in which the string search_str appears as a substring in the Servers name.
        This is case sensitive.

        :param search_str: Substring to search for in Server names
        :return: All Servers in which the string search_str appears as a substring in the Servers name.
        """
        servers_with_matching_criteria = []

        for server in self._servers:
            if search_str in server.name:
                servers_with_matching_criteria.append(server)

        return servers_with_matching_criteria

    def filter_servers(self, server_filter: ServerFilter) -> ServerList:
        """
        Returns a new ServerList that only contains Servers that match the ServerFilter.
        ServerFilter properties that are set to None are ignored.

        @FixMe: typing.Self is the new best practice, but is a 3.11+ feature.
                It needs to be decided if and when 3.7 compatibility is broken.
                Current standing: Once >=3.11 is delivered as default on debian-based systems.

        :param server_filter: ServerFilter object
        :return: ServerList that only contains Servers that match the ServerFilter
        """
        servers_matching_filter: list[Server] = []
        for server in self._servers:
            if server_filter.name and server.name != server_filter.name:
                continue
            if server_filter.map and \
                    server.map.name != server_filter.map.name and \
                    server_filter.map.size != server.map.size:
                continue
            if server_filter.game_mode and server.game_mode != server_filter.game_mode:
                continue
            if server_filter.region and server.region != server_filter.region:
                continue
            if server_filter.current_players and server.current_players != server_filter.current_players:
                continue
            if server_filter.max_players and server.max_players != server_filter.max_players:
                continue
            if server_filter.players_in_queue and server.players_in_queue != server_filter.players_in_queue:
                continue
            if server_filter.hz and server.hz != server_filter.hz:
                continue
            if isinstance(server_filter.is_day_mode, bool) and server.is_day_mode != server_filter.is_day_mode:
                continue
            if isinstance(server_filter.is_official, bool) and server.is_official != server_filter.is_official:
                continue
            if isinstance(server_filter.has_password, bool) and server.has_password != server_filter.has_password:
                continue
            if server_filter.anti_cheat and server.anti_cheat != server_filter.anti_cheat:
                continue
            if server_filter.server_version and server.server_version != server_filter.server_version:
                continue
            servers_matching_filter.append(server)

        new_server_list = ServerList()
        new_server_list.update(servers_matching_filter)
        return new_server_list

    def get_servers_sorted_by_current_players(self, many_to_few: bool = True) -> list[Server]:
        """
        Returns a list of all Servers in the ServerList, sorted by the amount of current players on it.

        :param many_to_few: Used to control if the list is ascending (False) or descending (True)
        :return: List of all Servers in the ServerList, sorted by the amount of current players on it.
        """
        return sorted(self._servers, key=lambda s: s.current_players, reverse=many_to_few)
