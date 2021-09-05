from manager.character_manager import Character_manager


class Enemy_manager(Character_manager):
    def __init__(self, enemy):
        super().__init__(enemy)

    def get_input(self):
        enemy_direction = self.character.command()

        return enemy_direction