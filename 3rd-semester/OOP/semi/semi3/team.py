class Player:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, (int)):
            raise TypeError(f'{type(new_age).__name__} is not int')
        if new_age <= 0:
            raise ValueError(f'{new_age} < 0. Челик еще не родился :( :(. У него еще все в будущем!!')
        self._age = new_age

class PlayerIsNotAdultError(Exception):
    pass

class Team:
    def __init__(self, players: list[Player]) -> None:
        self.players = players

    @property
    def players(self) -> list[Player]:
        return self._players
    
    @players.setter
    def players(self, new_players: list[Player]) -> None:
        if not isinstance(new_players,list):
            raise TypeError(f'{type(new_players).__name__} is not list')
        if len(new_players) != 11:
            raise ValueError(f'{new_players} is not equal 11. Иди ищи команду дальше Ka4ok Kaba4ok')
        for player in new_players:
            if not isinstance(player,Player):
                raise TypeError(f'{type(new_players).__name__} is not Player')
            if player.age < 18:
                raise PlayerIsNotAdultError(f'Player: {player.name}, Age: {player.age} < 18')
        self._new_players = new_players
            

player = Player('Bimbimbambam', 15)
player1 = Player('Bimbambambam', 17)
player2 = Player('Bambambambam', 1234567890)
        