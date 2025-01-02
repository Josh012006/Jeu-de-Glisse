# Auteur 1: Josué Saint-Martin Junior (Matricule 20290870)
# Auteur 2: Kuza Twagiramungu (Matricule 20317467)
# Date: 01-11-2024

cyan = "#088"
blanc = "#fff"
vert = "#0f0"
rouge = "#f00"
gris = "#444"
noir = "#000"

px = 9            # unité de mesure en pixels
bloc = px + 1     # largeur en pixels d'une case de la grille



# La fonction creer_matrice prend en paramètre un entier n strictement positif
# et renvoie une matrice de dimension n x n dont toutes les valeurs sont 0.

def creer_matrice(n):
 
    tab = []
    for _ in range(n):
        tab.append([0] * n)
    return tab


# La procédure dessiner_grille prend en paramètre un entier positif qui
# représentela dimension de la grille et une couleur qui est gris par défaut.
# Elle affiche sur l'écran la grille principale du jeu en la couleur donnée.

def dessiner_grille(dimension, couleur=gris):
 
    largeur = bloc * dimension + 1

    for i in range(dimension + 1):
     
        # Coordonnées du début du trait.
     
        x = px
        y = px + bloc * i
         
        # Affichage du i-ième trait horizontal.
     
        fill_rectangle(x, y, largeur, 1, couleur)
     
        # Affichage du i-ième trait vertical.

        fill_rectangle(y, x, 1, largeur, couleur)


# La fonction creer_image prend en paramètre une couleur et une matrice qui
# représente un bitmap. Elle retourne une chaine de caractères qui est une
# image tirée du bitmap.

def creer_image(couleur, bitmap):
    image = ""
 
    # Nombre de lignes et de colonnes de la matrice.
 
    m = len(bitmap)
    n = len(bitmap[0])
 
    for i in range(m):
        for j in range(n):
            image += noir if bitmap[i][j] == 0 else couleur
        image += '\n' if i != (m - 1) else ''
   
    return image


# La procédure creer_jeton prend en paramètre une couleur et deux entiers x et
# y qui représentent une position sur la grille. Elle affiche un jeton de la
# couleur précisée à la position donnée.

def creer_jeton(x, y, couleur):
 
    jeton = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
 
    image = creer_image(couleur, jeton)
 
    draw_image(x, y, image)


# La fonction coor_fleche prend en paramètre un coup et un entier positif qui
# est la dimension de la grille. Elle retourne une structure avec des champs x
# et y qui représentent les coordonnées du coin supérieur gauche de la flèche.

def coor_fleche(coup, dimension):
 
    largeur = (dimension + 1) * bloc
 
    if coup.ligne.horiz:
        x = 0 if (not coup.fin) else largeur
        y = bloc * (coup.ligne.index + 1)
    else:
        x = bloc * (coup.ligne.index + 1)
        y = 0 if (not coup.fin) else largeur
 
    resultat = struct(x=x, y=y)
 
    return resultat


# La fonction rotation prend en paramètre une matrice binaire carrée
# bidimensionnelle. Elle retourne une nouvelle matrice qui est le résultat de
# la rotation d'angle 90° de la matrice initiale suivant le sens des aiguilles
# d'une montre.

def rotation(matrice):
   
    # Initialisation d'une matrice nulle de même taille que celle passée en
    # paramètre.
   
    taille = len(matrice)
    resultat = creer_matrice(taille)

    # Effectuer la rotation en considérant uniquement les 1.
   
    for i in range(taille):
        for j in range(taille):
            if matrice[i][j] == 1:
                resultat[j][taille-1-i] = 1
               
    return resultat


# La fonction repeter_rotation prend en paramètre une matrice bidirectionnelle
# et un entier positif n. Elle retourne une matrice qui correspond à la matrice
# initiale après avoir effectué une rotation de 90° dans le sens des aiguilles
# d'une montre n fois.

def repeter_rotation(matrice, n):
    tab = matrice.copy()
     
    for i in range(n):
        tab = rotation(tab)
   
    return tab


