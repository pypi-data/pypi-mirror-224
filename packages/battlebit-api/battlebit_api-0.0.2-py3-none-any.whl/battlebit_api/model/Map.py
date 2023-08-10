from dataclasses import dataclass

from battlebit_api.model.MapSize import MapSize


@dataclass
class Map:
    """ Dataclass representing a map """
    name: str
    size: MapSize
