""" Classes to represent various sided dice """
from random import randint


class Die:
    """N-sided die labeled with minimum to maximum values."""

    def __init__(self, number_of_sides, minimum, maximum):
        """Initialize an N sided die with numbers between minimum and maximum."""
        self._min = minimum
        self._max = maximum
        self._num_sides = number_of_sides
        if (self._max - self._min) != (number_of_sides - 1):
            print("Warning: number of sides does not match the min and max.")

    def roll(self):
        """Roll the die and return the value"""
        return randint(self._min, self._max)


class SixSidedDie(Die):
    """6 sided die with values from 1 to 6"""

    def __init__(self):
        super().__init__(6, 1, 6)
