PLAYER_LIVES = 5
COMMANDS = ("start", "scores", "help", "exit")


class GameOptions:

   player_score = 1
   player_score_level_up = 5
   enemy_lives = 1

   @staticmethod
   def commands(command: str) -> str:
      command = command.strip().lower()
      if command in COMMANDS:
         return command
      if command == "scores":
         return GameOptions.score(command)
      if command == "help":
         return GameOptions.help(command)
      if command == "exit":
         return GameOptions.exit()

   @staticmethod
   def help(command: str) -> str:
      print("'Start'  --->>> enter to start game.\n"
            "'Scores'  --->>> enter to show scores.\n"
            "'Exit'  --->>> enter to exit the game.")
      return command

   @staticmethod
   def score(command: str) -> str:
      with open("scores.txt", encoding="utf-8") as file:
         for line in file:
            print(line)
      return command

   @staticmethod
   def exit():
      raise KeyboardInterrupt
