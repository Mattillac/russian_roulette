from player import HumanPlayer, AIEnemy
from revolver import RussianRouletteGame
from ascii_art import AsciiArt

def main():
    AsciiArt.skull()
    names = input("Enter players (human/s:John, ai:Bot): ").split(",")

    players = []
    for name in names:
        role, pname = name.strip().split(":")
        if role == "human":
            players.append(HumanPlayer(pname))
        elif role == "ai":
            players.append(AIPlayer(pname))

    game = RussianRouletteGame(players)

    while len([player for player in players if player.is_alive()]) > 1:
        for player in players:
            if player.is_alive():
                print("*reloading the revolver*")
                player.take_turn(game)
                if not player.is_alive():
                    break

    winner = [player for player in players if player.is_alive()][0]
    print(f"\n {winner.get_name()} is the last one laughing!")

if __name__ == "__main__":
    main()