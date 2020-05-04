from pathlib import Path
import sys


#================================================
#
#   FONCTION DE VERIFICATION
#
#================================================

def Verif(DebutX, DebutY, Tableau1, Tableau2):
    Trouv = True

    for a in range(0 , len(Tab1)):
        z = DebutY
        for b in range(0 , len(Tab1[a])):
            #print("On verifie la correspondance entre {}:{} et {}:{}".format(a,b,DebutX,z))
            if Tableau1[a][b] != Tableau2[DebutX][z]:
                Trouv = False
                break
            z += 1
        DebutX += 1

    return Trouv







#=============================================================================================
#
#         MAIN PROGRAM
#
#=============================================================================================

print("Fichiers stockés dans le folder ../Rectangle/")
print("")


#....Test existance fichier 1

Name1 = input("Saisir le nom du fichier 1 sans extension : ").strip().capitalize()
Name1 += ".txt"

Path1 = Path("Rectangle/{}".format(Name1))
if Path1.is_file():
    print("Fichier {} existant.".format(Name1))
else:
    print("Fichier inexistant !")
    sys.exit(0)



#=.....Test existance fichier 2

Name2 = input("Saisir le nom du fichier 2 sans extension : ").strip().capitalize()
Name2 += ".txt"

Path2 = Path("Rectangle/{}".format(Name2))
if Path2.is_file():
    print("Fichier {} existant.".format(Name2))
else:
    print("Fichier inexistant !")
    sys.exit(0)


#.....Ouverture des fichiers

F1 = open(Path1,"r")
F2 = open(Path2,"r")

Tab1 = F1.read().split()
for x in range(0 , len(Tab1)):
    Tab1[x] = list(Tab1[x])

Tab2 = F2.read().split()
for x in range(0 , len(Tab2)):
    Tab2[x] = list(Tab2[x])


#....Le premier caractère a rechercher est en position 0,0 du premier fichier
PCaract = Tab1[0][0]
HauteurTab = len(Tab1)
LongueurTab = len(Tab1[0]) 

#....On balaye le tableau 2 pour chercher ce premier caractère
for x in range(0 , len(Tab2)):
    for z in range(0 , len(Tab2[x])):
        if Tab2[x][z] == PCaract:
            print("Position trouvée ! {}:{}".format(x,z))
            if ((x + LongueurTab) <= len(Tab2)) and ((z + HauteurTab) <= len(Tab2[0])):
                print("Lancement de la recherche.....")
                if Verif(x,z,Tab1,Tab2):
                    print("Trouvé ! Position {},{} validée !".format(z,x))
                    break
                else:
                    print("Mauvaise position : Caractère qui ne correspond pas")
            else:
                print("Mauvaise position : Pas assez de place...")
