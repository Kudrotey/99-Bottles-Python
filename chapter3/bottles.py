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
                return "No more bottles of milk on the wall, " + \
                       "no more bottles of milk.\n" + \
                       "Go to the store and buy some more, " + \
                       "99 bottles of milk on the wall.\n"
            case 1:
                return f"1 bottle of milk on the wall, " + \
                       f"1 bottle of milk.\n" + \
                       f"Take it down and pass it around, " + \
                       f"no more bottles of milk on the wall.\n"
            case _:
                return f"{number} {self.container(number)} of milk on the wall, " + \
                       f"{number} {self.container(number)} of milk.\n" + \
                       f"Take one down and pass it around, " + \
                       f"{number - 1} {self.container(number - 1)} of milk on the wall.\n"
                       
    def container(self, number:int) -> str:
        if number == 1:
            return 'bottle'
        return 'bottles'
                       