import pygame

# Partie chargement des images
# Récupération des noms des cellules du démineur
# ==============================================
# Nom des images brutes


class Image:
    img_cells_over = None
    img_cells = None
    img_btns = None
    img_digits = None
    img_digits_dots = None
    sources = 'Images/Normal/'

    @staticmethod
    def load_images():
        Image.img_cells_over = ['cell_' + str(i) for i in range(0, 9)] + \
                               ['cell_doubt', 'cell_flag', 'cell_up']
        Image.img_cells = Image.img_cells_over + ['cell_down', 'cell_mine']
        cells_name = Image.img_cells.copy()
        Image.img_cells_over = [n + "_over" for n in Image.img_cells_over]
        cells_over_name = Image.img_cells_over.copy()
        # Formattage des noms : chemin + extension
        Image.img_cells = [Image.sources + img + '.png' for img in Image.img_cells]
        Image.img_cells_over = [Image.sources + img + '.png' for img in Image.img_cells_over]

        IDX_CELL_UP = 11
        IDX_CELL_DOWN = 12

        # Récupération des noms des boutons
        # =================================
        Image.img_btns = ['btn_up', 'btn_down', 'btn_guess_down', 'btn_loose_up', 'btn_play_up', 'btn_win_up']
        btns_name = Image.img_btns.copy()
        # Formattage des noms :
        Image.img_btns = [Image.sources + img + '.png' for img in Image.img_btns]

        IDX_BTN_PLAY = 4

        # Gestion des affichages digitaux
        # ===============================
        Image.img_digits = ['digit_' + str(i) for i in range(0, 10)] + ['digit_none']
        #digits_name = Image.img_digits.copy()
        Image.img_digits = [Image.sources + t + '.png' for t in Image.img_digits]
        Image.img_digits_dots = ['digit_2dots_off', 'digit_2dots_on']
        #digits_dots_name = Image.img_digits_dots.copy()
        Image.img_digits_dots = [Image.sources + t + '.png' for t in Image.img_digits_dots]

        # Chargement des images et vérification...
        # ----------------------------------------
        Image.img_cells = [pygame.image.load(img) for img in Image.img_cells]
        Image.img_cells_over = [pygame.image.load(img) for img in Image.img_cells_over]
        Image.img_btns = [pygame.image.load(img) for img in Image.img_btns]
        Image.img_digits = [pygame.image.load(img) for img in Image.img_digits]
        Image.img_digits_dots = [pygame.image.load(img) for img in Image.img_digits_dots]

        # TODO : il faudra convertir (convert_alpha) une fois que la fenêtre sera créée...
        # Récupération et vérification des tailles des images
        # Cellules
        CELL_WIDTH = Image.img_cells[0].get_width()
        CELL_HEIGHT = Image.img_cells[0].get_height()
        # Toutes les cellules doivent avoir la même taille !
        for i, img in enumerate(Image.img_cells):
            if img.get_width() != CELL_WIDTH:
                raise Exception(f"L'image {cells_name[i]} du tableau img_cells a une largeur de {img.get_width()} au lieu de {CELL_WIDTH}")
            if img.get_height() != CELL_HEIGHT:
                raise Exception(f"L'image {cells_name[i]} du tableau img_cells a une hauteur de {img.get_height()} au lieu de {CELL_HEIGHT}")
        w = Image.img_cells_over[0].get_width()
        if w != CELL_WIDTH:
            raise Exception("Les images de couverture n'ont pas la même largeur que les images de cellules !")
        h = Image.img_cells_over[0].get_height()
        if h != CELL_HEIGHT:
            raise Exception("Les images de couverture n'ont pas la même hauteur que les images de cellules !")
        # Toutes les cellules doivent avoir la même taille !
        for i, img in enumerate(Image.img_cells_over):
            if img.get_width() != CELL_WIDTH:
                raise Exception(f"L'image {cells_over_name[i]} du tableau img_cells_over a une largeur de {img.get_width()} au lieu de {CELL_WIDTH}")
            if img.get_height() != CELL_HEIGHT:
                raise Exception(f"L'image {cells_over_name[i]} du tableau img_cells_over a une hauteur de {img.get_height()} au lieu de {CELL_HEIGHT}")
        # Boutons : Tous les boutons devient avoir la même hauteur
        BTN_HEIGHT = Image.img_btns[0].get_height()
        for i, img in enumerate(Image.img_btns):
            if img.get_height() != BTN_HEIGHT:
                raise Exception(f"Le bouton {btns_name[i]} a une hauteur de {img.get_height()} au lieu de {BTN_HEIGHT}")

    @staticmethod
    def get_margin() -> int:
        return 10 # 10 pixels de marge entre les composants

    @staticmethod
    def get_cell_width() -> int:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells[0].get_width()

    @staticmethod
    def get_cell_height() -> int:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells[0].get_height()

    @staticmethod
    def get_cell_up() -> pygame.image:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells[11]

    @staticmethod
    def get_cell_down() -> pygame.image:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells[12]

    @staticmethod
    def get_cell_over() -> pygame.image:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells_over[11]

    @staticmethod
    def get_cell_mine() -> pygame.image:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells[13]

    @staticmethod
    def get_cell(n: int, over: bool = False) -> pygame.image:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells_over[n] if over else Image.img_cells[n]

    @staticmethod
    def get_cell_flag(over: bool = False) -> pygame.image:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells_over[10] if over else Image.img_cells[10]

    @staticmethod
    def get_cell_doubt(over: bool = False) -> pygame.image:
        if Image.img_cells is None:
            Image.load_images()
        return Image.img_cells_over[9] if over else Image.img_cells[9]

    @staticmethod
    def get_button_height() -> int:
        if Image.img_btns is None:
            Image.load_images()
        return Image.img_btns[0].get_height()

    @staticmethod
    def get_btn_up() -> pygame.image:
        if Image.img_btns is None:
            Image.load_images()
        return Image.img_btns[0]

    @staticmethod
    def get_btn_down() -> pygame.image:
        if Image.img_btns is None:
            Image.load_images()
        return Image.img_btns[1]

    @staticmethod
    def get_btn_guess() -> pygame.image:
        if Image.img_btns is None:
            Image.load_images()
        return Image.img_btns[2]

    @staticmethod
    def get_btn_loose() -> pygame.image:
        if Image.img_btns is None:
            Image.load_images()
        return Image.img_btns[3]

    @staticmethod
    def get_btn_play() -> pygame.image:
        if Image.img_btns is None:
            Image.load_images()
        return Image.img_btns[4]

    @staticmethod
    def get_btn_win() -> pygame.image:
        if Image.img_btns is None:
            Image.load_images()
        return Image.img_btns[5]

    @staticmethod
    def get_digit_off() -> pygame.image:
        if Image.img_digits is None:
            Image.load_images()
        return Image.img_digits[10]

    @staticmethod
    def get_digit(n: int) -> pygame.image:
        if Image.img_digits is None:
            Image.load_images()
        return Image.img_digits[n]

    @staticmethod
    def get_digit_width() -> int:
        if Image.img_digits is None:
            Image.load_images()
        return Image.img_digits[0].get_width()

    @staticmethod
    def get_digit_height() -> int:
        if Image.img_digits is None:
            Image.load_images()
        return Image.img_digits[0].get_height()

    @staticmethod
    def get_digit_dots() -> pygame.image:
        if Image.img_digits_dots is None:
            Image.load_images()
        return Image.img_digits_dots[1]

    @staticmethod
    def get_digit_dots_off() -> pygame.image:
        if Image.img_digits_dots is None:
            Image.load_images()
        return Image.img_digits_dots[0]

    @staticmethod
    def get_digit_dots_width() -> int:
        if Image.img_digits_dots is None:
            Image.load_images()
        return Image.img_digits_dots[0].get_width()
