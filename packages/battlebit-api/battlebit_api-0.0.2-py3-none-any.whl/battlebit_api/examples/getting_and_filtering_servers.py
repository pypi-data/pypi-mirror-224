from pprint import pprint

from battlebit_api.BattleBitApiClient import BattleBitApiClient
from battlebit_api.model.GameMode import GameMode
from battlebit_api.model.Map import Map
from battlebit_api.model.MapSize import MapSize
from battlebit_api.model.ServerFilter import ServerFilter

# Obtaining instance of BattleBitApiClient
my_api_client = BattleBitApiClient()

# Obtaining a ServerList
server_list = my_api_client.get_server_list()

# Printing human-readable version of server list to console
pprint(server_list.servers)

# Creating new filter
map_and_game_mode_filter = ServerFilter(
    map=Map(
        name="Azagor",
        size=MapSize.SMALL
    ),
    game_mode=GameMode.TEAM_DEATHMATCH
)

# Applying filter
filtered_server_list = server_list.filter_servers(map_and_game_mode_filter)

# Printing human-readable version of filtered server list to console
pprint(filtered_server_list.servers)
