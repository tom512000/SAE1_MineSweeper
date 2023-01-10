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
    """
    Cette fonction permet de créer une grille sous forme de liste avec `nbl` ligne(s) et `nbc` colonne(s)

    :param nbl: entier correspondant au nombre de lignes
    :param nbc: entier correspondant au nombre de colonnes
    :return: liste correspondant à une grille
    """
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
            ligne += [construireCellule()]
        liste += [ligne]
    return liste


def getNbLignesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction permet de retourner le nombre de lignes d'une grille

    :param grille: liste correspondant à une grille
    :return: entier correspondant au nombre de lignes
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction permet de retourner le nombre de colonnes d'une grille

    :param grille: liste correspondant à une grille
    :return: entier correspondant au nombre de colonnes
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    """
    Cette fonction permet de vérifier si la coordonnée en paramètre est dans la grille ou non

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: `True` si la coordonnée est dans la grille, `False` sinon.
    """
    if (not type_grille_demineur(grille)) or (not type_coordonnee(coord)):
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    res = False
    if ((coord[0] < getNbLignesGrilleDemineur(grille)) and (coord[0] >= 0)) and (
            (coord[1] < getNbColonnesGrilleDemineur(grille)) and (coord[1] >= 0)):
        res = True
    return res


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    """
    Cette fonction permet de retourner une cellule d'une grille grâce à une coordonnée

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: dictionnaire correspondant à une cellule
    """
    if (not type_grille_demineur(grille)) or (not type_coordonnee(coord)):
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    """
    Cette fonction permet de retourner le contenu d'une cellule grâce à une grille et une coordonnée

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: entier correspondant au contenu d'une cellule
    """
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    """
    Cette fonction permet de modifier le contenu de la cellule grâce à une grille et une coordonnée

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :param contenu: entier correspondant au contenu de la cellule
    :return: Rien
    """
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Cette fonction permet de vérifier si la visibilité de la cellule est correcte ou non grâce à une grille et une
    coordonnée

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: `True` si la valeur de la clé const.VISIBLE est du bon type, `False` sinon.
    """
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visibilite: bool) -> None:
    """
    Cette fonction permet de modifier la visibilité de la cellule grâce à une grille et une coordonnée

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :param visibilite: booléen correspondant à la visibilité de la cellule
    :return: Rien
    """
    if type(visibilite) != bool:
        raise TypeError("setVisibleGrilleDemineur : Le troisième paramètre n’est pas un booléen.")
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visibilite)
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Cette fonction permet de vérifier si une cellule contient une mine grâce à une grille et une coordonnée

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: True si la cellule est une mine, False sinon
    """
    res = False
    if getCelluleGrilleDemineur(grille, coord)[const.CONTENU] == const.ID_MINE:
        res = True
    return res


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """
    Cette fonction permet de retourner une liste constituée des coordonnées des cellules voisines d'une cellule grâce
    à une grille et une coordonnée

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: liste constituée des coordonnées des cellules voisines
    """
    if (not type_grille_demineur(grille)) or (not type_coordonnee(coord)):
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    voisins = []
    for i in range(coord[0] - 1, coord[0] + 2):
        if (i >= 0) and (i < getNbLignesGrilleDemineur(grille)):
            for j in range(coord[1] - 1, coord[1] + 2):
                if (j >= 0) and (j < getNbColonnesGrilleDemineur(grille)) and ((i, j) != coord):
                    voisins += [(i, j)]
    return voisins


def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    """
    Cette fonction permet de placer aléatoirement `nb` mine(s) dans une grille

    :param grille: liste correspondant à une grille
    :param nb: entier correspondant au nombre de mines à placer dans la grille
    :param coord: couple correspondant à une coordonnée
    :return: Rien
    """
    if (nb < 0) or (nb > (getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille)) - 1):
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect.")
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    for i in range(nb):
        x = randint(0, getNbLignesGrilleDemineur(grille) - 1)
        y = randint(0, getNbColonnesGrilleDemineur(grille) - 1)
        cellule = (x, y)
        while (cellule == coord) or (getContenuCellule(getCelluleGrilleDemineur(grille, cellule)) == const.ID_MINE):
            x = randint(0, getNbLignesGrilleDemineur(grille) - 1)
            y = randint(0, getNbColonnesGrilleDemineur(grille) - 1)
            cellule = (x, y)
        setContenuCellule(getCelluleGrilleDemineur(grille, cellule), const.ID_MINE)
    compterMinesVoisinesGrilleDemineur(grille)
    return None


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    """
    Cette fonction permet de calculer pour chaque cellule le nombre de mines parmi ses cellules voisines

    :param grille: liste correspondant à une grille
    :return: Rien
    """
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if getContenuCellule(getCelluleGrilleDemineur(grille, (i, j))) != const.ID_MINE:
                coord = getCoordonneeVoisinsGrilleDemineur(grille, (i, j))
                bombes = 0
                for k in range(len(coord)):
                    if getContenuCellule(getCelluleGrilleDemineur(grille, (coord[k][0], coord[k][1]))) == const.ID_MINE:
                        bombes += 1
                setContenuGrilleDemineur(grille, (i, j), bombes)
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction permet de calculer le nombre total de mines dans une grille

    :param grille: liste correspondant à une grille
    :return: entier correspondant au nombre de mines
    """
    if not type_grille_demineur(grille):
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    bombes = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if getContenuCellule(getCelluleGrilleDemineur(grille, (i, j))) == const.ID_MINE:
                bombes += 1
    return bombes


def getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    """
    Cette fonction permet de retourner l'annotation d'une cellule grâce à une grille et une coordonnée

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: chaine de caractères correspondant à l'annotation de la cellule
    """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction permet de calculer le nombre de mines restantes dans une grille

    :param grille: liste correspondant à une grille
    :return: entier correspondant au nombre de mines
    """
    nb = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if getAnnotationGrilleDemineur(grille, (i, j)) == const.FLAG:
                nb += 1
    return getNbMinesGrilleDemineur(grille) - nb


