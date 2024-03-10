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
        bottle_number = BottleNumber(number)
        next_bottle_number = BottleNumber(bottle_number.successor())
        
        return f"{bottle_number.quantity().capitalize()} {bottle_number.container()} of milk on the wall, " + \
                f"{bottle_number.quantity()} {bottle_number.container()} of milk.\n" + \
                f"{bottle_number.action()}, " + \
                f"{next_bottle_number.quantity()} {next_bottle_number.container()} of milk on the wall.\n"
    
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