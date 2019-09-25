""" PyTest program """

from pyve import message

def get_string():
    """ get the message string from pyve package """
    return message

def test_string_not_equal():
    """ test if the message not is iqual """
    assert get_string() != "La comunidad Python en Venezuela, por Leonardo J. Caballero G."

def test_string_equal():
    """ test if the message is iqual """
    assert get_string() == message

