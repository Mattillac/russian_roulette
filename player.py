class PlayerName:
    def __init__(self, name: str):
        self.name = name
        self.__alive = True

    def alive(self):
        return self.__alive
    
    def kill(self):
        self.__alive = False

    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.name} - {'alive' if self.__alive else 'dead'}"