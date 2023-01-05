import unittest
import const

from Model.Cellule import *
from random import randint


class TestCelluleMethods(unittest.TestCase):

    @unittest.skipIf('isContenuCorrect' not in globals(), "isContenuCorrect non écrit")
    def test_isContenuCorrect(self):
        l_c = list(range(0, 9)) + [const.ID_MINE]
        for i in range(-20, 20):
            self.assertEqual(i in l_c, isContenuCorrect(i),
                             f"isContenuCorrect pour un contenu valant {i} devrait retourner {i in l_c}")

    @unittest.skipIf('isContenuCorrect' not in globals(), "isContenuCorrect non écrit")
    def test_OPTION_isContenuCorrect_False_due_to_TypeError(self):
        self.assertFalse(isContenuCorrect("Rien ne va plus !"))
        self.assertFalse(isContenuCorrect(5.2))
        self.assertFalse(isContenuCorrect([5]))

    @unittest.skipIf('construireCellule' not in globals(), "Constructeur non écrit")
    def test_construire_cellule(self):
        # On teste les valeurs possibles
        l_v = list(range(0, 9)) + [const.ID_MINE]
        for _v in l_v:
            c = construireCellule(_v, False)
            self.assertTrue(type_cellule(c),
                            f"Erreur sur la construction de cellule avec contenu = {c}, visible = True")
            c = construireCellule(_v, True)
            self.assertTrue(type_cellule(c),
                            f"Erreur sur la construction de cellule avec contenu = {c}, visible = True")

    @unittest.skipIf('construireCellule' not in globals(), "Constructeur non écrit")
    def test_construire_cellule_defaut(self):
        # On teste les constructeurs sans valeur
        # Attention, pas de getter...
        c = construireCellule()
        self.assertEqual(0, c[const.CONTENU], "Le constructeur par défaut devrait initialiser le contenu à 0")
        self.assertFalse(c[const.VISIBLE], "Le constructeur par défaut devrait initialiser la visibilité à False")
        c = construireCellule(5)
        self.assertEqual(5, c[const.CONTENU], "Constructeur : le contenu devrait valoir 5 !?")
        self.assertFalse(c[const.VISIBLE], "Le constructeur par défaut devrait initialiser la visibilité à False")

    @unittest.skipIf('construireCellule' not in globals(), "Constructeur non écrit")
    def test_OPTION_construire_cellule_raise_ValueError(self):
        # Valeurs autorisées
        l_a = list(range(0, 9)) + [const.ID_MINE]
        for v in range(-10, 20):
            if v in l_a:
                self.assertTrue(type_cellule(construireCellule(v, False)))
            else:
                self.assertRaises(ValueError, construireCellule, v, False)

    @unittest.skipIf('construireCellule' not in globals(), "Constructeur non écrit")
    def test_OPTION_construire_cellule_raise_TypeError(self):
        self.assertRaises(TypeError, construireCellule, 0, 5)
        self.assertRaises(TypeError, construireCellule, 0, 55.4)
        self.assertRaises(TypeError, construireCellule, 0, [5])


    @unittest.skipIf('construireCellule' not in globals() or 'getContenuCellule' not in globals(),
                     "Constructeur ou getContenuCellule non écrit")
    def test_getContenuCellule(self):
        # Valeurs autorisées
        l_a = list(range(0, 9)) + [const.ID_MINE]
        for v in l_a:
            c = construireCellule(v, False)
            self.assertEqual(v, getContenuCellule(c), "Erreur sur getContenuCellule")

    @unittest.skipIf('construireCellule' not in globals() or 'getContenuCellule' not in globals(),
                     "Constructeur ou getContenuCellule non écrit")
    def test_OPTION_getContenuCellule_raise_TypeError(self):
        # Test avec autre chose qu'une cellule
        self.assertRaises(TypeError, getContenuCellule, "Rien ne va plus !")
        self.assertRaises(TypeError, getContenuCellule, 12)
        self.assertRaises(TypeError, getContenuCellule, [12, False])

    @unittest.skipIf('construireCellule' not in globals() or 'isVisibleCellule' not in globals(),
                     "Constructeur ou isVisibleCellule non écrit")
    def test_isVisibleCellule(self):
        # Test avec les deux valeurs possibles
        c = construireCellule(visible=True)

    @unittest.skipIf('construireCellule' not in globals() or 'isVisibleCellule' not in globals(),
                     "Constructeur ou isVisibleCellule non écrit")
    def test_OPTION_isVisibleCellule_raise_TypeError(self):
        # Test avec autre chose qu'une cellule
        self.assertRaises(TypeError, isVisibleCellule, "Rien ne va plus !")
        self.assertRaises(TypeError, isVisibleCellule, 12)
        self.assertRaises(TypeError, isVisibleCellule, [12, False])

    @unittest.skipIf('construireCellule' not in globals() or 'setContenuCellule' not in globals()
        or 'getContenuCellule' not in globals(),
                     "Constructeur ou setContenuCellule non écrit")
    def test_setContenuCellule(self):
        l_v = list(range(0, 9)) + [const.ID_MINE]
        c = construireCellule()
        for v in l_v:
            setContenuCellule(c, v)
            self.assertEqual(v, getContenuCellule(c), "Problème avec le setter")
            setContenuCellule(c, 0)

    @unittest.skipIf('construireCellule' not in globals() or 'setContenuCellule' not in globals(),
                     "Constructeur ou setContenuCellule non écrit")
    def test_setContenuCellule_raise_ValueError(self):
        l_v = list(range(0, 9)) + [const.ID_MINE]
        c = construireCellule()
        # Test du raise ValueError
        for v in range(-20, 20):
            if v not in l_v:
                self.assertRaises(ValueError, setContenuCellule, c, v)

    @unittest.skipIf('construireCellule' not in globals() or 'setContenuCellule' not in globals(),
                     "Constructeur ou setContenuCellule non écrit")
    def test_OPTION_setContenuCellule_raise_TypeError(self):
        self.assertRaises(TypeError, setContenuCellule, "Rien ne va plus...", 5)
        self.assertRaises(TypeError, setContenuCellule, 15, 5)
        self.assertRaises(TypeError, setContenuCellule, [5, False], 5)

    @unittest.skipIf('construireCellule' not in globals() or 'setContenuCellule' not in globals(),
                     "Constructeur ou setContenuCellule non écrit")
    def test_OPTION_setContenuCellule_raise_Error_type_value(self):
        c = construireCellule()
        self.assertRaises(TypeError, setContenuCellule, c, True)
        self.assertRaises(TypeError, setContenuCellule, c, 13.5)
        self.assertRaises(TypeError, setContenuCellule, c, [1])

    @unittest.skipIf('construireCellule' not in globals() or 'isVisibleCellule' not in globals() or
                     'setVisibleCellule' not in globals(),
                     "Constructeur, isVisibleCellule ou setVisibleCellule non écrit")
    def test_setVisibleCellule(self):
        c = construireCellule()
        setVisibleCellule(c, True)
        self.assertTrue(isVisibleCellule(c))
        setVisibleCellule(c, False)
        self.assertFalse(isVisibleCellule(c))

    @unittest.skipIf('construireCellule' not in globals() or 'isVisibleCellule' not in globals() or
                     'setVisibleCellule' not in globals(),
                     "Constructeur, isVisibleCellule ou setVisibleCellule non écrit")
    def test_OPTION_setVisibleCellule_raise_type_Cellule(self):
        c = construireCellule()
        self.assertRaises(TypeError, isVisibleCellule, "Rien ne va plus !", True)
        self.assertRaises(TypeError, isVisibleCellule, 12, True)
        self.assertRaises(TypeError, isVisibleCellule, [12, 20], True)

    @unittest.skipIf('construireCellule' not in globals() or 'isVisibleCellule' not in globals() or
                     'setVisibleCellule' not in globals(),
                     "Constructeur, isVisibleCellule ou setVisibleCellule non écrit")
    def test_OPTION_setVisibleCellule_raise_type_bool(self):
        c = construireCellule()
        self.assertRaises(TypeError, isVisibleCellule, c, "Rien ne va plus !")
        self.assertRaises(TypeError, isVisibleCellule, c, 12)
        self.assertRaises(TypeError, isVisibleCellule, c, [12])

    @unittest.skipIf('construireCellule' not in globals() or 'contientMineCellule' not in globals(),
                     "Constructeur ou contientMineCellule non écrit")
    def test_contientMineCellule(self):
        cell = construireCellule(const.ID_MINE, False)
        self.assertTrue(contientMineCellule(cell))
        cell = construireCellule(const.ID_MINE, True)
        self.assertTrue(contientMineCellule(cell))
        for c in range(0, 9):
            cell = construireCellule(c, False)
            self.assertFalse(contientMineCellule(cell))
            cell = construireCellule(c, True)
            self.assertFalse(contientMineCellule(cell))

    @unittest.skipIf('construireCellule' not in globals() or 'contientMineCellule' not in globals(),
                     "Constructeur ou contientMineCellule non écrit")
    def test_OPTION_contientMineCellule_raise_TypeError(self):
        self.assertRaises(TypeError, contientMineCellule, "Rien ne va plus")
        self.assertRaises(TypeError, contientMineCellule, 12)
        self.assertRaises(TypeError, contientMineCellule, [12])

    @unittest.skipIf('isAnnotationCorrecte' not in globals(), "isAnnotationCorrecte non écrite.")
    def test_isAnnotationCorrecte(self):
        self.assertTrue(isAnnotationCorrecte(None), "None est une annotation !")
        self.assertTrue(isAnnotationCorrecte(const.DOUTE), f"{const.DOUTE} est une annotation !")
        self.assertTrue(isAnnotationCorrecte(const.FLAG), f"{const.FLAG} est une annotation !")
        self.assertFalse(isAnnotationCorrecte("Autre"), "'Autre' n'est pas une annotation !")
        self.assertFalse(isAnnotationCorrecte(0), "'0' n'est pas une annotation !")

    @unittest.skipIf('getAnnotationCellule' not in globals(), "getAnnotationCellule non écrite.")
    def test_getAnnotationCellule(self):
        cell = {const.CONTENU: 0, const.VISIBLE: False, const.ANNOTATION: None}
        self.assertEqual(None, getAnnotationCellule(cell), f"La cellule {cell} contient l'annotation None et non {getAnnotationCellule(cell)}")
        cell[const.ANNOTATION] = const.DOUTE;
        self.assertEqual(const.DOUTE, getAnnotationCellule(cell), f"La cellule {cell} contient l'annotation {const.DOUTE} et non {getAnnotationCellule(cell)}")
        cell[const.ANNOTATION] = const.FLAG
        self.assertEqual(const.FLAG, getAnnotationCellule(cell), f"La cellule {cell} contient l'annotation {const.FLAG} et non {getAnnotationCellule(cell)}")

    @unittest.skipIf('getAnnotationCellule' not in globals(), "getAnnotationCellule non écrite.")
    def test_OPTION_getAnnotationCellule_sans_annotation(self):
        cell = {const.CONTENU: 0, const.VISIBLE: False}
        self.assertEqual(None, getAnnotationCellule(cell))

    @unittest.skipIf('getAnnotationCellule' not in globals(), "getAnnotationCellule non écrite.")
    def test_OPTION_getAnnotationCellule_raise_TypeError(self):
        self.assertRaises(TypeError, getAnnotationCellule, "N'importe quoi !")
        self.assertRaises(TypeError, getAnnotationCellule, 10)
        self.assertRaises(TypeError, getAnnotationCellule, [1, 2, 3])

    @unittest.skipIf('changeAnnotationCellule' not in globals(), "changeAnnotationCellule non écrite.")
    def test_changeAnnotationCellule(self):
        cycle = [None, const.FLAG, const.DOUTE]
        for i in range(10):
            dep = randint(0, 2)
            cell = {const.CONTENU: 0, const.VISIBLE: False, const.ANNOTATION: cycle[dep]}
            for j in range(1, 7):
                changeAnnotationCellule(cell)
                self.assertEqual(cycle[(dep+j) % 3], cell[const.ANNOTATION],
                                 f"Après l'annotation {cycle[(dep+j-1) % 3]}, on devrait avoir {cycle[(dep+j) % 3]} au lieu de {cell[const.ANNOTATION]}")

    @unittest.skipIf('changeAnnotationCellule' not in globals(), "changeAnnotationCellule non écrite.")
    def test_OPTION_changeAnnotationCellule_raise_TypeError(self):
        self.assertRaises(TypeError, changeAnnotationCellule, "N'importe quoi !")
        self.assertRaises(TypeError, changeAnnotationCellule, 10)
        self.assertRaises(TypeError, changeAnnotationCellule, [1, 2, 3])