# La fonction bitmaps_fleches ne prend aucun paramètre. Elle retourne un
# tableau contenant les bitmaps de toutes les directions de flèche possibles.

def bitmaps_fleches():
   
    fleche_haut = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 1, 0, 1, 0, 1, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
   
    resultat = [fleche_haut]
   
    # Déduire chaque bitmap en appliquant une rotation sur la matrice
    # fleche_haut un certain nombre de fois.
   
    for i in range(1, 4):
        resultat.append(repeter_rotation(fleche_haut, i))

    return resultat
     
   
# La fonction code_fleche prend en paramètre un coup et retourne un entier qui
# est soit 0, 1, 2 ou 3. Il correspond au nombre de rotation qu'il faut
# appliquer sur la matrice fleche_haut pour obtenir la flèche liée au coup.
   
def code_fleche(coup):
   
    if coup.ligne.horiz:
        direction = 1 if (not coup.fin) else 3
    else:
        direction = 2 if (not coup.fin) else 0
   
    return direction

   
# La procédure creer_fleche prend en parametre un coup, la dimension de la
# grille, une couleur et une matrice bitmap_fleche. Elle affiche sur l'écran
# une flèche ayant la couleur précisée et dont la position et la direction
# représentent le coup associé et la bitmap donnée.

def creer_fleche(coup, dimension, couleur, bitmap_fleche):

    # Coordonnées de la flèche.
 
    fleche = coor_fleche(coup, dimension)
    x = fleche.x
    y = fleche.y
 
    image = creer_image(couleur, bitmap_fleche)
 
    draw_image(x, y, image)


# La fonction generer_coups prend en paramètre un entier positif qui est la
# dimension de la grille et retourne un tableau contenant tous les coups
# possibles du jeu.

def generer_coups(dimension):
 
    resultat = []

    for i in range(dimension):
        for j in range(4):
       
            # Créer deux coups verticaux et deux coups horizontaux pour
            # chaque index en instaurant une alternance entre les valeurs
            # horiz et fin.
       
            ligne = struct(index=i, horiz=(j<2))
            coup = struct(ligne=ligne, fin=(j%2==0))
     
            resultat.append(coup)
 
    return resultat


# La procédure afficher_fleches prend en paramètre un entier positif qui est la
# dimension de la grille et affiche toutes les flèches devant apparaître sur
# l'écran dans leur état initial.

def afficher_fleches(dimension):
   
    bitmaps =  bitmaps_fleches()
 
    coups = generer_coups(dimension)
   
    for coup in coups:
     
        # Afficher la flèche associée au coup.
       
        direction = code_fleche(coup)
        bitmap_fleche = bitmaps[direction]

        creer_fleche(coup, dimension, cyan, bitmap_fleche)


# La procédure survol prend en paramètre un entier positif qui est la dimension
# de la grille. Elle retourne le coup associé à une flèche si celle-ci est
# survolée.

def survol(dimension):
 
    souris = get_mouse()
    coups = generer_coups(dimension)
 
    for coup in coups:
   
        fleche = coor_fleche(coup, dimension)

        survoler_x = souris.x >= fleche.x and souris.x < (fleche.x + bloc)
        survoler_y = souris.y >= fleche.y and souris.y < (fleche.y + bloc)
 
        if survoler_x and survoler_y:
            return coup
 
    return None


# La procédure retablir_grille prend en paramètre un entier positif qui est la
# dimension de la grille. Elle affiche les flèches en cyan et les lignes en
# gris afin de revenir à l'état initial du jeu.

def retablir_grille(dimension):
   
    afficher_fleches(dimension)

    dessiner_grille(dimension)


# La procédure surbrillance prend en paramètre une ligne, la dimension de la
# grille et une couleur. Elle change en la couleur voulue la ligne donnée.

