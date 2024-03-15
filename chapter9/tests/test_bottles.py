from ..bottles import CountdownSong
from ..bottles import BottleNumber,BottleNumber0, BottleNumber1, BottleNumber6
from ..bottles import BottleVerse

class FakeVerse:
    @classmethod
    def get_lyrics(cls, number:int) -> str:
        return f"This is verse {number}.\n"

class TestCountdownSong:
    def test_verse(self):
        expected = "This is verse 132.\n"
        
        assert expected == CountdownSong(FakeVerse).verse(132)
        
    def test_verses(self):
        expected = "This is verse 99.\n" + \
                   "\n" + \
                   "This is verse 98.\n" + \
                   "\n" + \
                   "This is verse 97.\n"
        
        assert expected == CountdownSong(FakeVerse).verses(99, 97)
    
    def test_song(self):
        expected = "This is verse 54.\n" + \
                   "\n" + \
                   "This is verse 53.\n" + \
                   "\n" + \
                   "This is verse 52.\n" + \
                   "\n" + \
                   "This is verse 51.\n" + \
                   "\n" + \
                   "This is verse 50.\n"
                   
        assert expected == CountdownSong(
                                         FakeVerse, 
                                         max_verse=54, 
                                         min_verse=50
                                        ).song()
        
        
class TestBottleNumber:
    def test_factory_returns_correct_class_for_given_number(self):
        assert BottleNumber0 == type(BottleNumber.for_(0))
        assert BottleNumber1 == type(BottleNumber.for_(1))
        assert BottleNumber6 == type(BottleNumber.for_(6))
        
        assert BottleNumber == type(BottleNumber.for_(86))
        assert BottleNumber == type(BottleNumber.for_(7))
        

class TestBottleVerse:
    def test_verse_general_rule_upper_bound(self):
        expected = "99 bottles of milk on the wall, " + \
                "99 bottles of milk.\n" + \
                "Take one down and pass it around, " + \
                "98 bottles of milk on the wall.\n"
        
        assert expected == BottleVerse.get_lyrics(99)
        
    def test_verse_general_rule_lower_bound(self):
        expected = "3 bottles of milk on the wall, " + \
                "3 bottles of milk.\n" + \
                "Take one down and pass it around, " + \
                "2 bottles of milk on the wall.\n"
        
        assert expected == BottleVerse.get_lyrics(3)  
        
    def test_verse_2(self):
        expected = "2 bottles of milk on the wall, " + \
                "2 bottles of milk.\n" + \
                "Take one down and pass it around, " + \
                "1 bottle of milk on the wall.\n"
        
        assert expected == BottleVerse.get_lyrics(2)
        
    def test_verse_1(self):
        expected = "1 bottle of milk on the wall, " + \
                "1 bottle of milk.\n" + \
                "Take it down and pass it around, " + \
                "no more bottles of milk on the wall.\n"
        
        assert expected == BottleVerse.get_lyrics(1)
        
    def test_verse_0(self):
        expected = "No more bottles of milk on the wall, " + \
                "no more bottles of milk.\n" + \
                "Go to the store and buy some more, " + \
                "99 bottles of milk on the wall.\n"
        
        assert expected == BottleVerse.get_lyrics(0)
        
    def test_verse_7(self):
        expected = "7 bottles of milk on the wall, " + \
                   "7 bottles of milk.\n" + \
                   "Take one down and pass it around, " + \
                   "1 six-pack of milk on the wall.\n"
                    
        assert expected == BottleVerse.get_lyrics(7)
        
    def test_verse_6(self):
        expected = "1 six-pack of milk on the wall, " + \
                   "1 six-pack of milk.\n" + \
                   "Take one down and pass it around, " + \
                   "5 bottles of milk on the wall.\n"
                    
        assert expected == BottleVerse.get_lyrics(6)