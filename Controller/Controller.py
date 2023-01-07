from random import randint
from Model.Constantes import *

from Model.GrilleDemineur import *


def __changeAnnotationCellule(c: dict) -> None:
    print("Fonction changeAnnotationCellule manquante !")
    return None


def __contientMineCellule(cell: dict) -> bool:
    print("Fonction contientMineCellule manquante !")
    return False


def __decouvrirGrilleDemineur(g: list, coord: tuple) -> list:
    print("Fonction decouvrirGrilleDemineur manquante.")
    if "setVisibleGrilleDemineur" in globals():
        setVisibleGrilleDemineur(g, coord, True)
    else:
        print("Fonction setVisibleGrilleDemineur manquante.")
    return [coord]


def __gagneGrilleDemineur(g: list) -> bool:
    print("Fonction gagneGrilleDemineur manquante !")
    return False


def __getAnnotationCellule(cell: dict) -> str:
    print("Fonction getAnnotationCellule manquante !")
    return None


def __getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    print("Fonction getAnnotationGrilleDemineur manquante !")
    return None


def __getCelluleGrilleDemineur(g: list, coord: tuple) -> dict:
    print("Fonction getCelluleGrilleDemineur manquante !")
    return None


def __getContenuGrilleDemineur(g: list, coord: tuple) -> int:
    print("Fonction getContenuGrilleDemineur manquante !")
    return 0


def __getMinesRestantesGrilleDemineur(g: list) -> int:
    print("Fonction getMinesRestantesGrilleDemineur manquante !")
    return 0


def __getNbMinesGrilleDemineur(g: list) -> int:
    print("Fonction getNbMinesGrilleDemineur manquante !")
    return 0


def __isVisibleCellule(cell: dict) -> bool:
    print("Fonction isVisibleCellule manquante !")
    return False


def __isVisibleGrilleDemineur(g: list, coord: tuple) -> bool:
    print("Fonction isVisibleFrilleDemineur manquante !")
    return False


def __perduGrilleDemineur(grille: list) -> bool:
    print("Fonction perduGrilleDemineur manquante.")
    return False


def __placerMinesGrilleDemineur(g: list, nb: int, coord: tuple) -> None:
    print("Fonction placerMinesGrilleDemineur manquante !")
    return None


def __reinitialiserGrilleDemineur(g: list) -> None:
    print("Fonction reinitialiserGrilleDemineur manquante !")
    return None


def __setVisibleCellule(cell: dict) -> None:
    print("Fonction setVisibleCellule manquante !")
    return None


def __simplifierGrilleDemineur(grille: list, coord: tuple) -> set:
    print("Fonction simplifierGrilleDemineur manquante.")
    return set()


def __simplifierToutGrilleDemineur(grille: list) -> tuple:
    print("Fonction simplifierToutGrilleDemineur manquante.")
    return set(), set()


def load_function(name: str) -> callable:
    if name in globals():
        return globals()[name]
    name = '__' + name
    if name not in globals():
        print(f"Implementation Error : {name} not defined")
        raise ModuleNotFoundError(name)
    return globals()[name]


