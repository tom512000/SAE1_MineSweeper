import unittest
from Model.GrilleDemineur import *
from random import randint, shuffle
from copy import deepcopy

scientific_modules_installed = True

try:
    import numpy as np
    from scipy import signal
except ImportError:
    scientific_modules_installed = False


class TestGrilleDemineur(unittest.TestCase):

    def __print__(self, grille):
        return '\n' + '\n'.join([','.join([str(c) for c in ligne]) for ligne in grille]) + '\n'

    @unittest.skipIf('construireGrilleDemineur' not in globals(), "constructeur manquant")
    def test_construireGrilleDemineur(self):
        g = construireGrilleDemineur(5, 10)
        self.assertTrue(type_grille_demineur(g), "Problème avec le constructeur...")

    @unittest.skipIf('construireGrilleDemineur' not in globals(), "constructeur manquant")
    def test_construireGrilleDemineur_raise_ValueError(self):
        for li in range(-5, 1):
            self.assertRaises(ValueError, construireGrilleDemineur, li, 5)
        for co in range(-5, 1):
            self.assertRaises(ValueError, construireGrilleDemineur, 5, co)

    @unittest.skipIf('construireGrilleDemineur' not in globals(), "constructeur manquant")
    def test_OPTION_construireGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, construireGrilleDemineur, 2.4, 5)
        self.assertRaises(TypeError, construireGrilleDemineur, 5, 6.3)

    @unittest.skipIf('construireGrilleDemineur' not in globals() or 'getNbLignesGrilleDemineur' not in globals(),
                     "Le constructeur ou getNbLignesGrilleDemineur non écrits")
    def test_getNbLignesGrilleDemineur(self):
        co = 20
        for i in range(1, 20):
            c = construireGrilleDemineur(i, co)
            self.assertEqual(i, getNbLignesGrilleDemineur(c))

    @unittest.skipIf('construireGrilleDemineur' not in globals() or 'getNbLignesGrilleDemineur' not in globals(),
                     "Le constructeur ou getNbLignesGrilleDemineur non écrits")
    def test_OPTION_getNbLignesGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, getNbLignesGrilleDemineur, "Rien ne va plus !")
        self.assertRaises(TypeError, getNbLignesGrilleDemineur, 10)
        self.assertRaises(TypeError, getNbLignesGrilleDemineur, [10])

    @unittest.skipIf('construireGrilleDemineur' not in globals() or 'getNbColonnesGrilleDemineur' not in globals(),
                     "Le constructeur ou getNbColonnesGrilleDemineur non écrits")
    def test_getNbColonnesGrilleDemineur(self):
        li = 20
        for i in range(1, 20):
            c = construireGrilleDemineur(li, i)
            self.assertEqual(i, getNbColonnesGrilleDemineur(c))

    @unittest.skipIf('construireGrilleDemineur' not in globals() or 'getNbColonnesGrilleDemineur' not in globals(),
                     "Le constructeur ou getNbColonnesGrilleDemineur non écrits")
    def test_OPTION_getNbColonnesGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, getNbColonnesGrilleDemineur, "Rien ne va plus !")
        self.assertRaises(TypeError, getNbColonnesGrilleDemineur, 10)
        self.assertRaises(TypeError, getNbColonnesGrilleDemineur, [10])

    @unittest.skipIf('construireGrilleDemineur' not in globals() or 'isCoordonneeCorrecte' not in globals(),
                     "Le constructeur ou isCoordonneeCorrecte non écrit")
    def test_isCoordonneeCorrecte(self):
        for li in range(1, 10):
            l_li = list(range(li))
            for co in range(1, 10):
                g = construireGrilleDemineur(li, co)
                l_co = list(range(co))
                for l in range(15):
                    for c in range(15):
                        self.assertEqual(l in l_li and c in l_co, isCoordonneeCorrecte(g, (l, c)))

    @unittest.skipIf('construireGrilleDemineur' not in globals() or 'isCoordonneeCorrecte' not in globals(),
                     "Le constructeur ou isCoordonneeCorrecte non écrit")
    def test_OPTION_isCoordonneeCorrecte_raise_TypeError(self):
        self.assertRaises(TypeError, isCoordonneeCorrecte, "Rien ne va plus", (0, 0))
        g = construireGrilleDemineur(10, 10)
        self.assertRaises(TypeError, isCoordonneeCorrecte, g, "OK")
        self.assertRaises(TypeError, isCoordonneeCorrecte, g, 0)

    @unittest.skipIf('getCelluleGrilleDemineur' not in globals(), "getCelluleGrilleDemineur non écrite")
    def test_getCelluleGrilleDemineur(self):
        # A ne pas faire: construction d'une grille "à la main" !!
        nl = 10
        nc = 5
        g = [[{const.CONTENU: (j * nc + i) % 10 - 1, const.VISIBLE: (j * nc + i) % 2 == 1} for j in range(nc)]
             for i in range(nl)]
        for i in range(nl):
            for j in range(nc):
                cell = {const.CONTENU: (j * nc + i) % 10 - 1, const.VISIBLE: (j * nc + i) % 2 == 1}
                coord = construireCoordonnee(i, j)
                self.assertEqual(cell, getCelluleGrilleDemineur(g, coord), "Problème avec getCelluleGrilleDemineur")

    @unittest.skipIf('getCelluleGrilleDemineur' not in globals(), "getCelluleGrilleDemineur non écrite")
    def test_OPTION_getCelluleGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, getCelluleGrilleDemineur, "Rien ne a plus", construireCoordonnee(0, 0))
        g = construireGrilleDemineur(5, 5)
        self.assertRaises(TypeError, getCelluleGrilleDemineur, g, "Rien ne va plus")

    @unittest.skipIf('getContenuGrilleDemineur' not in globals(), "getContenuGrilleDemineur non écrit")
    def test_getContenuGrilleDemineur(self):
        # A ne pas faire: construction d'une grille "à la main" !!
        nl = 10
        nc = 5
        g = [[{const.CONTENU: (j * nc + i) % 10 - 1, const.VISIBLE: (j * nc + i) % 2 == 1} for j in range(nc)]
             for i in range(nl)]
        for i in range(nl):
            for j in range(nc):
                contenu = (j * nc + i) % 10 - 1
                coord = construireCoordonnee(i, j)
                self.assertEqual(contenu, getContenuGrilleDemineur(g, coord), "Problème avec getContenuGrilleDemineur")

    @unittest.skipIf('getContenuGrilleDemineur' not in globals(), "getContenuGrilleDemineur non écrit")
    def test_OPTION_getContenuGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, getContenuGrilleDemineur, "Rien ne va plus", construireCoordonnee(0, 0))
        g = construireGrilleDemineur(10, 5)
        self.assertRaises(TypeError, getContenuGrilleDemineur, g, "Rien ne va plus !")

    @unittest.skipIf('getContenuGrilleDemineur' not in globals(), "getContenuGrilleDemineur non écrit")
    def test_OPTION_getContenuGrilleDemineur_raise_IndexError(self):
        g = construireGrilleDemineur(5, 10)
        for i in range(5):
            self.assertRaises(IndexError, getContenuGrilleDemineur, g, construireCoordonnee(5 + i, 0))
            self.assertRaises(IndexError, getContenuGrilleDemineur, g, construireCoordonnee(0, 10 + i))

    @unittest.skipIf('setContenuGrilleDemineur' not in globals(), "setContenuGrilleDemineur non écrit")
    def test_setContenuGrilleDemineur(self):
        # A ne pas faire: construction d'une grille "à la main" !!
        nl = 10
        nc = 5
        g = [[{const.CONTENU: (j * nc + i) % 9 - 1, const.VISIBLE: (j * nc + i) % 2 == 1} for j in range(nc)]
             for i in range(nl)]
        for i in range(nl):
            for j in range(nc):
                coord = construireCoordonnee(i, j)
                setContenuGrilleDemineur(g, coord, 8)
                self.assertEqual(8, getContenuGrilleDemineur(g, coord), "Problème avec setContenuGrilleDemineur")

    @unittest.skipIf('setContenuGrilleDemineur' not in globals(), "setContenuGrilleDemineur non écrit")
    def test_OPTION_setContenuGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, setContenuGrilleDemineur, "Rien ne va plus", construireCoordonnee(0, 0), 0)
        g = construireGrilleDemineur(10, 5)
        self.assertRaises(TypeError, setContenuGrilleDemineur, g, "Rien ne va plus !", 0)
        self.assertRaises(TypeError, setContenuGrilleDemineur, g, construireCoordonnee(0, 0), "Rien ne va plus !")

    @unittest.skipIf('setContenuGrilleDemineur' not in globals(), "setContenuGrilleDemineur non écrit")
    def test_OPTION_setContenuGrilleDemineur_raise_ValueError(self):
        g = construireGrilleDemineur(10, 5)
        self.assertRaises(ValueError, setContenuGrilleDemineur, g, construireCoordonnee(0, 0), -5)
        self.assertRaises(ValueError, setContenuGrilleDemineur, g, construireCoordonnee(0, 0), 9)

    @unittest.skipIf('setContenuGrilleDemineur' not in globals(), "setContenuGrilleDemineur non écrit")
    def test_OPTION_setContenuGrilleDemineur_raise_IndexError(self):
        g = construireGrilleDemineur(5, 10)
        for i in range(5):
            self.assertRaises(IndexError, setContenuGrilleDemineur, g, construireCoordonnee(5 + i, 0), 0)
            self.assertRaises(IndexError, setContenuGrilleDemineur, g, construireCoordonnee(0, 10 + i), 0)

    @unittest.skipIf('isVisibleGrilleDemineur' not in globals(), "isVisibleGrilleDemineur non écrit")
    def test_isVisibleGrilleDemineur(self):
        # A ne pas faire: construction d'une grille "à la main" !!
        nl = 10
        nc = 5
        g = [[{const.CONTENU: (j * nc + i) % 10 - 1, const.VISIBLE: (j * nc + i) % 2 == 1} for j in range(nc)]
             for i in range(nl)]
        for i in range(nl):
            for j in range(nc):
                visible = (j * nc + i) % 2 == 1
                coord = construireCoordonnee(i, j)
                self.assertEqual(visible, isVisibleGrilleDemineur(g, coord), "Problème avec isVisibleGrilleDemineur")

    @unittest.skipIf('isVisibleGrilleDemineur' not in globals(), "isVisibleGrilleDemineur non écrit")
    def test_OPTION_isVisibleGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, isVisibleGrilleDemineur, "Rien ne va plus", construireCoordonnee(0, 0))
        g = construireGrilleDemineur(10, 5)
        self.assertRaises(TypeError, isVisibleGrilleDemineur, g, "Rien ne va plus !")

    @unittest.skipIf('isVisibleGrilleDemineur' not in globals(), "isVisibleGrilleDemineur non écrit")
    def test_OPTION_isVisibleGrilleDemineur_raise_IndexError(self):
        g = construireGrilleDemineur(5, 10)
        for i in range(5):
            self.assertRaises(IndexError, isVisibleGrilleDemineur, g, construireCoordonnee(5 + i, 0))
            self.assertRaises(IndexError, isVisibleGrilleDemineur, g, construireCoordonnee(0, 10 + i))

    @unittest.skipIf('setVisibleGrilleDemineur' not in globals(), "setVisibleGrilleDemineur non écrit")
    def test_setVisibleGrilleDemineur(self):
        # A ne pas faire: construction d'une grille "à la main" !!
        nl = 10
        nc = 5
        g = [[{const.CONTENU: (j * nc + i) % 9 - 1, const.VISIBLE: (j * nc + i) % 2 == 1} for j in range(nc)]
             for i in range(nl)]
        for i in range(nl):
            for j in range(nc):
                coord = construireCoordonnee(i, j)
                visible = (j * nc + i) % 2 != 1
                setVisibleGrilleDemineur(g, coord, visible)
                self.assertEqual(visible, isVisibleGrilleDemineur(g, coord), "Problème avec setVisibleGrilleDemineur")

    @unittest.skipIf('setVisibleGrilleDemineur' not in globals(), "setVisibleGrilleDemineur non écrit")
    def test_OPTION_setVisibleGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, setVisibleGrilleDemineur, "Rien ne va plus", construireCoordonnee(0, 0), True)
        g = construireGrilleDemineur(10, 5)
        self.assertRaises(TypeError, setVisibleGrilleDemineur, g, "Rien ne va plus !", True)
        self.assertRaises(TypeError, setVisibleGrilleDemineur, g, construireCoordonnee(0, 0), 0)

    @unittest.skipIf('setVisibleGrilleDemineur' not in globals(), "setVisibleGrilleDemineur non écrit")
    def test_OPTION_setVIsibleGrilleDemineur_raise_IndexError(self):
        g = construireGrilleDemineur(5, 10)
        for i in range(5):
            self.assertRaises(IndexError, setVisibleGrilleDemineur, g, construireCoordonnee(5 + i, 0), False)
            self.assertRaises(IndexError, setVisibleGrilleDemineur, g, construireCoordonnee(0, 10 + i), False)

    @unittest.skipIf('contientMineGrilleDemineur' not in globals(), 'contientMineGrilleDemineur non écrit')
    def test_contientMineGrilleDemineur(self):
        # A ne pas faire: construction d'une grille "à la main" !!
        nl = 10
        nc = 5
        g = [[{const.CONTENU: (j * nc + i) % 10 - 1, const.VISIBLE: (j * nc + i) % 2 == 1} for j in range(nc)]
             for i in range(nl)]
        for i in range(nl):
            for j in range(nc):
                coord = construireCoordonnee(i, j)
                contient = (j * nc + i) % 10 - 1 == const.ID_MINE
                self.assertEqual(contient, contientMineGrilleDemineur(g, coord),
                                 "Problème avec contientMineGrilleDemineur")

    @unittest.skipIf('contientMineGrilleDemineur' not in globals(), 'contientMineGrilleDemineur non écrit')
    def test_OPTION_contientMineGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, contientMineGrilleDemineur, "Rien ne va plus", construireCoordonnee(0, 0))
        g = construireGrilleDemineur(10, 5)
        self.assertRaises(TypeError, contientMineGrilleDemineur, g, "Rien ne va plus !")

    @unittest.skipIf('contientMineGrilleDemineur' not in globals(), 'contientMineGrilleDemineur non écrit')
    def test_OPTION_contientMineGrilleDemineur_raise_IndexError(self):
        g = construireGrilleDemineur(5, 10)
        for i in range(5):
            self.assertRaises(IndexError, contientMineGrilleDemineur, g, construireCoordonnee(5 + i, 0))
            self.assertRaises(IndexError, contientMineGrilleDemineur, g, construireCoordonnee(0, 10 + i))

    @unittest.skipIf('getCoordonneeVoisinsGrilleDemineur' not in globals(),
                     'getCoordonneeVoisinsGrilleDemineur non écrit')
    def test_getCoordonneeVoisinsGrilleDemineur(self):
        g = construireGrilleDemineur(7, 11)
        # Test des voisins en (0, 0)
        attendu = {(1, 0), (1, 1), (0, 1)}
        res = getCoordonneeVoisinsGrilleDemineur(g, construireCoordonnee(0, 0))
        s_res = set(res)
        self.assertEqual(len(res), len(s_res), "getCoordonneeVoisinsGrilleDemineur duplique des résultats !")
        self.assertEqual(attendu, s_res, "Probleme avec getCoordonneeVoisinsGrilleDemineur quand la coordonnée est \
        en (0, 0) (coin supérieur gauche)")
        # Test des voisins en (3, 0)
        attendu = {(2, 0), (2, 1), (3, 1), (4, 1), (4, 0)}
        res = getCoordonneeVoisinsGrilleDemineur(g, construireCoordonnee(3, 0))
        s_res = set(res)
        self.assertEqual(len(res), len(s_res), "getCoordonneeVoisinsGrilleDemineur duplique des résultats !")
        self.assertEqual(attendu, s_res, "Probleme avec getCoordonneeVoisinsGrilleDemineur quand la coordonnée est en \
        (3, 0) (bord gauche)")
        # Test des voisins en (6, 0)
        attendu = {(5, 0), (5, 1), (6, 1)}
        res = getCoordonneeVoisinsGrilleDemineur(g, construireCoordonnee(6, 0))
        s_res = set(res)
        self.assertEqual(len(res), len(s_res), "getCoordonneeVoisinsGrilleDemineur duplique des résultats !")
        self.assertEqual(attendu, s_res, "Probleme avec getCoordonneeVoisinsGrilleDemineur quand la coordonnée est en \
        (6, 0) (coin inférieur gauche)")
        # Test des voisins en (6, 5)
        attendu = {(6, 4), (5, 4), (5, 5), (5, 6), (6, 6)}
        res = getCoordonneeVoisinsGrilleDemineur(g, construireCoordonnee(6, 5))
        s_res = set(res)
        self.assertEqual(len(res), len(s_res), "getCoordonneeVoisinsGrilleDemineur duplique des résultats !")
        self.assertEqual(attendu, s_res, "Probleme avec getCoordonneeVoisinsGrilleDemineur quand la coordonnée est en \
        (6, 5) (bord inférieur)")
        # Test des voisins en (6, 10)
        attendu = {(6, 9), (5, 9), (5, 10)}
        res = getCoordonneeVoisinsGrilleDemineur(g, construireCoordonnee(6, 10))
        s_res = set(res)
        self.assertEqual(len(res), len(s_res), "getCoordonneeVoisinsGrilleDemineur duplique des résultats !")
        self.assertEqual(attendu, s_res, "Probleme avec getCoordonneeVoisinsGrilleDemineur quand la coordonnée est en \
        (6, 10) (coin inférieur droit)")
        # Test des voisins en (2, 10)
        attendu = {(3, 10), (3, 9), (2, 9), (1, 9), (1, 10)}
        res = getCoordonneeVoisinsGrilleDemineur(g, construireCoordonnee(2, 10))
        s_res = set(res)
        self.assertEqual(len(res), len(s_res), "getCoordonneeVoisinsGrilleDemineur duplique des résultats !")
        self.assertEqual(attendu, s_res, "Probleme avec getCoordonneeVoisinsGrilleDemineur quand la coordonnée est en \
        (2, 10) (bord droit)")
        # Test des voisins en (0, 10)
        attendu = {(1, 10), (1, 9), (0, 9)}
        res = getCoordonneeVoisinsGrilleDemineur(g, construireCoordonnee(0, 10))
        s_res = set(res)
        self.assertEqual(len(res), len(s_res), "getCoordonneeVoisinsGrilleDemineur duplique des résultats !")
        self.assertEqual(attendu, s_res, "Probleme avec getCoordonneeVoisinsGrilleDemineur quand la coordonnée est en \
        (0, 10) (coin supérieur droit)")
        # Test des voisins en (3, 8)
        attendu = {(4, 8), (4, 9), (3, 9), (2, 9), (2, 8), (2, 7), (3, 7), (4, 7)}
        res = getCoordonneeVoisinsGrilleDemineur(g, construireCoordonnee(3, 8))
        s_res = set(res)
        self.assertEqual(len(res), len(s_res), "getCoordonneeVoisinsGrilleDemineur duplique des résultats !")
        self.assertEqual(attendu, s_res, "Probleme avec getCoordonneeVoisinsGrilleDemineur quand la coordonnée est en \
        (3, 8) (coordonnée dans la grille)")

    @unittest.skipIf('getCoordonneeVoisinsGrilleDemineur' not in globals(),
                     'getCoordonneeVoisinsGrilleDemineur non écrit')
    def test_OPTION_getCoordonneeVoisinsGrilleDemineur_raise_TypeError(self):
        self.assertRaises(TypeError, getCoordonneeVoisinsGrilleDemineur, "Rien ne va plus", construireCoordonnee(0, 0))
        g = construireGrilleDemineur(10, 5)
        self.assertRaises(TypeError, getCoordonneeVoisinsGrilleDemineur, g, "Rien ne va plus !")

    @unittest.skipIf('getCoordonneeVoisinsGrilleDemineur' not in globals(),
                     'getCoordonneeVoisinsGrilleDemineur non écrit')
    def test_OPTION_getCoordonneeVoisinsGrilleDemineur_raise_IndexError(self):
        g = construireGrilleDemineur(5, 10)
        for i in range(5):
            self.assertRaises(IndexError, getCoordonneeVoisinsGrilleDemineur, g, construireCoordonnee(5 + i, 0))
            self.assertRaises(IndexError, getCoordonneeVoisinsGrilleDemineur, g, construireCoordonnee(0, 10 + i))

    @unittest.skipIf('placerMinesGrilleDemineur' not in globals(),
                     'placerMinesGrilleDemineur non écrit')
    def test_placerMinesGrilleDemineur(self):
        # Tests aléatoires
        for _ in range(10):  # 10 tests
            g = construireGrilleDemineur(5, 10)
            c = (randint(0, 4), randint(0, 9))
            nb = randint(10, 40)
            placerMinesGrilleDemineur(g, nb, c)
            # Compter le nombre de mines
            m = []
            for li in g:
                m.extend([1 for c in li if c[const.CONTENU] == const.ID_MINE])
            self.assertEqual(nb, sum(m), f"{nb} mines demandées, {sum(m)} mines trouvées ??")
            # Vérifier que la cellule donnée ne contient pas de mine
            self.assertFalse(g[c[0]][c[1]][const.CONTENU] == const.ID_MINE,
                             f"La cellule {c} ne devrait pas contenir de mine !")

    @unittest.skipIf('placerMinesGrilleDemineur' not in globals(),
                     'placerMinesGrilleDemineur non écrit')
    def test_placerMinesGrilleDemineur_raise_ValueError(self):
        g = construireGrilleDemineur(5, 10)
        self.assertRaises(ValueError, placerMinesGrilleDemineur, g, -1, (0, 0))
        self.assertRaises(ValueError, placerMinesGrilleDemineur, g, 50, (0, 0))

    @unittest.skipIf('placerMinesGrilleDemineur' not in globals(),
                     'placerMinesGrilleDemineur non écrit')
    def test_OPTION_placerMinesGrilleDemineur_raise_TypeError(self):
        g = construireGrilleDemineur(5, 10)
        self.assertRaises(IndexError, placerMinesGrilleDemineur, g, 10, (5, 0))
        self.assertRaises(IndexError, placerMinesGrilleDemineur, g, 10, (0, 10))
        self.assertRaises(IndexError, placerMinesGrilleDemineur, g, 10, (5, 10))

    @unittest.skipIf('compterMinesVoisinesGrilleDemineur' not in globals(),
                     'compterMinesVoisinesGrilleDemineur non écrite')
    @unittest.skipIf(not scientific_modules_installed, "Pour utiliser ce test, il faut installer numpy et scipy !...")
    def test_compterMinesVoisinesGrilleDemineur(self):
        # Chaînes de formatage...
        sp1 = "\n"
        sp2 = " "
        fm = "{:>2}"
        # Tests aléatoires...
        for _ in range(10):
            nl = randint(5, 10)
            nc = randint(5, 10)
            nb = randint(10, nl * nc)
            # Création de la grille avec les mines : A NE PAS FAIRE !
            arr = [[0 if randint(0, nl * nc) > nb else 1 for _ in range(nc)] for _ in range(nl)]
            g = [[{const.CONTENU: const.ID_MINE if arr[i][j] else 0, const.VISIBLE: True} for j in range(nc)] for i in
                 range(nl)]
            # Compter les mines voisines
            compterMinesVoisinesGrilleDemineur(g)
            # Vérification
            arr2 = signal.convolve2d(np.array(arr), np.array([[1] * 3] * 3))[1:-1, 1:-1]
            for i in range(nl):
                for j in range(nc):
                    if arr[i][j] == 0:
                        self.assertEqual(arr2[i][j], g[i][j][const.CONTENU],
                                         f"Le décompte des mines voisines en ({i},{j}) devrait donner {arr2[i][j]} au lieu de {g[i][j][const.CONTENU]}\n\
Votre calcul (dans le voisinage de ({i},{j}) ) :\n\
{sp1.join([sp2.join([fm.format(g[_i][_j][const.CONTENU]) for _j in range(max(j - 1, 0), min(j + 2, nc))]) for _i in range(max(i - 1, 0), min(i + 2, nl))])}\n\
Le calcul attendu (dans le voisinage de ({i},{j}) ) :\n\
{sp1.join([sp2.join([fm.format(arr2[_i][_j] if not arr[_i][_j] else -1) for _j in range(max(j - 1, 0), min(j + 2, nc))]) for _i in range(max(i - 1, 0), min(i + 2, nl))])}\n")

    @unittest.skipIf("getNbMinesGrilleDemineur" not in globals(), "Fonction getNbMinesGrilleDemineur non écrite.")
    def test_getNbMinesGrilleDemineur(self):
        for _ in range(500):
            nl = randint(4, 10)
            nc = randint(4, 10)
            # Contruction d'une grille à la main : A NE PAS FAIRE !
            grille = [[{const.CONTENU: 0, const.VISIBLE: False} for _j in range(nc)] for _i in range(nl)]
            # Déterminer aléatoirement un nombre de mines
            nb = randint(0, nl*nc - 10)
            coords = [(_n // nc, _n % nc) for _n in range(nl*nc)]
            shuffle(coords)
            for i in range(nb):
                setContenuGrilleDemineur(grille, coords[i], const.ID_MINE)
            n = getNbMinesGrilleDemineur(grille)
            self.assertEqual(nb, n, f"La grille {grille} contient {nb} mines au lieu de {n} retourné par la fonction getNbMinesGrilleDemineur")

    @unittest.skipIf("getNbMinesGrilleDemineur" not in globals(), "Fonction getNbMinesGrilleDemineur non écrite.")
    def test_OPTION_getNbMinesGrilleDemineur_raise_ValueError(self):
        self.assertRaises(ValueError, getNbMinesGrilleDemineur, "Ca ne marche pas !")
        self.assertRaises(ValueError, getNbMinesGrilleDemineur, [[0, 1, 2], [3, 4, 5]])
        self.assertRaises(ValueError, getNbMinesGrilleDemineur, 100)

    @unittest.skipIf("getMinesRestantesGrilleDemineur" not in globals(), "Fonction getMinesRestantesGrilleDemineur non écrite.")
    def test_getMinesRestantesGrilleDemineur(self):
        for _ in range(500):
            nl = randint(4, 10)
            nc = randint(4, 10)
            # Contruction d'une grille à la main : A NE PAS FAIRE !
            grille = [[{const.CONTENU: 0, const.VISIBLE: False, const.ANNOTATION: None} for _j in range(nc)] for _i in range(nl)]
            # Déterminer aléatoirement un nombre de mines
            nb_mines = randint(0, nl*nc - 10)
            coords = [(_n // nc, _n % nc) for _n in range(nl*nc)]
            shuffle(coords)
            for i in range(nb_mines):
                grille[coords[i][0]][coords[i][1]][const.CONTENU] = const.ID_MINE
            # Déterminer aléatoirement un nombre de drapeaux
            nb_flags = randint(0, nl*nc - 10)
            shuffle(coords)
            for i in range(nb_flags):
                grille[coords[i][0]][coords[i][1]][const.ANNOTATION] = const.FLAG
            n = getMinesRestantesGrilleDemineur(grille)
            self.assertEqual(nb_mines - nb_flags, n,
                             f"Dans la grille {grille}, on a {nb_mines} mines et {nb_flags} drapeaux. Il reste donc {nb_mines - nb_flags} mines au lieu de {n} retourné par la fonction getMinesRestantesGrilleDemineur")

    @unittest.skipIf("gagneGrilleDemineur" not in globals(), "Fonction gagneGrilleDemineur non écrite.")
    def test_gagneGrilleDemineur(self):
        for _ in range(100):
            nl = randint(4, 10)
            nc = randint(4, 10)
            # Contruction d'une grille à la main : A NE PAS FAIRE !
            grille = [[{const.CONTENU: 0, const.VISIBLE: False, const.ANNOTATION: None} for _j in range(nc)] for _i in range(nl)]
            # Déterminer aléatoirement un nombre de mines
            nb_mines = randint(5, nl*nc - 10)
            coords = [(_n // nc, _n % nc) for _n in range(nl*nc)]
            shuffle(coords)
            c_mines = set(coords[0:nb_mines])
            for c in c_mines:
                grille[c[0]][c[1]][const.CONTENU] = const.ID_MINE
                grille[c[0]][c[1]][const.ANNOTATION] = const.FLAG
            c_other = set(coords) - c_mines
            # Situation gagnante
            for c in c_other:
                grille[c[0]][c[1]][const.VISIBLE] = True
            self.assertTrue(gagneGrilleDemineur(grille), f"La grille {self.__print__(grille)} devrait être gagnante")
            # Situation non gagnante : cases non découvertes
            l_other = list(c_other)
            for _ in range(5):
                shuffle(l_other)
                _l_other = l_other[0:randint(1, len(l_other) - 1)]
                for c in _l_other:
                    grille[c[0]][c[1]][const.VISIBLE] = False
                self.assertFalse(gagneGrilleDemineur(grille), f"La grille {self.__print__(grille)} ne devrait pas être gagnante")
                for c in _l_other:
                    grille[c[0]][c[1]][const.VISIBLE] = True
            # Situation non gagnante : une bombe a été découverte
            l_mines = list(c_mines)
            for _ in range(5):
                c = l_mines[randint(0, len(l_mines) - 1)]
                grille[c[0]][c[1]][const.VISIBLE] = True
                self.assertFalse(gagneGrilleDemineur(grille), f"La grille {self.__print__(grille)} ne devrait pas être gagnante")
                grille[c[0]][c[1]][const.VISIBLE] = False
    @unittest.skipIf("gagneGrilleDemineur" not in globals(), "Fonction gagneGrilleDemineur non écrite.")
    def test_OPTION_gagneGrilleDemineur(self):
        for _ in range(100):
            nl = randint(4, 10)
            nc = randint(4, 10)
            # Contruction d'une grille à la main : A NE PAS FAIRE !
            grille = [[{const.CONTENU: 0, const.VISIBLE: False, const.ANNOTATION: None} for _j in range(nc)] for _i in range(nl)]
            # Déterminer aléatoirement un nombre de mines
            nb_mines = randint(5, nl*nc - 10)
            coords = [(_n // nc, _n % nc) for _n in range(nl*nc)]
            shuffle(coords)
            c_mines = set(coords[0:nb_mines])
            for c in c_mines:
                grille[c[0]][c[1]][const.CONTENU] = const.ID_MINE
                grille[c[0]][c[1]][const.ANNOTATION] = const.FLAG
            # Situation non gagnante : une bombe n'a pas son drapeau
            l_mines = list(c_mines)
            for _ in range(5):
                c = l_mines[randint(0, len(l_mines) - 1)]
                grille[c[0]][c[1]][const.ANNOTATION] = None
                self.assertFalse(gagneGrilleDemineur(grille), f"La grille {self.__print__(grille)} ne devrait pas être gagnante")
                grille[c[0]][c[1]][const.ANNOTATION] = const.FLAG

    @unittest.skipIf("perduGrilleDemineur" not in globals(), "Fonction perduGrilleDemineur non écrite.")
    def test_perduGrilleDemineur(self):
        for _ in range(100):
            nl = randint(4, 10)
            nc = randint(4, 10)
            # Contruction d'une grille à la main : A NE PAS FAIRE !
            grille = [[{const.CONTENU: 0, const.VISIBLE: False, const.ANNOTATION: None} for _j in range(nc)] for _i in range(nl)]
            # Déterminer aléatoirement un nombre de mines
            nb_mines = randint(5, nl*nc - 10)
            coords = [(_n // nc, _n % nc) for _n in range(nl*nc)]
            shuffle(coords)
            c_mines = set(coords[0:nb_mines])
            for c in c_mines:
                grille[c[0]][c[1]][const.CONTENU] = const.ID_MINE
            c_other = set(coords) - c_mines
            # Situation gagnante
            for c in c_other:
                grille[c[0]][c[1]][const.VISIBLE] = True
            self.assertFalse(perduGrilleDemineur(grille), f"La grille {self.__print__(grille)} ne devrait pas être perdue")
            # Situation non gagnante mais non perdue : cases non découvertes
            l_other = list(c_other)
            for _ in range(5):
                shuffle(l_other)
                _l_other = l_other[0:randint(1, len(l_other) - 1)]
                for c in _l_other:
                    grille[c[0]][c[1]][const.VISIBLE] = False
                self.assertFalse(perduGrilleDemineur(grille), f"La grille {self.__print__(grille)} ne devrait pas être perdue")
                for c in _l_other:
                    grille[c[0]][c[1]][const.VISIBLE] = True
            # Situation non gagnante et perdue : une bombe a été découverte
            l_mines = list(c_mines)
            for _ in range(5):
                c = l_mines[randint(0, len(l_mines) - 1)]
                grille[c[0]][c[1]][const.VISIBLE] = True
                self.assertTrue(perduGrilleDemineur(grille), f"La grille {self.__print__(grille)} devrait être perdue")
                grille[c[0]][c[1]][const.VISIBLE] = False
