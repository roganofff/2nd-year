from abc import ABC, abstractmethod
from typing import Self


class State(ABC):
    @abstractmethod
    def play(self) -> str:
        pass

class Ready(State):
    def play(self) -> str:
        return 'Ready to play'
    
class OnVacation(State):
    def play(self) -> str:
        return 'Cannot play, chilling'


class Player:
    def __init__(self, name: str, state: State = Ready()) -> None:
        self.name, self.state = name, state

    def play(self) -> None:
        print(f'{self.name} is playing...')

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: State):
        if not isinstance(state, State):
            raise TypeError(f'State is not State type.')
        self._state = state

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} is {self._state.play()}'

class Team:
    def __init__(self, title: str, players: list[Player]) -> None:
        self.title = title
        self.players = players
        self._set_state()
        self.__cnt = 0

    @property
    def players(self):
        return self.players
    
    @staticmethod
    def check_player(new_player) -> None:
        if not isinstance(new_player, Player):
            raise TypeError(f'Expected player to be type of Player, not {type(new_player).__name__}')

    @players.setter
    def players(self, new_players: list[Player]) -> None:
        for player in new_players:
            self.check_player(player)
        self._players = new_players

    def add_player(self, new_player: Player) -> None:
        if not new_player in self._players:
            self.check_player(new_player)
            self._players.append(new_player)
        else:
            raise ValueError(f'Player {new_player} already exists in {self.title}.')
    
    def remove_player(self, player):
        if player in self._players:
            self._players.remove(player)
        else:
            raise ValueError(f'Player {player} does not exist in {self.title}.')
            
    def play(self) -> None:
        for player in self._players:
            player.play()

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Player:
        if self.__cnt >= len(self._players):
            self.__cnt = 0
            raise StopIteration()
        self.__cnt += 1
        return self._players[self.__cnt - 1]
    
    def _set_state(self) -> None:
        self._state = [player.__dict__.copy() for player in self._players]
    
    def _get_state(self) -> list[dict]:
        return self._state
    
    def _reset(self) -> None:
        self._players = [Player(name=player['name'], state=player['_state']) for player in self._state]

players = [
    Player('Slavik'),
    Player('Dayana'),
    Player('Egor')
]
sirius_team = Team('Siriusly', players)

sirius_team.remove_player(players[1])
sirius_team.play()

sirius_team._reset()
sirius_team.play()