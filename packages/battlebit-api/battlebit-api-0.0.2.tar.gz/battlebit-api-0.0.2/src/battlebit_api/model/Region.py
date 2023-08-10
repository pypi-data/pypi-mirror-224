from enum import Enum


class Region(Enum):
    """ ENUM for the different server regions """
    DEVELOPER_SERVER = -1
    EUROPE_CENTRAL = 1
    AUSTRALIA_CENTRAL = 2
    AMERICA_CENTRAL = 3
    JAPAN_CENTRAL = 4
    BRAZIL_CENTRAL = 5
    UNKNOWN = 99
