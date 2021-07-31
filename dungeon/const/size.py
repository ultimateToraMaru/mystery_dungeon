from enum import IntEnum

class Size(IntEnum):
    __SCALE = 1
    MASS_WIDTH = 16
    MASS_HEIGHT = 16
    MAX_MASS_IN_ROOM_ONE_SIDE = 12*__SCALE  # 2倍でもいい(20)
    MAX_BLOCKS_IN_FLOOR_ONE_SIDE = 5    # 2倍でもいい(10)