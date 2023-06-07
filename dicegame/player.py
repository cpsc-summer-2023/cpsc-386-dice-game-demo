"""A class defining a player."""

from locale import currency, setlocale, LC_ALL


class Player:
    """A human player and a player base class."""

    def __init__(self, nid, name, bankroll=100):
        """Init a player with a numerical ID, a name, and a bankroll."""
        self._id = nid
        self._name = name
        self._bankroll = bankroll
        self._current_roll = -1
        self._wager = -1
        setlocale(LC_ALL, '')

    @property
    def wager(self):
        """How much the player has wagered"""
        return self._wager

    @wager.setter
    def wager(self, val):
        """Set how much the player is wagering."""
        self._bankroll = self._bankroll - val
        self._wager = val

    @property
    def current_roll(self):
        """The current value of the dice roll."""
        return self._current_roll

    @current_roll.setter
    def current_roll(self, val):
        """Change the object's memory of what occured."""
        self._current_roll = val

    @property
    def pid(self):
        """The player's ID"""
        return self._id

    @property
    def name(self):
        """The player's name."""
        return self._name

    @property
    def bankroll(self):
        """The current bankroll formattted."""
        return currency(self._bankroll, grouping=True)

    @bankroll.setter
    def bankroll(self, val):
        """A setter to change the bankroll"""
        self._bankroll += val

    def is_ai(self):
        """A helper to identify if the player is a robot or not."""
        return False

    def __str__(self):
        """Convert the player to a string."""
        return self._name

    def __repr__(self):
        """Show the objects representation"""
        return 'Player({}, \'{}\', {})'.format(
            self._id, self._name, self._bankroll
        )


class RobotPlayer(Player):
    """A robot player to play the dice game."""

    def __init__(self, nid, name, bankroll=100):
        """The initializer."""
        super().__init__(nid, name, bankroll)

    def is_ai(self):
        """A helper to identify if the player is a robot or not."""
        return True
