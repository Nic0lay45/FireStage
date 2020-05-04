from pathlib import Path
import sys

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



