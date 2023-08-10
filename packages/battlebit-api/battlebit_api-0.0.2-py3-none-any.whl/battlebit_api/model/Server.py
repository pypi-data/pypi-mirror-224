from dataclasses import dataclass
from typing import Optional

from battlebit_api.model.AntiCheatProvider import AntiCheatProvider
from battlebit_api.model.GameMode import GameMode
from battlebit_api.model.Map import Map
from battlebit_api.model.Region import Region


@dataclass
class Server:
    """ Dataclass representing a server """
    name: str
    map: Map
    game_mode: GameMode
    region: Region
    current_players: int
    max_players: int
    players_in_queue: int
    hz: int
    is_day_mode: bool
    is_official: bool
    has_password: bool
    anti_cheat: Optional[AntiCheatProvider]
    server_version: str
