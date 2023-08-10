from dataclasses import dataclass
from typing import Optional

from battlebit_api.model.AntiCheatProvider import AntiCheatProvider
from battlebit_api.model.GameMode import GameMode
from battlebit_api.model.Map import Map
from battlebit_api.model.Region import Region
from battlebit_api.model.Server import Server


@dataclass
class ServerFilter(Server):
    """ A filter class to be used to match against Server objects """
    name: Optional[str] = None
    map: Optional[Map] = None
    game_mode: Optional[GameMode] = None
    region: Optional[Region] = None
    current_players: Optional[int] = None
    max_players: Optional[int] = None
    players_in_queue: Optional[int] = None
    hz: Optional[int] = None
    is_day_mode: Optional[bool] = None
    is_official: Optional[bool] = None
    has_password: Optional[bool] = None
    anti_cheat: Optional[AntiCheatProvider] = None
    server_version: Optional[str] = None
