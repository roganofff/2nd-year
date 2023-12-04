from typing import Self


class Curses:
    words = 'php', 'javafx', 'windows', 'microsoft', 'чечевица'

class Beautifier:
    def __init__(self, text: str) -> None:
        self._text = text

    def entitler(self) -> Self:
        self._text = self._text.title()
        return self

    def censor(self) -> Self:
        self._text = self._text.lower()
        for word in Curses.words:
            if len(word) > 2:
                filler = '*' * (len(word) - 2)
                new = f'{word[0]}{filler}{word[-1]}'
            else:
                new = '*' * len(word)

            self._text = self._text.replace(word, new)
        return self

    def dot(self) -> Self:
        self._text = f'{self._text}.' if self._text[-1] != '.' else self._text
        return self
    
    def beautified(self) -> str:  # CHAIN
        return self.censor().entitler().dot()._text
    

print(Beautifier('php is much more easier than JavaFX if you\'re using Windows').beautified())
