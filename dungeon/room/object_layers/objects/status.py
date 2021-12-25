class Status():
    def __init__(self, room_address, position, name, level, hp, max_hp, mp, max_mp, attack, defense, exp):

        self.__room_address = room_address
        self.__position = position

        # ステータス
        self.__name: str = name
        self.__level: int = level
        self.__hp: int = hp
        self.__max_hp: int = max_hp
        self.__mp: int = mp
        self.__max_mp: int = max_mp
        self.__attack: int = attack
        self.__defense: int = defense
        self.__exp: int = exp

    @property
    def room_address(self):
        pass

    @room_address.getter
    def room_address(self):
        return self.__room_address

    @room_address.setter
    def room_address(self, room_address):
        self.__room_address = room_address

    @property
    def position(self):
        pass

    @position.getter
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def level(self):
        pass

    @level.getter
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def hp(self):
        pass

    @hp.getter
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def max_hp(self):
        pass

    @max_hp.getter
    def max_hp(self):
        return self.__max_hp

    @max_hp.setter
    def max_hp(self, max_hp):
        self.__max_hp = max_hp

    @property
    def mp(self):
        pass

    @mp.getter
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, mp):
        self.__mp = mp

    @property
    def max_mp(self):
        pass

    @max_mp.getter
    def max_mp(self):
        return self.__max_mp

    @max_mp.setter
    def max_mp(self, max_mp):
        self.__max_mp = max_mp

    @property
    def attack(self):
        pass

    @attack.getter
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @property
    def defense(self):
        pass

    @defense.getter
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        self.__defense = defense

    @property
    def exp(self):
        pass

    @exp.getter
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        self.__exp = exp

    @property
    def alive(self):
        pass

    @alive.getter
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, alive):
        self.__alive = alive