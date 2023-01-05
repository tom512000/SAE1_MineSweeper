# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(entier: int) -> bool:
    res = False
    if type(entier) == int and (entier >= 0 and entier <= 8) or entier == const.ID_MINE:
        res = True
    return res


def construiteCellule(entier: int = 0, booleen: bool = False) -> dict:
    if not isContenuCorrect(entier):
        raise ValueError(f"construireCellule : le contenu {entier} n’est pas correct")
    if type(booleen) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({booleen}) n’est pas un booléen")
    return {const.CONTENU: entier, const.VISIBLE: booleen}


def getContenuCellule(cell: dict) -> int:
    if type(cell) != dict:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cell[const.CONTENU]
