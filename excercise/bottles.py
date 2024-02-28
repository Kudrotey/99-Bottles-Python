class Bottles():
    
    def verse(self, n):
        return self.sentence(n).capitalize() + ", " + \
        self.sentence(n, is_on_the_wall=False) + ".\n" + \
        self.third_line(n) + \
        self.sentence(n - 1, is_last=True) + ".\n"

    def verses(self, upper, lower):
        result = ''
        for n in range(upper, lower-1, -1):
            result += self.verse(n) + "\n"
        return result

    def song(self):
        self.verses(99, 0)

    # private

    def sentence(self, n, is_last=False, is_on_the_wall=True):
        return self.count(n) + self.bottles(n) + ' of beer' + self.on_the_wall(is_on_the_wall)

    def count(self, n):
        if n > 0:
            return str(n)
        elif n == -1:
            return str(99)
        else:
            return 'no more'

    def bottles(self, n):
        if self.singular(n):
            return ' bottle'
        else:
            return ' bottles'

    def singular(self, n):
        return n == 1

    def on_the_wall(self, is_on_the_wall):
        if is_on_the_wall:
            return ' on the wall'
        else:
            return ''

    def how_many(self, n):
        if self.singular(n):
            return 'it'
        else:
            return 'one'

    def third_line(self, n):
        if n == 0:
            return "Go to the store and buy some more, "
        else:
            return f"Take {self.how_many(n)} down and pass it around, "