import unittest
from Model.Coordonnee import *


class TestCoordonnee(unittest.TestCase):
    @unittest.skipIf('construireCoordonnee' not in globals(), "Constructeur non écrit")
    def test_construireCoordonnee(self):
        coord = construireCoordonnee(2, 4)
        self.assertTrue(type_coordonnee(coord), "Problème avec le constructeur")

    @unittest.skipIf('construireCoordonnee' not in globals(), "Constructeur non écrit")
    def test_OPTION_construireCoordonnee_raise_TypeError(self):
        self.assertRaises(TypeError, construireCoordonnee, "Rien ne va plus !", 0)
        self.assertRaises(TypeError, construireCoordonnee, 0, "Rien ne va plus !")
        for i in range(-10, 0, -1):
            self.assertRaises(TypeError, construireCoordonnee(i, 0))
            self.assertRaises(TypeError, construireCoordonnee(0, i))

    @unittest.skipIf('construireCoordonnee' not in globals() or 'getLigneCoordonnee' not in globals(),
                     "Constructeur ou getLigneCoordonnee non écrit")
    def test_getLigneCoordonnee(self):
        for li in range(10):
            coord = construireCoordonnee(li, 0)
            self.assertEqual(li, getLigneCoordonnee(coord))

    @unittest.skipIf('construireCoordonnee' not in globals() or 'getLigneCoordonnee' not in globals(),
                     "Constructeur ou getLigneCoordonnee non écrit")
    def test_OPTION_getLigneCoordonnee_raise_TypeError(self):
        self.assertRaises(TypeError, getLigneCoordonnee, "Rien ne va plus !")
        self.assertRaises(TypeError, getLigneCoordonnee, [5, 4])

    @unittest.skipIf('construireCoordonnee' not in globals() or 'getColonneCoordonnee' not in globals(),
                     "Constructeur ou getColonneCoordonnee non écrit")
    def test_getColonneCoordonnee(self):
        for co in range(10):
            coord = construireCoordonnee(0, co)
            self.assertEqual(co, getColonneCoordonnee(coord))

    @unittest.skipIf('construireCoordonnee' not in globals() or 'getColonneCoordonnee' not in globals(),
                     "Constructeur ou getColonneCoordonnee non écrit")
    def test_OPTION_getColonneCoordonnee_raise_TypeError(self):
        self.assertRaises(TypeError, getColonneCoordonnee, "Rien ne va plus !")
        self.assertRaises(TypeError, getColonneCoordonnee, [5, 4])

