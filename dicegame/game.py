""" A game where a human player and a robot player take turns rolling a die."""


from dicegame.player import Player, RobotPlayer
from dicegame.die import SixSidedDie


class DiceGame:
    """A simple game of dice. Whoever has the highest wins."""

    def __init__(self):
        """Init. the dice game."""
        self._is_game_over = False
        self._players = [Player(10, 'Tuffy', 100000)]

        self._robots = [RobotPlayer(20, 'SkyNet')]

        self._all_particpants = self._players + self._robots
        # A pair of dice
        self._dice = [SixSidedDie() for _ in range(2)]

    def run(self):
        """The game loop"""
        while not self._is_game_over:
            for player in self._all_particpants:
                if player.is_ai():
                    print(f'The robot {player} will wager $10')
                    player.wager = 10
                else:
                    player.wager = int(
                        input('How much do you want to wager?> ')
                    )
            for player in self._all_particpants:
                print(f'{player} rolls the dice...')
                die_sum = 0
                for n, die in enumerate(self._dice):
                    val = die.roll()
                    print(f'Roll {n} is a {val}!')
                    die_sum += val
                player.current_roll = die_sum
            winner = max(self._all_particpants, key=lambda p: p.current_roll)
            print(f'The winner is {winner}!')
            winner.bankroll = winner.wager * 2
            for player in self._all_particpants:
                player.wager = 0
                print(repr(player))
            answer = input('Do you want to play again? (y/n)> ')
            if answer != 'y':
                self._is_game_over = True

        return 0
