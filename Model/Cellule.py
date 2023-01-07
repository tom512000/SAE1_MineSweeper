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
    if (type(entier) == int and (0 <= entier <= 8)) or entier == const.ID_MINE:
        res = True
    return res


def construireCellule(entier: int = 0, visible: bool = False) -> dict:
    if not isContenuCorrect(entier):
        raise ValueError(f"construireCellule : le contenu {entier} n’est pas correct.")
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({visible}) n’est pas un booléen.")
    return {const.CONTENU: entier, const.VISIBLE: visible, const.ANNOTATION: None}


def getContenuCellule(cell: dict) -> int:
    if not type_cellule(cell):
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cell[const.CONTENU]


def isVisibleCellule(cell: dict) -> bool:
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cell[const.VISIBLE]


def setContenuCellule(cell: dict, contenu: int) -> None:
    if not type_cellule(cell):
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n’est pas correcte.")
    cell[const.CONTENU] = contenu
    return None


def setVisibleCellule(cell: dict, visibilite: bool) -> None:
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visibilite) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen.")
    cell[const.VISIBLE] = visibilite
    return None


def contientMineCellule(cell: dict) -> bool:
    if not type_cellule(cell):
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    res = False
    if cell[const.CONTENU] == const.ID_MINE:
        res = True
    return res


def isAnnotationCorrecte(annotation: str) -> bool:
    res = False
    if annotation in (None, const.DOUTE, const.FLAG):
        res = True
    return res


def getAnnotationCellule(cell: dict) -> str:
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : Le paramètre {cell} n’est pas une cellule.")
    if const.ANNOTATION not in cell:
        res = None
    else:
        res = cell[const.ANNOTATION]
    return res
