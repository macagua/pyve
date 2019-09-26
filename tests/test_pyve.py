""" PyTest tests """

from pyve import MESSAGE, Community

pyve = Community(MESSAGE)

test_message = "La comunidad Python en Venezuela, por Leonardo J. Caballero G."

def test_string_not_equal():
    """ test if the message not is iqual """
    assert pyve != test_message

def test_string_equal():
    """ test if the message is iqual """
    if pyve and str(pyve.message):
        assert True