def surbrillance(ligne, dimension, couleur):
 
    # Les coordonnées du coin supérieur gauche de la ligne concernée.
 
    ref_x = px if ligne.horiz else bloc * (ligne.index) + px
    ref_y = bloc * (ligne.index) + px if ligne.horiz else px

    # Dessiner les 4 côtés de la ligne en la couleur donnée.

    largeur = bloc * dimension if ligne.horiz else bloc
    hauteur = bloc if ligne.horiz else bloc * dimension
 
    fill_rectangle(ref_x, ref_y, largeur + 1, 1, couleur)
    fill_rectangle(ref_x, ref_y, 1, hauteur + 1, couleur)
    fill_rectangle(ref_x + largeur, ref_y, 1, hauteur + 1, couleur)
    fill_rectangle(ref_x, ref_y + hauteur,largeur + 1, 1, couleur)


# La procédure surbrillance_coup prend en paramètre un coup et la dimension de
# la grille. Elle change en blanc la couleur de la flèche et de la ligne
# associées au coup.

def surbrillance_coup(coup, dimension, fleche=blanc, ligne=blanc):
   
    # Détermination de la bitmap.
   
    bitmaps =  bitmaps_fleches()
   
    direction = code_fleche(coup)
    bitmap_fleche = bitmaps[direction]
   
    # Mettre la flèche et la ligne en couleur.
   
    creer_fleche(coup, dimension, fleche, bitmap_fleche)
    surbrillance(coup.ligne, dimension, ligne)

   
# La procédure melodie_triste ne prend aucun paramètre. Elle joue une séquence
# de tonalités de fréquence 1000 Hz, 900 Hz, 800 Hz, 700 Hz, 600 Hz et 500 Hz
# d'une durée de 0.1 seconde chaque, et se terminant par une tonalité de 100 Hz
# pendant 0.75 seconde.

def melodie_triste():
 
    for frequence in range (1000, 400, -100):
        beep(0.1, frequence)
    beep(0.75, 100)


# La procédure melodie_joyeuse ne prend aucun paramètre. Elle joue une séquence
# de tonalités de fréquence 500 Hz, 600 Hz, 700 Hz, 800 Hz, 900 Hz d'une durée
# de 0.1 seconde chaque, suivi de 3 tonalités de 1000 Hz de durée 0.1 seconde
# séparées de silences de 0.1 seconde, et une tonalité finale de 1000 Hz de
# durée 0.4 seconde.

def melodie_joyeuse():
 
    for frequence in range (500, 1000, 100):
        beep(0.1, frequence)

    for i in range(3):
        beep(0.1, 1000)
        beep(0.1, 0)

    beep(0.4, 1000)


# La fonction lignes_completes prend en paramètre une matrice d'entiers qui
# représente une configuration de la grille du jeu. Elle retourne un tableau
# qui contient toutes les lignes ayant uniquement des jetons d'une même
# couleur.

def lignes_completes(grille):

    dimension = len(grille)
    resultat = []
 
    # Vérification des rangées.
 
    for i in range(dimension):
        element_1 = grille[i][0]
        if element_1 == 0:
            continue
     
        for j in range(1, dimension):
            if grille[i][j] != element_1:
                break
        else:
            ligne = struct(index=i, horiz=True)
            resultat.append(ligne)
     
    # Vérification des colonnes.
 
    for i in range(dimension):
        element_1 = grille[0][i]
        if element_1 == 0:
            continue
 
        for j in range(1, dimension):
            if grille[j][i] != element_1:
                break
        else:
            ligne = struct(index=i, horiz=False)
            resultat.append(ligne)
     
 
    return resultat


# La fonction repetition prend en paramètre une matrice d'entiers qui
# représente une configuration de la grille et un tableau de matrices. Elle
# retourne True si la matrice se retrouve dans le tableau et False si non.

def repetition(grille, tab):
 
    for matrice in tab:
        if grille == matrice:
            return True
    return False


# La fonction rechercher prend en paramètre un tableau et une valeur. Si la
# valeur se retrouve dans le tableau, elle renvoie l'index de sa première
# occurence. Dans le cas contraire, elle renvoie -1.

def rechercher(tab, valeur):
 
    for i in range(len(tab)):
        if tab[i] == valeur:
            return i
    return -1


