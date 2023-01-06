# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                                         and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(nbl: int, nbc: int) -> list:
    if (nbl <= 0) or (nbc <= 0):
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes ({nbl}) ou de colonnes ({nbc}) est négatif "
                         "ou nul.")
    if (type(nbl) != int) or (type(nbc) != int):
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes ({nbl}) ou de colonnes ({nbc}) n’est pas un "
                        f"entier.")
    liste = []
    for i in range(nbl):
        ligne = []
        for j in range(nbc):
            ligne += [construiteCellule()]
        liste += [ligne]
    return liste


def getNbLignesGrilleDemineur(grille: list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    if (not type_grille_demineur(grille)) or (not type_coordonnee(coord)):
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    res = False
    if ((coord[0] < len(grille)) and (coord[0] >= 0)) and ((coord[1] < len(grille[0])) and (coord[1] >= 0)):
        res = True
    return res


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    if (not type_grille_demineur(grille)) or (not type_coordonnee(coord)):
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visibilite: bool) -> None:
    if type(visibilite) != bool:
        raise TypeError("setVisibleGrilleDemineur : Le troisième paramètre n’est pas un booléen.")
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visibilite)
    return None
