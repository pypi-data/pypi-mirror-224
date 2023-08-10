import logging

from battlebit_api.model.AntiCheatProvider import AntiCheatProvider
from battlebit_api.model.GameMode import GameMode
from battlebit_api.model.Map import Map
from battlebit_api.model.Region import Region
from battlebit_api.model.Server import Server


def map_game_mode_string_to_enum(gm_str: str) -> GameMode:
    gm_str = gm_str.lower().strip()
    if gm_str == "domi":
        return GameMode.DOMINATION
    elif gm_str == "conq":
        return GameMode.CONQUEST
    elif gm_str == "rush":
        return GameMode.RUSH
    elif gm_str == "voxelfortify":
        return GameMode.VOXEL_FORTIFY
    elif gm_str == "frontline":
        return GameMode.FRONTLINE
    elif gm_str == "tdm":
        return GameMode.TEAM_DEATHMATCH
    elif gm_str == "dm":
        return GameMode.DEATHMATCH
    elif gm_str == "ctf" or gm_str == "capturetheflag":
        return GameMode.CAPTURE_THE_FLAG
    logging.debug(f"Got unknown game mode: {gm_str}")
    return GameMode.UNKNOWN


def map_region_string_to_enum(rg_str: str) -> Region:
    rg_str = rg_str.lower().strip()
    if rg_str == "europe_central":
        return Region.EUROPE_CENTRAL
    elif rg_str == "australia_central":
        return Region.AUSTRALIA_CENTRAL
    elif rg_str == "america_central":
        return Region.AMERICA_CENTRAL
    elif rg_str == "japan_central":
        return Region.JAPAN_CENTRAL
    elif rg_str == "brazil_central":
        return Region.BRAZIL_CENTRAL
    elif rg_str == "developer_server":
        return Region.DEVELOPER_SERVER
    logging.debug(f"Got unknown region: {rg_str}")
    return Region.UNKNOWN


def map_anti_cheat_string_to_enum(ac_str: str) -> AntiCheatProvider:
    ac_str = ac_str.lower().strip()
    if ac_str == "eac":
        return AntiCheatProvider.EAC
    logging.debug(f"Got unknown anti cheat provider: {ac_str}")
    return AntiCheatProvider.UNKNOWN


def build_servers(parsed_json_data: list[dict]) -> list[Server]:
    servers: list[Server] = []
    for server_dict in parsed_json_data:
        server_name = server_dict["Name"]
        server_map = Map(name=server_dict["Map"], size=server_dict["MapSize"])
        server_game_mode = map_game_mode_string_to_enum(server_dict["Gamemode"])
        server_region = map_region_string_to_enum(server_dict["Region"])
        server_current_players = server_dict["Players"]
        server_max_players = server_dict["MaxPlayers"]
        server_players_in_queue = server_dict["QueuePlayers"]
        server_hz = server_dict["Hz"]
        server_is_day_mode = server_dict["DayNight"] == "Day"
        server_is_official = server_dict["IsOfficial"]
        server_has_password = server_dict["HasPassword"]
        server_anti_cheat = map_anti_cheat_string_to_enum(server_dict["AntiCheat"])
        server_server_version = server_dict["Build"]
        servers.append(
            Server(
                name=server_name,
                map=server_map,
                game_mode=server_game_mode,
                region=server_region,
                current_players=server_current_players,
                max_players=server_max_players,
                players_in_queue=server_players_in_queue,
                hz=server_hz,
                is_day_mode=server_is_day_mode,
                is_official=server_is_official,
                has_password=server_has_password,
                anti_cheat=server_anti_cheat,
                server_version=server_server_version
            )
        )

    return servers