class Controller:

    def __init__(self, lines: int, columns: int):
        self.win = None
        self.demineur = construireGrilleDemineur(lines, columns) if "construireGrilleDemineur" in globals() else None
        self.mines_placed = False
        self.end = False

        # Récupération des méthodes existantes
        # et remplacement par des méthodes par défaut si non existantes
        self.changeAnnotationCellule = load_function("changeAnnotationCellule")
        self.contientMineCellule = load_function("contientMineCellule")
        self.decouvrirGrilleDemineur = load_function("decouvrirGrilleDemineur")
        self.gagneGrilleDemineur = load_function("gagneGrilleDemineur")
        self.getAnnotationCellule = load_function("getAnnotationCellule")
        self.getAnnotationGrilleDemineur = load_function("getAnnotationGrilleDemineur")
        self.getCelluleGrilleDemineur = load_function("getCelluleGrilleDemineur")
        self.getContenuGrilleDemineur = load_function("getContenuGrilleDemineur")
        self.getMinesRestantesGrilleDemineur = load_function("getMinesRestantesGrilleDemineur")
        self.getNbMinesGrilleDemineur = load_function("getNbMinesGrilleDemineur")
        self.isVisibleCellule = load_function("isVisibleCellule")
        self.isVisibleGrilleDemineur = load_function("isVisibleGrilleDemineur")
        self.perduGrilleDemineur = load_function("perduGrilleDemineur")
        self.placerMinesGrilleDemineur = load_function("placerMinesGrilleDemineur")
        self.reinitialiserGrilleDemineur = load_function("reinitialiserGrilleDemineur")
        self.setVisibleCellule = load_function("setVisibleCellule")
        self.simplifierGrilleDemineur = load_function("simplifierGrilleDemineur")
        self.simplifierToutGrilleDemineur = load_function("simplifierToutGrilleDemineur")

    def set_win(self, win: object):
        self.win = win

    def on_pressed(self, params: tuple, button: int) -> None:
        # print(f"Pressed on {params}")
        if self.end or self.isVisibleGrilleDemineur(self.demineur, params):
            return
        self.win.is_guessing()

    def on_released(self, params: tuple, button: int) -> None:
        # print(f"Released on {params}")
        if self.end or self.isVisibleGrilleDemineur(self.demineur, params):
            return
        self.win.guessing_done();

    def on_clicked(self, params: tuple, button: int) -> None:
        if self.end:
            return
        # print(f"Clicked on {params}")
        cell = self.getCelluleGrilleDemineur(self.demineur, params)
        print("Cellule cliquée :", cell, "bouton :", button)
        if self.isVisibleCellule(cell) and button in [1, 3]:
            return
        if button == 1 and self.getAnnotationCellule(cell) != const.FLAG:
            # print("...")
            if not self.mines_placed:
                self.placerMinesGrilleDemineur(self.demineur, 40, params)
                # print("Mines placées dans le modèle")
                n = self.getNbMinesGrilleDemineur(self.demineur)
                # print('Nombre de mines calculé...')
                self.win.set_mines_count(n)
                # print('Set Mines Count')
                self.mines_placed = True
                self.win.start_clock()
                # print('Clock started')
            if self.contientMineCellule(cell):
                self.win.set_mine(params)
                self.setVisibleCellule(cell, True)
                self.end = True
                self.win.stop_clock()
                print("Mine displayed !! Game Lost !!!")
            else:
                # Debug
                _cell = self.getCelluleGrilleDemineur(self.demineur, params)
                print(_cell)
                # End Debug
                lst = self.decouvrirGrilleDemineur(self.demineur, params)
                # print('updating', lst)
                self.update_content_cells(lst)
        elif button == 3:
            self.changeAnnotationCellule(cell)
            a = self.getAnnotationCellule(cell)
            if a is None:
                self.win.set_none(params)
            elif a == const.DOUTE:
                self.win.set_doubt(params)
            else:
                self.win.set_flag(params)
                self.verify_win_status()
            self.win.set_mines_count(self.getMinesRestantesGrilleDemineur(self.demineur))
        elif button == 2:
            lst = self.simplifierGrilleDemineur(self.demineur, params)
            self.update_content_cells(lst)
        elif button == 5:
            lst_content, lst_flag = self.simplifierToutGrilleDemineur(self.demineur)
            self.update_content_cells(lst_content)
            self.update_flag_cells(lst_flag)
        print("Etat final de la cellule :", cell)
        # n = randint(0, 10)
        # if n <= 8:
        #     self.win.set_state(params, n)
        #     print("Number of mines displayed.")
        # elif n == 9:
        #     self.win.set_mine(params)
        #     print("Mine displayed !!")
        # else:
        #     self.win.set_won()
        #     print("Won !!!")

    def update_content_cells(self, lst):
        for coord in lst:
            self.win.set_state(coord, self.getContenuGrilleDemineur(self.demineur, coord))
        # print('Testing win and lost status')
        if not self.verify_win_status() and self.perduGrilleDemineur(self.demineur):
            self.stop_playing()
        # print('Ended !')
        # print("Perdu ?", self.perduGrilleDemineur(self.demineur))

    def update_flag_cells(self, lst):
        for coord in lst:
            a = self.getAnnotationGrilleDemineur(self.demineur, coord)
            if a is None:
                self.win.set_none(coord)
            elif a == const.DOUTE:
                self.win.set_doubt(coord)
            else:
                self.win.set_flag(coord)
                self.win.set_mines_count(self.getMinesRestantesGrilleDemineur(self.demineur))
        if not self.verify_win_status() and self.perduGrilleDemineur(self.demineur):
            self.stop_playing()
        # print("Perdu ?", self.perduGrilleDemineur(self.demineur))

    def stop_playing(self):
        self.win.stop_clock()
        self.end = True

    def verify_win_status(self) -> bool:
        if self.gagneGrilleDemineur(self.demineur):
            self.stop_playing()
            self.win.set_won()
            print("Game Won !!!")
            return True
        return False

    def on_play(self, param: object, button: int) -> None:
        # print("Bouton play appuyé...")
        self.mines_placed = False
        self.end = False
        self.reinitialiserGrilleDemineur(self.demineur)
        self.win.reset()
