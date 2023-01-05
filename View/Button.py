import pygame

from View.images import Image


class Button:
    # Différents états du bouton
    COVERED = "Covered"
    PRESSED = "Pressed"

    """
    Création d'un bouton

    :param screen: écran où s'affiche le bouton
    :param pos: Position (x, y) où afficher le bouton
    :param images: Liste de 3 images à utiliser pour afficher le bouton (0: image de base, 1: image lorsqu'on clique
    sur le bouton, 2: image lorsque la souris survole le bouton)
    Les images 1 et 2 sont facultatives.
    :param params: Paramètres à fournir à l'appel des fonctions lors du changement d'état du bouton
    :param onClicked: Fonction à appeler lorsque l'utilisateur clique sur le bouton
    :param onPressed: Fonction à appeler lorsque l'utilisateur appuie sur le bouton
    :param onReleased: Fonction à appeler lorsque l'utilisateur relâche le bouton
    :param visible: Détermine si on doit afficher le bouton ou non
    """
    def __init__(self, screen: pygame.Surface, pos: tuple, images: list, params: object = None,
                 onClicked: callable = None,
                 onPressed: callable = None,
                 onReleased: callable = None,
                 visible: bool = True):
        self.screen = screen
        self.pos = pos
        self.images = images
        self.params = params
        self.onClicked = onClicked
        self.onPressed = onPressed
        self.onReleased = onReleased
        # print(pos, type(pos), images[0], type(images[0]))
        self.rect = pygame.Rect(pos, (images[0].get_width(), images[0].get_height()))

        self.state = None
        if visible:
            self.refresh()

    def copy_to(self, pos: tuple, params: object, visible: bool = True) -> object:
        """
        Crée une copie du bouton à la position donnée

        :param pos: Position de la copie du bouton
        :param params: Paramètre à passer aux fonctions...
        :param visible: Détermine si on affiche le bouton ou non
        :return: Copie du bouton
        """
        but = Button(screen=self.screen, pos=pos, images=self.images, params=params,
                     onClicked= self.onClicked, onPressed= self.onPressed,
                     onReleased= self.onReleased, visible=visible)
        but.rect = pygame.Rect(pos, (but.get_width(), but.get_height()))
        return but

    def refresh(self) -> None:
        nb = len(self.images)
        if nb:
            if self.state is None:
                self.screen.blit(self.images[0], self.pos)
            elif self.state == Button.COVERED:
                self.screen.blit(self.images[2] if nb > 2 else self.images[0], self.pos)
            elif self.state == Button.PRESSED:
                self.screen.blit(self.images[1] if nb > 1 else self.images[0], self.pos)

    def set_image_up(self, img: pygame.image):
        if self.images[0] != img:
            self.images[0] = img
            if self.state is None:
                self.refresh()

    def set_image_down(self, img: pygame.image):
        if len(self.images) > 1 and self.images[1] != img or len(self.images) == 1:
            if len(self.images) > 1:
                self.images[1] = img
            else:
                self.images.append(img)
            if self.state == Button.PRESSED:
                self.refresh()

    def set_image_over(self, img: pygame.image):
        modified = True
        if len(self.images) == 1:
            self.images.append(self.images[0])
            self.images.append(img)
        elif len(self.images) == 2:
            self.images.append(img)
        elif self.images[2] != img:
            self.images[2] = img
        else:
            modified = False
        if modified and self.state == Button.COVERED:
            self.refresh()

    def set_images(self, imgs: list):
        self.images = imgs.copy()
        self.refresh()

    def mouse_button_down(self, pos: tuple, button: int, touch: int) -> bool:
        if self.rect.collidepoint(pos):
            # print(f"Press in {pos} - {self.params}, bouton {button}, touch {touch}")
            self.state = Button.PRESSED
            if self.onPressed:
                self.onPressed(self.params, button)
            self.refresh()
            return True
        return False

    def mouse_button_up(self, pos: tuple, button: int, touch: int) -> bool:
        if self.rect.collidepoint(pos):
            # print(f"Release in {pos} - {self.params}, bouton {button}, touch {touch}")
            if self.state == Button.PRESSED:
                if self.onReleased:
                    # print(": calling onReleased")
                    self.onReleased(self.params, button)
                if self.onClicked:
                    # print(": calling onClicked")
                    self.onClicked(self.params, button)
            if self.state != Button.COVERED:
                self.state = Button.COVERED
                self.refresh()
                return True
        elif self.state == Button.PRESSED:
            # print(f"Release outside ! - {self.params}")
            if self.onReleased:
                self.onReleased(self.params, button)
            self.state = None
            self.refresh()
            return True
        return False

    def mouse_move(self, pos: tuple, buttons: int, touch: int) -> bool:
        if sum(buttons):
            return False
        if self.rect.collidepoint(pos):
            if self.state != Button.COVERED:
                # print(f"Move in {pos} - {self.params}, boutons {buttons}, touch {touch}")
                self.state = Button.COVERED
                self.refresh()
                return True
        elif self.state == Button.COVERED:
            self.state = None
            self.refresh()
            return True
        return False

    def get_width(self) -> int:
        return self.images[0].get_width()

    def get_height(self) -> int:
        return self.images[0].get_height()

    def set_state(self, n: int):
        self.images = [Image.get_cell(n)]
        self.refresh()

    def set_mine(self):
        self.images = [Image.get_cell_mine()]
        self.refresh()

    def set_flag(self):
        self.images = [Image.get_cell_flag()]
        self.refresh()

    def set_doubt(self):
        self.images = [Image.get_cell_doubt(), Image.get_cell_doubt(), Image.get_cell_doubt(True)]
        self.refresh()

    def set_none(self):
        self.images = [Image.get_cell_up(), Image.get_cell_down(), Image.get_cell_over()]
        self.refresh()
