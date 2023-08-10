from dataclasses import dataclass

from battlebit_api.model.MapSize import MapSize


@dataclass
class Map:
    name: str
    size: MapSize
