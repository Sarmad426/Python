"""
Python Car Game
"""

import sys


class CarGame:
    """
    Car Game class
    """

    commands: tuple[str, str, str, str] = ("start", "stop", "exit", "help")
    states = (True, False)

    def __init__(self) -> None:
        self.started: bool = False
        self.stopped: bool = True

    def start_game(self):
        while True:
            command = input(":> ").strip()
            if command in CarGame.commands:
                if command == "start":
                    self.start_car(self.started)
                elif command == "stop":
                    self.stop_car(self.stopped)
                elif command == "help":
                    self.help()
                else:
                    sys.exit("Game Terminated: ")
            else:
                print("Invalid command! ")
                self.help()

    def start_car(self, started: bool):
        if started:
            print("Car already started: ")
        else:
            self.started, self.stopped = CarGame.states
            print("Car started: ")

    def stop_car(self, stopped: bool):
        if stopped:
            print("Car already stopped: ")
        else:
            self.stopped, self.started = CarGame.states
            print("Car stopped: ")

    def help(self) -> None:
        print("start: to start the car\nstop: to stop the car\nexit: to exit the game")


def main():
    car = CarGame()

    car.start_game()


if __name__ == "__main__":
    main()
