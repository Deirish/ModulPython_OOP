from datetime import datetime as dt


class GameOver(Exception):

    def __init__(self, players):
        self.players = players
        self.game_result()
        self.save_game_result()

    def game_result(self):
        """
        This method prints the result of the game
        """
        print(f"\nPLAYER --> {self.players.name}\n"
              f"SCORE --> {self.players.score}\n")

    def save_game_result(self):
        """
        This method writes the result of the game to a file
        """
        now = dt.today()
        result = [self.players.name, f"{now:%d-%m_%Y}", str(self.players.score)]
        with open("scores.txt", "a+", encoding="utf-8") as file:
            file.write("|".join(result) + '\n')
            file.seek(0)
            result = sorted([line.split("|")[1:] for line in file], key=lambda x: int(x[3]), reverse=True)

        with open("scores.txt", "w", encoding="utf-8") as file:
            for num, players in enumerate(result, 1):
                if num < 11:
                    file.write(f"{num}. |" + '|'.join(players))


class EnemyDown(Exception):
    pass


class InvalidInput(Exception):
    pass
