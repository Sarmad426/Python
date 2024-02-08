"""
Python Car Game
"""

import sys


class CarGame:
    """
    Car Game class
    """

    commands: tuple[str, str, str, str] = ("start", "stop", "exit", "help")

    def __init__(self) -> None:
        self.started: bool = False
        self.stopped: bool = True

    def start_game(self):
        states = (True, False)
        while True:
            command = input(":> ")
            if command in CarGame.commands:
                if command == "start":
                    if self.started:
                        print("Car already started: ")
                    else:
                        self.started, self.stopped = states
                        print("Car Started: ")
                elif command == "stop":
                    if self.stopped:
                        print("Car already stopped: ")
                    else:
                        self.stopped, self.started = states
                        print("Car Stopped:")
                elif command == "help":
                    print(
                        "start: to start the car\nstop: to stop the car\nexit: to exit the game"
                    )
                else:
                    sys.exit("Game Terminated: ")
            else:
                print("Invalid command! ")


def main():
    car = CarGame()

    car.start_game()


if __name__ == "__main__":
    main()
