""" Documentation from Python Venezuela Community """

MESSAGE = """La comunidad Python en Venezuela, por Leonardo J. Caballero G.\n
Somos un grupo de entusiastas reunidos.
Nuestro objetivo: promocionar el lenguaje de programación Python
Nos gusta difundir las bondades de Python.
Somos chamos y chamas muy panas.
Nos gusta cayapiar a Python.
Las dificultades de nuestro país (Murphy y la PATRIA) no nos detiene.
Muchos migraron, muchos siguen luchando.
Hemos organizado la Conferencia Nacional PyCon, PyDay, DjangoGirls, talleres.
Tenemos la organización "Fundación Python Venezuela".
Tenemos página principal https://pyve.github.io
Tenemos página de Facebook https://facebook.com/python.ve
Nos encuentras en Telegram https://t.me/python_venezuela
Estamos en Linkedin https://linkedin.com/company/fundación-python-de-venezuela
Nosotros tuiteamos en https://twitter.com/PythonVe
Nosotros también tuiteamos en https://twitter.com/PyConVe
Colaboramos en la forja de código Github https://github.com/pyve
"PYTHONISTA QUIEN LO LEA!!!", si chalequeamos mientras hackeamos.
Somos tan Vergatarios como la Chinita!!!
Somos tan Restiaos como los andinos!!!
Somos tan Guaros como el Cuatro!!!
Somos tan Orientales como el rompe colchón!!!
Somos tan Capitalinos como el Avila!!!
Somos tan Venezolanos como la Arepa!!!
Somos solidarios, somos Venezolanos."""


class Community(object):
    """ Class that represent to Python Venezuela Community """

    def __init__(self, message):
        """ PyVe Constructor Class """
        self.message = message

    def __str__(self):
        """ Return a string about the Python Venezuela Community """
        return "%s" % (self.message)


py_vzla = Community(MESSAGE)
print(py_vzla)
