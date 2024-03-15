from ..bottles import Bottles
from ..bottles import BottleNumber,BottleNumber0, BottleNumber1, BottleNumber6
from ..bottles import BottleVerse

class TestBottles:
    def test_the_first_two_verses(self):
        expected = "99 bottles of milk on the wall, " + \
                "99 bottles of milk.\n" + \
                "Take one down and pass it around, " + \
                "98 bottles of milk on the wall.\n" + \
                "\n" + \
                "98 bottles of milk on the wall, " + \
                "98 bottles of milk.\n" + \
                "Take one down and pass it around, " + \
                "97 bottles of milk on the wall.\n"

        assert expected == Bottles().verses(99,98)

    def test_the_last_three_verses(self):
        expected = "2 bottles of milk on the wall, " + \
                "2 bottles of milk.\n" + \
                "Take one down and pass it around, " + \
                "1 bottle of milk on the wall.\n" + \
                "\n" + \
                "1 bottle of milk on the wall, " + \
                "1 bottle of milk.\n" + \
                "Take it down and pass it around, " + \
                "no more bottles of milk on the wall.\n" + \
                "\n" + \
                "No more bottles of milk on the wall, " + \
                "no more bottles of milk.\n" + \
                "Go to the store and buy some more, " + \
                "99 bottles of milk on the wall.\n"

        assert expected == Bottles().verses(2,0)

    def test_the_whole_song(self):
        expected = \
            "99 bottles of milk on the wall, 99 bottles of milk.\n" + \
            "Take one down and pass it around, 98 bottles of milk on the wall.\n\n" + \
            "98 bottles of milk on the wall, 98 bottles of milk.\n" + \
            "Take one down and pass it around, 97 bottles of milk on the wall.\n\n" + \
            "97 bottles of milk on the wall, 97 bottles of milk.\n" + \
            "Take one down and pass it around, 96 bottles of milk on the wall.\n\n" + \
            "96 bottles of milk on the wall, 96 bottles of milk.\n" + \
            "Take one down and pass it around, 95 bottles of milk on the wall.\n\n" + \
            "95 bottles of milk on the wall, 95 bottles of milk.\n" + \
            "Take one down and pass it around, 94 bottles of milk on the wall.\n\n" + \
            "94 bottles of milk on the wall, 94 bottles of milk.\n" + \
            "Take one down and pass it around, 93 bottles of milk on the wall.\n\n" + \
            "93 bottles of milk on the wall, 93 bottles of milk.\n" + \
            "Take one down and pass it around, 92 bottles of milk on the wall.\n\n" + \
            "92 bottles of milk on the wall, 92 bottles of milk.\n" + \
            "Take one down and pass it around, 91 bottles of milk on the wall.\n\n" + \
            "91 bottles of milk on the wall, 91 bottles of milk.\n" + \
            "Take one down and pass it around, 90 bottles of milk on the wall.\n\n" + \
            "90 bottles of milk on the wall, 90 bottles of milk.\n" + \
            "Take one down and pass it around, 89 bottles of milk on the wall.\n\n" + \
            "89 bottles of milk on the wall, 89 bottles of milk.\n" + \
            "Take one down and pass it around, 88 bottles of milk on the wall.\n\n" + \
            "88 bottles of milk on the wall, 88 bottles of milk.\n"  + \
            "Take one down and pass it around, 87 bottles of milk on the wall.\n\n" + \
            "87 bottles of milk on the wall, 87 bottles of milk.\n" + \
            "Take one down and pass it around, 86 bottles of milk on the wall.\n\n" + \
            "86 bottles of milk on the wall, 86 bottles of milk.\n" + \
            "Take one down and pass it around, 85 bottles of milk on the wall.\n\n" + \
            "85 bottles of milk on the wall, 85 bottles of milk.\n" + \
            "Take one down and pass it around, 84 bottles of milk on the wall.\n\n" + \
            "84 bottles of milk on the wall, 84 bottles of milk.\n" + \
            "Take one down and pass it around, 83 bottles of milk on the wall.\n\n" + \
            "83 bottles of milk on the wall, 83 bottles of milk.\n" + \
            "Take one down and pass it around, 82 bottles of milk on the wall.\n\n" + \
            "82 bottles of milk on the wall, 82 bottles of milk.\n" + \
            "Take one down and pass it around, 81 bottles of milk on the wall.\n\n" + \
            "81 bottles of milk on the wall, 81 bottles of milk.\n" + \
            "Take one down and pass it around, 80 bottles of milk on the wall.\n\n" + \
            "80 bottles of milk on the wall, 80 bottles of milk.\n" + \
            "Take one down and pass it around, 79 bottles of milk on the wall.\n\n" + \
            "79 bottles of milk on the wall, 79 bottles of milk.\n" + \
            "Take one down and pass it around, 78 bottles of milk on the wall.\n\n" + \
            "78 bottles of milk on the wall, 78 bottles of milk.\n" + \
            "Take one down and pass it around, 77 bottles of milk on the wall.\n\n" + \
            "77 bottles of milk on the wall, 77 bottles of milk.\n" + \
            "Take one down and pass it around, 76 bottles of milk on the wall.\n\n" + \
            "76 bottles of milk on the wall, 76 bottles of milk.\n" + \
            "Take one down and pass it around, 75 bottles of milk on the wall.\n\n" + \
            "75 bottles of milk on the wall, 75 bottles of milk.\n" + \
            "Take one down and pass it around, 74 bottles of milk on the wall.\n\n" + \
            "74 bottles of milk on the wall, 74 bottles of milk.\n" + \
            "Take one down and pass it around, 73 bottles of milk on the wall.\n\n" + \
            "73 bottles of milk on the wall, 73 bottles of milk.\n" + \
            "Take one down and pass it around, 72 bottles of milk on the wall.\n\n" + \
            "72 bottles of milk on the wall, 72 bottles of milk.\n" + \
            "Take one down and pass it around, 71 bottles of milk on the wall.\n\n" + \
            "71 bottles of milk on the wall, 71 bottles of milk.\n" + \
            "Take one down and pass it around, 70 bottles of milk on the wall.\n\n" + \
            "70 bottles of milk on the wall, 70 bottles of milk.\n" + \
            "Take one down and pass it around, 69 bottles of milk on the wall.\n\n" + \
            "69 bottles of milk on the wall, 69 bottles of milk.\n" + \
            "Take one down and pass it around, 68 bottles of milk on the wall.\n\n" + \
            "68 bottles of milk on the wall, 68 bottles of milk.\n" + \
            "Take one down and pass it around, 67 bottles of milk on the wall.\n\n" + \
            "67 bottles of milk on the wall, 67 bottles of milk.\n" + \
            "Take one down and pass it around, 66 bottles of milk on the wall.\n\n" + \
            "66 bottles of milk on the wall, 66 bottles of milk.\n" + \
            "Take one down and pass it around, 65 bottles of milk on the wall.\n\n" + \
            "65 bottles of milk on the wall, 65 bottles of milk.\n" + \
            "Take one down and pass it around, 64 bottles of milk on the wall.\n\n" + \
            "64 bottles of milk on the wall, 64 bottles of milk.\n" + \
            "Take one down and pass it around, 63 bottles of milk on the wall.\n\n" + \
            "63 bottles of milk on the wall, 63 bottles of milk.\n" + \
            "Take one down and pass it around, 62 bottles of milk on the wall.\n\n" + \
            "62 bottles of milk on the wall, 62 bottles of milk.\n" + \
            "Take one down and pass it around, 61 bottles of milk on the wall.\n\n" + \
            "61 bottles of milk on the wall, 61 bottles of milk.\n" + \
            "Take one down and pass it around, 60 bottles of milk on the wall.\n\n" + \
            "60 bottles of milk on the wall, 60 bottles of milk.\n" + \
            "Take one down and pass it around, 59 bottles of milk on the wall.\n\n" + \
            "59 bottles of milk on the wall, 59 bottles of milk.\n" + \
            "Take one down and pass it around, 58 bottles of milk on the wall.\n\n" + \
            "58 bottles of milk on the wall, 58 bottles of milk.\n" + \
            "Take one down and pass it around, 57 bottles of milk on the wall.\n\n" + \
            "57 bottles of milk on the wall, 57 bottles of milk.\n" + \
            "Take one down and pass it around, 56 bottles of milk on the wall.\n\n" + \
            "56 bottles of milk on the wall, 56 bottles of milk.\n" + \
            "Take one down and pass it around, 55 bottles of milk on the wall.\n\n" + \
            "55 bottles of milk on the wall, 55 bottles of milk.\n" + \
            "Take one down and pass it around, 54 bottles of milk on the wall.\n\n" + \
            "54 bottles of milk on the wall, 54 bottles of milk.\n" + \
            "Take one down and pass it around, 53 bottles of milk on the wall.\n\n" + \
            "53 bottles of milk on the wall, 53 bottles of milk.\n" + \
            "Take one down and pass it around, 52 bottles of milk on the wall.\n\n" + \
            "52 bottles of milk on the wall, 52 bottles of milk.\n" + \
            "Take one down and pass it around, 51 bottles of milk on the wall.\n\n" + \
            "51 bottles of milk on the wall, 51 bottles of milk.\n" + \
            "Take one down and pass it around, 50 bottles of milk on the wall.\n\n" + \
            "50 bottles of milk on the wall, 50 bottles of milk.\n" + \
            "Take one down and pass it around, 49 bottles of milk on the wall.\n\n" + \
            "49 bottles of milk on the wall, 49 bottles of milk.\n" + \
            "Take one down and pass it around, 48 bottles of milk on the wall.\n\n" + \
            "48 bottles of milk on the wall, 48 bottles of milk.\n" + \
            "Take one down and pass it around, 47 bottles of milk on the wall.\n\n" + \
            "47 bottles of milk on the wall, 47 bottles of milk.\n" + \
            "Take one down and pass it around, 46 bottles of milk on the wall.\n\n" + \
            "46 bottles of milk on the wall, 46 bottles of milk.\n" + \
            "Take one down and pass it around, 45 bottles of milk on the wall.\n\n" + \
            "45 bottles of milk on the wall, 45 bottles of milk.\n" + \
            "Take one down and pass it around, 44 bottles of milk on the wall.\n\n" + \
            "44 bottles of milk on the wall, 44 bottles of milk.\n" + \
            "Take one down and pass it around, 43 bottles of milk on the wall.\n\n" + \
            "43 bottles of milk on the wall, 43 bottles of milk.\n" + \
            "Take one down and pass it around, 42 bottles of milk on the wall.\n\n" + \
            "42 bottles of milk on the wall, 42 bottles of milk.\n" + \
            "Take one down and pass it around, 41 bottles of milk on the wall.\n\n" + \
            "41 bottles of milk on the wall, 41 bottles of milk.\n" + \
            "Take one down and pass it around, 40 bottles of milk on the wall.\n\n" + \
            "40 bottles of milk on the wall, 40 bottles of milk.\n" + \
            "Take one down and pass it around, 39 bottles of milk on the wall.\n\n" + \
            "39 bottles of milk on the wall, 39 bottles of milk.\n" + \
            "Take one down and pass it around, 38 bottles of milk on the wall.\n\n" + \
            "38 bottles of milk on the wall, 38 bottles of milk.\n" + \
            "Take one down and pass it around, 37 bottles of milk on the wall.\n\n" + \
            "37 bottles of milk on the wall, 37 bottles of milk.\n" + \
            "Take one down and pass it around, 36 bottles of milk on the wall.\n\n" + \
            "36 bottles of milk on the wall, 36 bottles of milk.\n" + \
            "Take one down and pass it around, 35 bottles of milk on the wall.\n\n" + \
            "35 bottles of milk on the wall, 35 bottles of milk.\n" + \
            "Take one down and pass it around, 34 bottles of milk on the wall.\n\n" + \
            "34 bottles of milk on the wall, 34 bottles of milk.\n" + \
            "Take one down and pass it around, 33 bottles of milk on the wall.\n\n" + \
            "33 bottles of milk on the wall, 33 bottles of milk.\n" + \
            "Take one down and pass it around, 32 bottles of milk on the wall.\n\n" + \
            "32 bottles of milk on the wall, 32 bottles of milk.\n" + \
            "Take one down and pass it around, 31 bottles of milk on the wall.\n\n" + \
            "31 bottles of milk on the wall, 31 bottles of milk.\n" + \
            "Take one down and pass it around, 30 bottles of milk on the wall.\n\n" + \
            "30 bottles of milk on the wall, 30 bottles of milk.\n" + \
            "Take one down and pass it around, 29 bottles of milk on the wall.\n\n" + \
            "29 bottles of milk on the wall, 29 bottles of milk.\n" + \
            "Take one down and pass it around, 28 bottles of milk on the wall.\n\n" + \
            "28 bottles of milk on the wall, 28 bottles of milk.\n" + \
            "Take one down and pass it around, 27 bottles of milk on the wall.\n\n" + \
            "27 bottles of milk on the wall, 27 bottles of milk.\n" + \
            "Take one down and pass it around, 26 bottles of milk on the wall.\n\n" + \
            "26 bottles of milk on the wall, 26 bottles of milk.\n" + \
            "Take one down and pass it around, 25 bottles of milk on the wall.\n\n" + \
            "25 bottles of milk on the wall, 25 bottles of milk.\n" + \
            "Take one down and pass it around, 24 bottles of milk on the wall.\n\n" + \
            "24 bottles of milk on the wall, 24 bottles of milk.\n" + \
            "Take one down and pass it around, 23 bottles of milk on the wall.\n\n" + \
            "23 bottles of milk on the wall, 23 bottles of milk.\n" + \
            "Take one down and pass it around, 22 bottles of milk on the wall.\n\n" + \
            "22 bottles of milk on the wall, 22 bottles of milk.\n" + \
            "Take one down and pass it around, 21 bottles of milk on the wall.\n\n" + \
            "21 bottles of milk on the wall, 21 bottles of milk.\n" + \
            "Take one down and pass it around, 20 bottles of milk on the wall.\n\n" + \
            "20 bottles of milk on the wall, 20 bottles of milk.\n" + \
            "Take one down and pass it around, 19 bottles of milk on the wall.\n\n" + \
            "19 bottles of milk on the wall, 19 bottles of milk.\n" + \
            "Take one down and pass it around, 18 bottles of milk on the wall.\n\n" + \
            "18 bottles of milk on the wall, 18 bottles of milk.\n" + \
            "Take one down and pass it around, 17 bottles of milk on the wall.\n\n" + \
            "17 bottles of milk on the wall, 17 bottles of milk.\n" + \
            "Take one down and pass it around, 16 bottles of milk on the wall.\n\n" + \
            "16 bottles of milk on the wall, 16 bottles of milk.\n" + \
            "Take one down and pass it around, 15 bottles of milk on the wall.\n\n" + \
            "15 bottles of milk on the wall, 15 bottles of milk.\n" + \
            "Take one down and pass it around, 14 bottles of milk on the wall.\n\n" + \
            "14 bottles of milk on the wall, 14 bottles of milk.\n" + \
            "Take one down and pass it around, 13 bottles of milk on the wall.\n\n" + \
            "13 bottles of milk on the wall, 13 bottles of milk.\n" + \
            "Take one down and pass it around, 12 bottles of milk on the wall.\n\n" + \
            "12 bottles of milk on the wall, 12 bottles of milk.\n" + \
            "Take one down and pass it around, 11 bottles of milk on the wall.\n\n" + \
            "11 bottles of milk on the wall, 11 bottles of milk.\n" + \
            "Take one down and pass it around, 10 bottles of milk on the wall.\n\n" + \
            "10 bottles of milk on the wall, 10 bottles of milk.\n" + \
            "Take one down and pass it around, 9 bottles of milk on the wall.\n\n" + \
            "9 bottles of milk on the wall, 9 bottles of milk.\n" + \
            "Take one down and pass it around, 8 bottles of milk on the wall.\n\n" + \
            "8 bottles of milk on the wall, 8 bottles of milk.\n" + \
            "Take one down and pass it around, 7 bottles of milk on the wall.\n\n" + \
            "7 bottles of milk on the wall, 7 bottles of milk.\n" + \
            "Take one down and pass it around, 1 six-pack of milk on the wall.\n\n" + \
            "1 six-pack of milk on the wall, 1 six-pack of milk.\n" + \
            "Take one down and pass it around, 5 bottles of milk on the wall.\n\n" + \
            "5 bottles of milk on the wall, 5 bottles of milk.\n" + \
            "Take one down and pass it around, 4 bottles of milk on the wall.\n\n" + \
            "4 bottles of milk on the wall, 4 bottles of milk.\n" + \
            "Take one down and pass it around, 3 bottles of milk on the wall.\n\n" + \
            "3 bottles of milk on the wall, 3 bottles of milk.\n" + \
            "Take one down and pass it around, 2 bottles of milk on the wall.\n\n" + \
            "2 bottles of milk on the wall, 2 bottles of milk.\n" + \
            "Take one down and pass it around, 1 bottle of milk on the wall.\n\n" + \
            "1 bottle of milk on the wall, 1 bottle of milk.\n" + \
            "Take it down and pass it around, no more bottles of milk on the wall.\n\n" + \
            "No more bottles of milk on the wall, no more bottles of milk.\n" + \
            "Go to the store and buy some more, 99 bottles of milk on the wall.\n"

        assert expected == Bottles().song()
        
        
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