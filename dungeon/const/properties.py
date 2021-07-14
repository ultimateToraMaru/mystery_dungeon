from enum import IntEnum

class Properties(IntEnum):
    MASS_WIDTH = 5
    MASS_HEIGHT = 5
    MAX_MASS_IN_ROOM_ONE_SIDE = 10  # 二倍でもいい(20)
    MAX_BLOCKS_IN_FLOOR_ONE_SIDE = 5    # 二倍でもいい(10)