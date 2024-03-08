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
        match number:
            case 0:
                return f"{self.quantity(number).capitalize()} {self.container(number)} of milk on the wall, " + \
                       f"{self.quantity(number)} {self.container(number)} of milk.\n" + \
                       f"{self.action(number)}, " + \
                       f"99 bottles of milk on the wall.\n"
            case _:
                return f"{self.quantity(number).capitalize()} {self.container(number)} of milk on the wall, " + \
                       f"{self.quantity(number)} {self.container(number)} of milk.\n" + \
                       f"{self.action(number)}, " + \
                       f"{self.quantity(number - 1)} {self.container(number - 1)} of milk on the wall.\n"
                       
    def container(self, number:int) -> str:
        if number == 1:
            return 'bottle'
        return 'bottles'
    
    def pronoun(self, number:int) -> str:
        if number == 1:
            return 'it'
        return 'one'
    
    def quantity(self, number:int) -> str:
        if number == 0:
            return 'no more'
        return str(number)
    
    def action(self, number:int) -> str:
        if number == 0:
            return "Go to the store and buy some more"
        return f"Take {self.pronoun(number)} down and pass it around"