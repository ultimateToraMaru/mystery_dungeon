from enum import IntEnum

class Size(IntEnum):
    __SCALE = 1
    MASS_WIDTH = 16 # 5 or 16
    MASS_HEIGHT = MASS_WIDTH
    MAX_MASS_IN_ROOM_ONE_SIDE = 10*__SCALE  # 2倍でもいい(20)
    MAX_BLOCKS_IN_FLOOR_ONE_SIDE = 5    # 2倍でもいい(10)