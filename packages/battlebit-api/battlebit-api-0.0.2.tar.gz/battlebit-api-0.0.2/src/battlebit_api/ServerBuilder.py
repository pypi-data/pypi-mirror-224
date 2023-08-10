import logging

from battlebit_api.model.AntiCheatProvider import AntiCheatProvider
from battlebit_api.model.GameMode import GameMode
from battlebit_api.model.Map import Map
from battlebit_api.model.MapSize import MapSize
from battlebit_api.model.Region import Region
from battlebit_api.model.Server import Server


def map_game_mode_string_to_enum(gm_str: str) -> GameMode:
    """
    Maps the game mode string returned be the BattleBit API to the correct ENUM value.

    :param gm_str: String containing information about the game mode
    :return: GameMode ENUM value
    :note: If GameMode.UNKNOWN is returned, the API may have changed or new game modes have been added.
    """
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
    """
    Maps the region string returned be the BattleBit API to the correct ENUM value.

    :param rg_str: String containing information about the region
    :return: Region ENUM value
    :note: If Region.UNKNOWN is returned, the API may have changed or new regions have been added.
    """
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
    """
    Maps the anti cheat string returned be the BattleBit API to the correct ENUM value.

    :param ac_str: String containing information about the anti cheat provider
    :return: AntiCheatProvider ENUM value
    :note: If AntiCheatProvider.UNKNOWN is returned, the API may have changed or new anti cheat providers have been added.
    """
    ac_str = ac_str.lower().strip()
    if ac_str == "eac":
        return AntiCheatProvider.EAC
    logging.debug(f"Got unknown anti cheat provider: {ac_str}")
    return AntiCheatProvider.UNKNOWN


def map_map_size_string_to_enum(ms_str: str) -> MapSize:
    """
    Maps the map size string returned be the BattleBit API to the correct ENUM value.

    :param ms_str: String containing information about the map size
    :return: MapSize ENUM value
    :note: If MapSize.UNKNOWN is returned, the API may have changed or new map sizes have been added.
    """
    ms_str = ms_str.lower().strip()
    if ms_str == "small":
        return MapSize.SMALL
    elif ms_str == "medium":
        return MapSize.MEDIUM
    elif ms_str == "big":
        return MapSize.BIG
    elif ms_str == "ultra":
        return MapSize.ULTRA
    logging.debug(f"Got unknown map size: {ms_str}")
    return MapSize.UNKNOWN


def build_servers(parsed_json_data: list[dict]) -> list[Server]:
    """
    Parses the JSON data from the BattleBit API to Server objects

    :param parsed_json_data: pre-parsed JSON data as provided by the requests package
    :return: List of Server objects
    """
    servers: list[Server] = []
    for server_dict in parsed_json_data:
        server_name = server_dict["Name"]
        server_map = Map(name=server_dict["Map"], size=map_map_size_string_to_enum(server_dict["MapSize"]))
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
