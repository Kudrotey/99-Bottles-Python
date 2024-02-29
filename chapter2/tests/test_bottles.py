from ..bottles import Bottles

def test_the_first_verse():
    expected = "99 bottles of milk on the wall, " + \
               "99 bottles of milk.\n" + \
               "Take one down and pass it around, " + \
               "98 bottles of milk on the wall.\n"
    actual = Bottles().verse(99)        
    assert expected == actual