# La procédure sauvegarde prend en paramètre un tableau, une valeur, un entier
# positif n et un booléen fin. Elle modifie le tableau de telle manière à
# ajouter la valeur à la fin ou au début selon le paramètre fin. Elle s'assure
# aussi que ledit tableau garde une taille inférieure ou égale à n.

def sauvegarde(tab, valeur, n, fin=False):
 
    tab.append(valeur) if fin else tab.insert(0, valeur)
 
    if len(tab) > n :
        tab.pop(0) if fin else tab.pop(-1)
     
         
# La procédure jouer_coup prend en paramètre une matrice d'entiers qui
# représente la grille de jeu, un coup et un entier joueur qui est soit 1 ou 2.
# Elle modifie la grille pour que son contenu corresponde à l'ajout d'un jeton
# tel qu'indiqué par le paramètre coup et le paramètre joueur.

def jouer_coup(grille, coup, joueur):
 
    dimension = len(grille)
 
    ligne = coup.ligne
 
    # Détermination des coordonnées pour le jeton à ajouter.
 
    if ligne.horiz:
        x = ligne.index
        y = 0 if not coup.fin else dimension - 1
    else:
        x = 0 if not coup.fin else dimension - 1
        y = ligne.index
 
 
    # Détermination du tableau de la grille dans lequel on doit ajouter le
    # jeton.
 
    if ligne.horiz:
        tab = grille[x]
    else:
        tab = []
        for i in range(dimension):
            tab.append(grille[i][y])
 
    if coup.fin:
        tab.reverse()
 
    # Ajout du jeton de telle manière à combler les cases vides s'il y en a et
    # à pousser le dernier jeton de la ligne sinon.
   
    index = rechercher(tab, 0)
    index_tranche = index + (1 if index != -1 else 0)
 
    tab_final = tab[0 : index_tranche] if index != -1 else tab.copy()
   
    sauvegarde(tab_final, joueur, len(tab_final))
 
    # Reconstitution de la ligne.
   
    if index != -1:
        reste = tab[index_tranche : ]
        tab_final.extend(reste)
 
    if coup.fin:
        tab_final.reverse()
 
    # Modification de la grille avec la ligne mise à jour.
 
    if ligne.horiz:
        grille[x] = tab_final
    else:
        for i in range(dimension):
            grille[i][y] = tab_final[i]


# La procédure schematiser_grille prend en paramètre une matrice d'entiers qui
# est la configuration actuelle de la grille. Elle place les jetons à l'endroit
# approprié sur l'écran.

def schematiser_grille(grille):
 
    dimension = len(grille)
 
    for x in range(dimension):
        for y in range(dimension):
       
            val = grille[x][y]
       
            if val == 0:
                continue
           
            jeton_x = bloc * (y + 1)
            jeton_y = bloc * (x + 1)
     
            couleur = rouge if val == 1 else vert
     
            creer_jeton(jeton_x, jeton_y, couleur)


# La fonction animation prend en paramètre un entier positif qui est la
# dimension de la grille. Elle attend le prochain clic de souris et retourne
# le coup joué tout en gardant la dynamique de jeu (surbrillance, sons, etc.).
# Cette fonction est inspirée de la fonction attendre_clic présente dans
# l'énoncé du TP.

def animation(dimension):
 
    coup_survole = None

    while True:  # attendre que le bouton ne soit plus pressé
   
        etat = get_mouse()
        if etat.button == 0: break  # fin d'attente lorsque bouton plus pressé
   
        retablir_grille(dimension)

    while True:  # attendre que le bouton soit pressé
   
        etat = get_mouse()
        if etat.button != 0: break  # fin d'attente lorsque bouton pressé
 
        coup_actuel = survol(dimension)
 
        if coup_actuel != None:
       
            surbrillance_coup(coup_actuel, dimension)
     
            if coup_actuel != coup_survole:
               
                retablir_grille(dimension)
                beep(0.025, 1500)
           
                coup_survole = coup_actuel

    return coup_actuel


# La fonction copie prend en paramètre une matrice d'entiers qui représente une
# configuration de la grille de jeu et renvoie une copie profonde de cette
# dernière.

