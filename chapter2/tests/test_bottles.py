from ..bottles import Bottles


def test_the_first_verse():
    expected = "99 bottles of milk on the wall, " + \
               "99 bottles of milk.\n" + \
               "Take one down and pass it around, " + \
               "98 bottles of milk on the wall.\n"
    actual = Bottles().verse(99)        
    assert expected == actual
    
    
def test_another_verse():
    expected = "3 bottles of milk on the wall, " + \
               "3 bottles of milk.\n" + \
               "Take one down and pass it around, " + \
               "2 bottles of milk on the wall.\n"
    actual = Bottles().verse(3)        
    assert expected == actual
    
    
def test_verse_2():
    expected = "2 bottles of milk on the wall, " + \
               "2 bottles of milk.\n" + \
               "Take one down and pass it around, " + \
               "1 bottle of milk on the wall.\n"
    actual = Bottles().verse(2)        
    assert expected == actual