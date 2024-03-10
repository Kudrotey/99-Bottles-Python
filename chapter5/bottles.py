class Bottles():
    def song(self) -> str:
        return self.verses(99,0)
    
    def verses(self, upper:int, lower:int) -> str:
        result = ''
        for n in range(upper, lower-1, -1):
            result += self.verse(n) + "\n"
        result = result[:-1]
        return result
    
    def verse(self, number:int) -> str:
        return f"{self.quantity(number).capitalize()} {self.container(number)} of milk on the wall, " + \
                f"{self.quantity(number)} {self.container(number)} of milk.\n" + \
                f"{self.action(number)}, " + \
                f"{self.quantity(self.successor(number))} {self.container(self.successor(number))} of milk on the wall.\n"
                       
    def container(self, number:int) -> str:
        return BottleNumber(number).container()
    
    def pronoun(self, number:int) -> str:
        return BottleNumber(number).pronoun()
    
    def quantity(self, number:int) -> str:
        return BottleNumber(number).quantity()
    
    def action(self, number:int) -> str:
        return BottleNumber(number).action()
    
    def successor(self, number:int) -> int:
        return BottleNumber(number).successor()
    
class BottleNumber():
    def __init__(self, number:int) -> None:
        self.number = number
        
    def container(self) -> str:
        if self.number == 1:
            return 'bottle'
        return 'bottles'
    
    def pronoun(self) -> str:
        if self.number == 1:
            return 'it'
        return 'one'
    
    def quantity(self) -> str:
        if self.number == 0:
            return 'no more'
        return str(self.number)
    
    def action(self) -> str:
        if self.number == 0:
            return "Go to the store and buy some more"
        return f"Take {self.pronoun()} down and pass it around"
    
    def successor(self) -> int:
        if self.number == 0:
            return 99
        return self.number - 1