def gagneGrilleDemineur(grille: list) -> bool:
    """
    Cette fonction permet de vérifier si une partie est gagnée ou non

    :param grille: liste correspondant à une grille
    :return: True si la partie est gagnée, False sinon
    """
    res = True
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if (not contientMineGrilleDemineur(grille, (i, j)) and not isVisibleGrilleDemineur(grille, (i, j))) or (
                    (contientMineGrilleDemineur(grille, (i, j)) == True) and (isVisibleGrilleDemineur(grille, (i, j)
                                                                                                      ) == True)) or (
                    ((contientMineGrilleDemineur(grille, (i, j)) == True) and (not getAnnotationGrilleDemineur(grille, (
                            i, j))) == const.FLAG)):
                res = False
    return res


def perduGrilleDemineur(grille: list):
    """
    Cette fonction permet de vérifier si une partie est perdue ou non

    :param grille: liste correspondant à une grille
    :return: True si la partie est perdue, False sinon
    """
    res = False
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if (contientMineGrilleDemineur(grille, (i, j)) == True) and (
                    isVisibleGrilleDemineur(grille, (i, j)) == True):
                res = True
    return res


def reinitialiserGrilleDemineur(grille: list) -> None:
    """
    Cette fonction permet de réinitialiser toutes les cellules d'une grille

    :param grille: liste correspondant à une grille
    :return: Rien
    """
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            reinitialiserCellule(grille[i][j])
    return None


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Cette fonction permet de découvrir les cellules adjacentes à une cellule contenant 0 mine

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: ensemble constitué des coordonnées des cellules modifiées
    """
    if isVisibleGrilleDemineur(grille, coord):
        return set()
    setVisibleGrilleDemineur(grille, coord, True)
    if getContenuGrilleDemineur(grille, coord):
        return {coord}
    else:
        voisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
        coorddec = set()
        for coordvoisins in voisins:
            coorddec.update(decouvrirGrilleDemineur(grille, coordvoisins))
        for element in coorddec:
            setVisibleGrilleDemineur(grille, (element[0], element[1]), True)
        coorddec.add(coord)
        return coorddec


def simplifierGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Cette fonction permet de découvrir les cellules voisines lorsque le nombre de drapeaux correspond au nombre de
    mines dans le contenu de la cellule

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: ensemble constitué des coordonnées des cellules modifiées
    """
    if not isVisibleGrilleDemineur(grille, coord):
        return set()
    voisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
    drapeaux = 0
    for coordvoisins in voisins:
        if (not isVisibleGrilleDemineur(grille, coordvoisins)) and (getAnnotationGrilleDemineur(grille, coordvoisins) == const.FLAG):
            drapeaux += 1
    if drapeaux == getContenuGrilleDemineur(grille, coord):
        coorddec = set()
        for coordvoisins in voisins:
            if (not isVisibleGrilleDemineur(grille, coordvoisins)) and (
                    getAnnotationGrilleDemineur(grille, coordvoisins) != const.FLAG):
                setVisibleGrilleDemineur(grille, coordvoisins, True)
                coorddec.add(coordvoisins)
        return coorddec
    else:
        return set()


def ajouterFlagsGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Cette fonction permet de découvrir les cellules voisines lorsque le nombre de cases non découvertes correspond au
    nombre de mines dans le contenu de la cellule

    :param grille: liste correspondant à une grille
    :param coord: couple correspondant à une coordonnée
    :return: ensemble constitué des coordonnées des cellules modifiées
    """
    if not isVisibleGrilleDemineur(grille, coord):
        return set()
    cellnondec = 0
    voisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
    for coordvoisins in voisins:
        if not isVisibleGrilleDemineur(grille, coordvoisins):
            cellnondec += 1
    if cellnondec == getContenuGrilleDemineur(grille, coord):
        coorddec = set()
        for coordvoisins in voisins:
            if not isVisibleGrilleDemineur(grille, coordvoisins):
                getCelluleGrilleDemineur(grille, coordvoisins)[const.ANNOTATION] = const.FLAG
                coorddec.add(coordvoisins)
        return coorddec
    else:
        return set()


def simplifierToutGrilleDemineur(grille: list) -> tuple:
    """
    Cette fonction permet de découvrir les cellules voisines lorsque le nombre de cases non découvertes correspond au
    nombre de mines dans le contenu de la cellule

    :param grille: liste correspondant à une grille
    :return: couple constitué d'un ensemble correspondant aux coordonnées des cellules modifiées par la première
    fonction et d'un deuxième ensemble correspondant aux coordonnées des cellules modifiées par la deuxième fonction
    """
    simplifier = set()
    ajouter = set()
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            grille1 = grille.copy()
            simplifierGrilleDemineur(grille, (i, j))
            grille2 = grille.copy()
            if grille1 != grille2:
                simplifier.add((i, j))
            grille1 = grille.copy()
            ajouterFlagsGrilleDemineur(grille, (i, j))
            grille2 = grille.copy()
            if grille1 != grille2:
                ajouter.add((i, j))
    return simplifier, ajouter
