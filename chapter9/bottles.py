class CountdownSong():
    def __init__(self, verse_template=None, max_verse:int=99, min_verse:int=0) -> None:
        self.verse_template = \
            verse_template if verse_template is not None else BottleVerse
        self.max_verse = max_verse
        self.min_verse = min_verse
    def song(self) -> str:
        return self.verses(self.max_verse, self.min_verse)
    
    def verses(self, upper:int, lower:int) -> str:
        result = ''
        for n in range(upper, lower-1, -1):
            result += self.verse(n) + "\n"
        return result[:-1]
    
    def verse(self, number:int) -> str:
        return self.verse_template.get_lyrics(number)

class BottleVerse():
    def __init__(self, number) -> None:
        self.bottle_number = number
    
    @classmethod
    def get_lyrics(cls, number):
        return cls(BottleNumber.for_(number)).lyrics()
    
    def lyrics(self) -> str:
        return f"{self.bottle_number}".capitalize() + " of milk on the wall, " + \
               f"{self.bottle_number} of milk.\n" + \
               f"{self.bottle_number.action()}, " + \
               f"{self.bottle_number.successor()} of milk on the wall.\n"


class BottleNumber():
    def __init__(self, number:int) -> None:
        self.number = number
        
    def __str__(self) -> str:
        return f"{self.quantity()} {self.container()}"
    
    def container(self) -> str:
        return 'bottles'
    
    def pronoun(self) -> str:
        return 'one'
    
    def quantity(self) -> str:
        return str(self.number)
    
    def action(self) -> str:
        return f"Take {self.pronoun()} down and pass it around"
    
    def successor(self) -> int:
        return BottleNumber(self.number - 1).for_(self.number - 1)
    
    @classmethod
    def for_(cls, number:int):
        match number:
            case 0:
                return BottleNumber0(number)
            case 1:
                return BottleNumber1(number)
            case 6:
                return BottleNumber6(number)
            case _:
                return BottleNumber(number)
    
    
class BottleNumber0(BottleNumber):
    def quantity(self) -> str:
        return 'no more'
    
    def action(self) -> str:
        return "Go to the store and buy some more"
    
    def successor(self) -> int:
        return BottleNumber(self.number).for_(99)
    

class BottleNumber1(BottleNumber):
    def container(self) -> str:
        return 'bottle'
    
    def pronoun(self) -> str:
        return 'it'
    

class BottleNumber6(BottleNumber):
    def container(self) -> str:
        return 'six-pack'
    
    def quantity(self) -> str:
        return '1'
