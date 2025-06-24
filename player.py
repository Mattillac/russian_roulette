import time

class PlayerName:
    def __init__(self, name: str):
        self.__name = name
        self.__alive = True

    def is_alive(self):
        return self.__alive
    
    def kill(self):
        self.__alive = False

    def get_name(self):
        return self.__name
    
    def take_turn(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
class HumanPlayer(PlayerName):
    def take_turn(self, game):
        input(f"\n{self.get_name()}, press Enter to shoot.")
        game.shoot(self)

class AIEnemy(PlayerName):
    def take_turn(self, game):
        print(f"\n{self.get_name()} (AI) is taking their turn...")
        time.sleep(2)
        game.shoot(self)