from random import randint
from settings import GameOptions
from game_exceptions import EnemyDown, GameOver, InvalidInput
from settings import PLAYER_LIVES


class Enemy:
    """
    This class contains the methods of the enemy object.
    """

    def __init__(self, level: int):
        self.level = level
        self.lives = self.level * GameOptions.enemy_lives

    @staticmethod
    def select_attack():
        rand = randint(1, 3)
        return rand

    def decrease_lives(self):
        """
        Reduces the number of lives by 1. When life becomes 0, throws an EnemyDown exception.
        """
        self.lives -= 1
        if not self.lives:
            raise EnemyDown


class Player:

    lives = PLAYER_LIVES
    score = 0
    allowed_attacks = (1, 2, 3)

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def fight(attack, defense):
        """
        This method calls attack/defend result
        """
        result = attack - defense
        if result in (-1, 2):
            return 1
        if result in (-2, 1):
            return -1
        return 0

    def decrease_lives(self):
        """
        Reduces the number of lives by 1. When life becomes 0, throws an GameOver exception.
        """
        self.lives -= 1
        if not self.lives:
            raise GameOver(self)

    def choice_validation(self, choice: str) -> int:
        if choice.isdigit():
            if int(choice) in self.allowed_attacks:
                return int(choice)
        print("\nInvalid input \n"
              "You must choice one of the following characters:\n"
              "1 -> WIZARD\n"
              "2 -> WARRIOR\n"
              "3 -> ROBBER")
        raise InvalidInput

    def attack(self, enemy_obj):
        """
        This method prints a message to the console
        about the result of the attack.
        """
        while True:
            try:
                attack = self.choice_validation(input("Enter attack: "))
                break
            except InvalidInput:
                pass
        defence = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            self.score += GameOptions.player_score
            print("You attacked successfully!")
        if result == -1:
            print("You missed!")

    def defence(self, enemy_obj):
        """
        This method prints a message about the result
        of protection to the console.
        """
        while True:
            try:
                defence = self.choice_validation(input("Enter defence: "))
                break
            except InvalidInput:
                pass
        attack = enemy_obj.select_attack()
        result = self.fight(defence, attack)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            print("You missed!")
            self.decrease_lives()
        if result == -1:
            print("You attacked successfully!")