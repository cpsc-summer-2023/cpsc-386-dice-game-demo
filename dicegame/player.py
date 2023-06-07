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
        return self._wager

    @wager.setter
    def wager(self, val):
        self._bankroll = self._bankroll - val
        self._wager = val

    @property
    def current_roll(self):
        return self._current_roll

    @current_roll.setter
    def current_roll(self, val):
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
        return currency(self._bankroll, grouping=True)

    @bankroll.setter
    def bankroll(self, val):
        self._bankroll += val

    def is_AI(self):
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
    def __init__(self, nid, name, bankroll=100):
        super().__init__(nid, name, bankroll)

    def is_AI(self):
        """A helper to identify if the player is a robot or not."""
        return True
