"""
    Number guess game

    : A user have maximum of 3 attempts.
    : user get points based on the number of attempt on which they have guessed it correct
"""

import random
import sys


class GuessGame:
    """
    Guess Game Class

    Checks the guess and assign points

    methods:
    - check_guess(user_guess:int) -> bool: Checks the user guess and calls the `update_points` function
    - update_points() -> None: Update the user points according to the guess
    """

    def __init__(self):
        self.GUESS_LIMIT = 3
        # random guess value (constant)
        self.GUESS_NUM = random.randint(1, 5)
        self.guess_count = 0
        self.points = 0
        print(self.GUESS_NUM)

    def input_guess(self) -> None:
        """
        Takes user guess as input and returns the result

        No Parameters:\n
        Returns nothing

        if guess is correct, it exits the program with the user message

        Otherwise it keeps asking for guess input until 3 attempts
        """
        while self.guess_count < self.GUESS_LIMIT:
            self.guess_count += 1
            user_guess: int = int(input("Guess: "))
            guess: bool = self.check_guess(user_guess)
            if guess:
                self.points = self.update_points(self.guess_count)
                sys.exit(
                    f"You won \nattempts: {self.guess_count}\nPoints: {self.points}"
                )
            elif self.guess_count == 3:
                sys.exit("You Lose: ")
            else:
                print("Incorrect guess!")

    def check_guess(self, user_guess: int) -> bool:
        """
        Checks the guess and returns a boolean

        Parameter:
        - user_guess (int): input Guess value

        Return:
        - boolean: if guess is correct returns `True` otherwise returns `False`
        """
        return user_guess == self.GUESS_NUM

    def update_points(self, guess_count: int) -> int:
        """
        Updates the points based on the guess attempt

        Parameters:
        - guess_count (int) : attempts made by user

        Returns:
        points (int): number of points earned by the user
        """
        if guess_count == 1:
            return 15
        elif guess_count == 2:
            return 10
        return 5

    def __str__(self):
        return "Guess game with 3 guess attempts. Hint (1-10)"


def main():
    """
    Main function

    Creates `Guess_Game` class instance and calls the `input_guess` method
    """
    game = GuessGame()

    game.input_guess()


if __name__ == "__main__":
    main()
