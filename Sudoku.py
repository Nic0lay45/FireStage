from pathlib import Path
import sys
import os

os.system("cls")

#==========================================================
#
# FONCTION EXPLOSE : Eclate la grille en Tableau MultiDim
#
#==========================================================

def Explose(g):

    g = g.replace("|","")
    g = g.replace("-","")
    g = g.replace("+","")
    g = g.split("\n")
    g.remove(g[3])
    g.remove(g[6])

    for x in range(0 , len(g)):
        g[x] = list(g[x])

    return g



#==========================================================
#
# FONCTION RESTRUCT : RECONSTRUIT LA GRILLE AU PROPRE
#
#==========================================================

def Restruct(g):

    GrilleVide = ""
    for x in range(0,9):
        l = ""
        for z in range(0,9):
            if z == 3 or z == 6:
                l += "|"
            l += "{}".format(g[x][z])
        if x == 3 or x == 6:
            GrilleVide += "---+---+---\n"
        GrilleVide += "{}\n".format(l)

    return GrilleVide


#==========================================================
#
# TRAITEMENT LIGNE
#
#==========================================================

def TraitLigne(l):

    if "".join(l).count("_") == 1:
        print("Une seule inconnue, calcul...")
        for x in range(1,10):
            try:
                "".join(l).index(str(x))
                print("{} trouvé en position {}".format(x,"".join(l).index(str(x))))
            except:
                print("Valeur non trouvée : {}".format(x))
                l["".join(l).index("_")] = str(x)
                break
    else:
        print("Plusieurs inconnues, next...")

    return l



#============================================================
#
#            MAIN PROGRAM
#
#============================================================

print("Fichier stocké dans le folder ../Sudoku/")

#....Test existance fichier 

print("On s'assure que le fichier existe bien.")
Name1 = "s.txt"

Path1 = Path("Sudoku/{}".format(Name1))
if Path1.is_file():
    print("Fichier {} existant.".format(Name1))
else:
    print("Fichier inexistant !")
    sys.exit(0)

#.....Ouverture des fichiers
F1 = open(Path1,"r")

print("")
print("Voici la grille de Sudoku que le système va résoudre : ")

GrilleOrigine = F1.read()

print(GrilleOrigine)

GrilleOrigine = Explose(GrilleOrigine)

print("On commence par traiter ligne par ligne...")

for x in range(0 , len(GrilleOrigine)):
    print("Traitement de la ligne : {}".format(GrilleOrigine[x]))
    GrilleOrigine[x] = TraitLigne(GrilleOrigine[x])

print("Traitement des lignes terminé")

GrilleOrigine = Restruct(GrilleOrigine)

print(GrilleOrigine)
