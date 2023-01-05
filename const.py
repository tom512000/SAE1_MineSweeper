# const.py
# Définition du "package" const permettant de définir des constantes
# Syntaxe :
# import const
# ...
# const.MA_CONSTANTE = 1
#
# Ce module permet d'interdire la redéfinition d'une constante existante :
# const.MA_CONSTANTE = 2 --> lèvera l'exception ConstError avec le message "Ne peut modifier la valeur de MA_CONSTANTE"
#
# see https://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991
#

import sys


class _Const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("Ne peut modifier la valeur de %s" % key)
        self.__dict__[key] = value


sys.modules[__name__] = _Const()
