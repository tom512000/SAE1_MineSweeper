import const

# Constantes concernant les Cellules du démineur
const.CONTENU = "Contenu"
# Une cellule peut être connue (visible) ou non
const.VISIBLE = "Visible"
# Une cellule peut, si elle n'est pas visible, être recouverte par :
# - un drapeau indiquant qu'elle contient une mine
# - un point d'interrogation indiquant qu'elle est susceptible de contenir une mine
# Constante pour mémoriser la "couverture" de la cellule
const.ANNOTATION = "Annotation"
# Constantes pour le drapeau, le point d'interrogation
const.FLAG = "Flag"
const.DOUTE = "Doute"
# Pour indiquer qu'il n'y a rien, on utilise None

# Le contenu d'une cellule du démineur est le nombre de mines qui sont voisines de la cellule.
# C'est un entier compris entre 0 et 8.
# Si la cellule contient la mine, par convention elle contiendra l'identifiant de la mine : ID_MINE
const.ID_MINE = -1

# Ajout de mes propres constantes
const.RESOLU = "Résolue"

