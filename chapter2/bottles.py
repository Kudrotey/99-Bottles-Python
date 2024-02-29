class Bottles():
    def verse(self, number_of_bottles):
        return f"{number_of_bottles} bottles of milk on the wall, " + \
               f"{number_of_bottles} bottles of milk.\n" + \
               f"Take one down and pass it around, " + \
               f"{number_of_bottles - 1} bottles of milk on the wall.\n"