def copie(matrice):
 
    tab = []
 
    for rangee in matrice:
        tab.append(rangee.copy())
   
    return tab


# La procédure recommencer_partie prend en unique paramètre un entier positif
# qui est la dimension de la grille et lance une nouvelle partie de jeu.

def recommencer_partie(dimension):
    sleep(3)
    glisse(dimension)
   
   
# La procédure victoire prend en paramètre une matice d'entiers positifs qui
# représente la grille de jeu. Elle vérifie si l'un des joueurs a gagné et
# joue une mélodie joyeuse et un encadrement de chaque rangée et colonne
# complétée par le joueur gagnant.
   
def victoire (grille):
   
    dimension = len(grille)
   
    tab_completes = lignes_completes(grille)

    # Lignes complètes pour chaque joueur

    completes_1 = []
    completes_2 = []

    for ligne in tab_completes:
   
        index = ligne.index
        jeton = grille[index][0] if ligne.horiz else grille[0][index]
   
        if jeton == 1:
            completes_1.append(ligne)
        else:
            completes_2.append(ligne)
       
       
    # Nombre de lignes complètes pour chaque joueur.  
       
    nb_1 = len(completes_1)
    nb_2 = len(completes_2)

    if nb_1 != nb_2:
   
        # Détermination du gagnant et de ses lignes complètes.
   
        gagnant = 1 if nb_1 > nb_2 else 2
        tab_gagnant = [completes_1, completes_2][gagnant - 1]
   
        couleur = rouge if gagnant == 1 else vert
   
        retablir_grille(dimension)   # pour la fluidité du jeu
   
        for ligne in tab_gagnant:
            surbrillance(ligne, dimension, couleur)
       
        melodie_joyeuse()
   
        recommencer_partie(dimension)

       
# La procédure defaite prend en paramètres une matice d'entiers positifs qui
# représente la grille de jeu, un tableau qui contient les anciennes
# configurations de la grille et un entier joueur qui est soit 1 ou 2. Elle
# joue une mélodie triste et dessine les lignes de la grille avec la couleur
# du gagnant si la configuration de la grille se répète.
       
def defaite(grille, configurations, joueur):
   
    dimension = len(grille)
   
    repeter = repetition(grille, configurations)

    if repeter:
   
        couleur_gagnant = rouge if joueur == 2 else vert
        dessiner_grille(dimension, couleur_gagnant)
   
        melodie_triste()
   
        recommencer_partie(dimension)
       
# La procédure glisse prend comme unique paramètre un entier positif qui est la
# dimension de la grille de jeu. Elle crée une grille de pixels de la bonne
# taille sur l'écran et fait l'exécution de parties du jeu dans une boucle sans
# fin.

def glisse(dimension):
 
    # Afficher l'écran.
 
    cote = (dimension + 2) * bloc - 1
    set_screen_mode(cote, cote, 4)
 
    # État initial du jeu.
 
    grille = creer_matrice(dimension)
 
    joueur = 1
    couleur = rouge if joueur == 1 else vert
    creer_jeton( 0, 0, couleur)
 
    dessiner_grille(dimension)
    afficher_fleches(dimension)
 
    configurations = []
 
    while True:
   
        coup_actuel = animation(dimension)
 
        if coup_actuel != None:
       
            beep(0.15, 2000)  # générer un bref bip lors du clic de souris

            jouer_coup(grille, coup_actuel, joueur)
            schematiser_grille(grille)  # adaptation de l'écran à la grille
       
            # Fluidité du jeu.
       
            creer_jeton(0, 0, noir)      
            sleep(0.2)

            # Vérification de la condition de victoire.
           
            victoire(grille)
   
            # Vérification de la condition de défaite.
     
            defaite(grille, configurations, joueur)        
       
            # Changement de joueur.
                 
            joueur = 2 if joueur == 1 else 1
            couleur = rouge if joueur == 1 else vert
            creer_jeton( 0, 0, couleur)
       
            # Enregistrement de la configuration du jeu.

            sauvegarde(configurations, copie(grille), dimension + 1, True)

glisse(4)