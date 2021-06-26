from abc import ABCMeta


class Obj (metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    # @abstractmethod
    def create(self, x, y):
        pass