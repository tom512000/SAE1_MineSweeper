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
    """
    Cette fonction permet de vérifier si le contenu de la cellule est correct ou non

    :param entier: entier dont on veut tester la valeur
    :return: `True` si le paramètre correspond à un contenu, `False` sinon.
    """
    res = False
    if (type(entier) == int and (0 <= entier <= 8)) or entier == const.ID_MINE:
        res = True
    return res


def construireCellule(entier: int = 0, visible: bool = False) -> dict:
    """
    Cette fonction permet de créer un dictionnaire correspondant à cette cellule

    :param entier: entier que l'on ajoute à la clé const.CONTENU, par défaut à 0
    :param visible: entier que l'on ajoute à la clé const.VISIBLE, par défaut à False
    :return: dictionnaire correspondant à cette cellule
    """
    if not isContenuCorrect(entier):
        raise ValueError(f"construireCellule : le contenu {entier} n’est pas correct.")
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({visible}) n’est pas un booléen.")
    return {const.CONTENU: entier, const.VISIBLE: visible, const.ANNOTATION: None}


def getContenuCellule(cell: dict) -> int:
    """
    Cette fonction permet de retourner le contenu de la cellule en paramètres

    :param cell: dictionnaire correspondant à cette cellule
    :return: valeur de la clé const.CONTENU du dictionnaire
    """
    if not type_cellule(cell):
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cell[const.CONTENU]


def isVisibleCellule(cell: dict) -> bool:
    """
    Cette fonction permet de vérifier si la visibilité de la cellule est correcte ou non

    :param cell: dictionnaire correspondant à une cellule
    :return: `True` si la valeur de la clé const.VISIBLE est du bon type, `False` sinon.
    """
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cell[const.VISIBLE]


def setContenuCellule(cell: dict, contenu: int) -> None:
    """
    Cette fonction permet de modifier le contenu de la cellule

    :param cell: dictionnaire correspondant à cette cellule
    :param contenu: entier correspondant au contenu de la cellule
    :return: Rien
    """
    if not type_cellule(cell):
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n’est pas correcte.")
    cell[const.CONTENU] = contenu
    return None


def setVisibleCellule(cell: dict, visibilite: bool) -> None:
    """
    Cette fonction permet de modifier la visibilité de la cellule

    :param cell: dictionnaire correspondant à cette cellule
    :param visibilite: booléen correspondant à la visibilité de la cellule
    :return: Rien
    """
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visibilite) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen.")
    cell[const.VISIBLE] = visibilite
    return None


def contientMineCellule(cell: dict) -> bool:
    """
    Cette fonction permet de vérifier si une cellule contient une mine

    :param cell: dictionnaire correspondant à une cellule
    :return: True si la cellule est une mine, False sinon
    """
    if not type_cellule(cell):
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    res = False
    if cell[const.CONTENU] == const.ID_MINE:
        res = True
    return res


def isAnnotationCorrecte(annotation: str) -> bool:
    """
    Cette fonction permet de vérifier si le paramètre est une annotation ou non

    :param annotation: objet dont on veut tester l'annotation
    :return: True si c'est une annotation, False sinon
    """
    res = False
    if annotation in (None, const.DOUTE, const.FLAG):
        res = True
    return res


def getAnnotationCellule(cell: dict) -> str:
    """
    Cette fonction permet de retourner l'annotation de la cellule

    :param cell: dictionnaire correspondant à une cellule
    :return: chaine de caractères correspondant à l'annotation de la cellule
    """
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : Le paramètre {cell} n’est pas une cellule.")
    if const.ANNOTATION not in cell:
        res = None
    else:
        res = cell[const.ANNOTATION]
    return res


def changeAnnotationCellule(cell: dict) -> None:
    """
    Cette fonction permet de modifier l'annotation d'une cellule dans un ordre précis

    :param cell: dictionnaire correspondant à une cellule
    :return: Rien
    """
    if not type_cellule(cell):
        raise TypeError(f"changeAnnotationCellule : le paramètre n’est pas une cellule.")
    if cell[const.ANNOTATION] is None:
        cell[const.ANNOTATION] = const.FLAG
    elif cell[const.ANNOTATION] == const.FLAG:
        cell[const.ANNOTATION] = const.DOUTE
    elif cell[const.ANNOTATION] == const.DOUTE:
        cell[const.ANNOTATION] = None
    return None


def reinitialiserCellule(cell: dict) -> None:
    """
    Cette fonction permet de réinitialiser une cellule

    :param cell: dictionnaire correspondant à une cellule
    :return: Rien
    """
    setContenuCellule(cell, 0)
    setVisibleCellule(cell, False)
    cell[const.ANNOTATION] = None
    return None
