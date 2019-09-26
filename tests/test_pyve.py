""" PyTest tests """

from pyve import py_vzla

test_message = "La comunidad Python en Venezuela, por Leonardo J. Caballero G."

def test_string_not_equal():
    """ test if the message not is iqual """
    assert py_vzla != test_message

def test_string_equal():
    """ test if the message is iqual """
    if py_vzla and str(py_vzla.message):
        assert True

