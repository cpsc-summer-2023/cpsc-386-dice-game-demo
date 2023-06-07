""" A made up dice game to show how to organize a project. """

import sys
from dicegame import game


def main():
    """Game entry point; all the code is in the directory dicegame."""
    sys.exit(game.DiceGame().run())


if __name__ == '__main__':
    main()
