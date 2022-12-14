"""
This is the main file to start the game
"""

from game_exceptions import GameOver, EnemyDown, InvalidInput
from models import Player, Enemy
from settings import GameOptions


def play():
    """
    This is a function without parameters that starts the game process.
    """
    while True:
        username = input("Enter your name: ")
        if len(username.strip()):
            break
        print("\nInvalid input \n" "You must enter your name")
    while True:
        try:
            action = GameOptions.commands(input('Enter command: '))
            if action == "start":
                break
        except InvalidInput:
            print("\nInvalid input")
    player = Player(username)
    level = 1
    enemy_obj = Enemy(level)
    while True:
        try:
            print()
            player.attack(enemy_obj)
            print()
            player.defence(enemy_obj)
        except EnemyDown:
            player.score += GameOptions.player_score_level_up
            level += 1
            enemy_obj = Enemy(level)
            print(f"\nLevel {level}")


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        GameOver.save_game_result()
        print("\nGame Over")
    except KeyboardInterrupt:
        pass
    finally:
        print("\nGood bye!")
