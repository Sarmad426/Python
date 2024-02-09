"""
Python Car Game

    - Start the car
    - Stop the car
    - Exit the game

    Active start and stop states with user-friendly console messages.
"""

import sys


class CarGame:
    """
    Car Game class

    - Start the car
    - Stop the car
    - Exit the game

    Active start and stop states with user-friendly console messages.
    """

    commands: tuple[str, str, str, str] = ("start", "stop", "exit", "help")
    states = (True, False)

    def __init__(self) -> None:
        self.started: bool = False
        self.stopped: bool = True

    def start_game(self) -> None:
        """
        Starts the game

        No Parameters:\n
        Returns nothing:

        Prompts the user to enter command infinitely

        if command is valid it calls the function accordingly
        """
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
        """
        Starts the car by switching the states

        Parameters:
        - started (bool):

        Returns Nothing
        """
        if started:
            print("Car already started: ")
        else:
            self.started, self.stopped = CarGame.states
            print("Car started: ")

    def stop_car(self, stopped: bool):
        """
        Stops the car by switching the states

        Parameters:
        - stopped (bool):

        Returns Nothing
        """
        if stopped:
            print("Car already stopped: ")
        else:
            self.stopped, self.started = CarGame.states
            print("Car stopped: ")

    def help(self) -> None:
        """
        Prints the help message, list of commands
        """
        print("start: to start the car\nstop: to stop the car\nexit: to exit the game")


def main():
    """
    Main function

    - Creates a `CarGame` class object
    - starts the game
    """
    car = CarGame()

    car.start_game()


if __name__ == "__main__":
    main()
