from pathlib import Path
import sys

#=============================================================================================
#
#         MAIN PROGRAM
#
#=============================================================================================

print("Fichier stocké dans le folder ../Anagrammes/")
print("")


#....Test existance fichier 

print("On s'assure que le fichier existe bien.")
Name1 = "fr.txt"

Path1 = Path("Anagrammes/{}".format(Name1))
if Path1.is_file():
    print("Fichier {} existant.".format(Name1))
else:
    print("Fichier inexistant !")
    sys.exit(0)

#.....Ouverture des fichiers
F1 = open(Path1,"r")

Tab1 = F1.read().split()

Mot = input("Mot à rechercher : ").strip()

print("Lancement de la machine...")
print("Mot à rechercher : {}".format(Mot))
print("Possibilités : {}".format(Tab1))

ListeAna = []

for word in Tab1:
    wordTab = list(word)
    Trouv = True
    for x in Mot:
        if x in wordTab:
            wordTab[wordTab.index(x)] = ""
        else:
            Trouv = False
            break
    if Trouv:
        ListeAna.append(word)

print("Voici la liste des anagrammes dans le fichier : {}".format(ListeAna))
