from player import PlayerName
from revolver import RussianRouletteGame

def main():
    names = input("Enter player names (comma separated): ").split(",")
    players = [PlayerName(name.strip()) for name in names]

    game = RussianRouletteGame(players)

    while len([p for p in players if p.is_alive()]) > 1:
        for player in players:
            if player.is_alive():
                input(f"\n{player.get_name()}, press Enter to shoot.")
                game.shoot(player)
                if not player.is_alive():
                    break

    winner = [p for p in players if p.is_alive()][0]
    print(f"\n {winner.get_name()} is the last one laughing!")

if __name__ == "__main__":
    main()