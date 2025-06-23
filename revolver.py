import random

class RussianRouletteGame:
    def __init__(self, players):
        self.players = players
        self.bullet_position = random.randint(1, 6)
        self.current_chamber = 1

    def spin_chamber(self):
        self.current_chamber = random.randint(1, 6)

    def shoot(self, player):
        print(f"{player.get_name()} *hands trembling* pulls the trigger...")

        if self.current_chamber == self.bullet_position:
            player.kill()
            print("✴ BANG! They're dead.")
            self.bullet_position = random.randint(1, 6)
        else:
            print("CLICK!..... They're safe.")

        self.spin_chamber()