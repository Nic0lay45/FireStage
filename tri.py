ListeATrier = []

rep = True
while rep:
    rep = input("Saisir un nombre (X pour terminer) : ")
    if rep == "X" or rep == "x":
        rep = False
    else:
        ListeATrier.append(int(rep))
        rep = True






def debut():
    print("=============================================")
    print("| Méthodes de tri possibles :               |")
    print("|    1. Tri via les fonctions de Python     |")
    print("|    2. Tri par méthode Selection           |")
    print("|    3. Tri par méthode Bulle               |")
    print("=============================================")
    print("")
    choix = input("Votre choix (1/2/3/X pour sortir) : ")
    if choix == "X" or choix == "x":
        print("A bientôt")
        return
    if choix == "1":
        Fct(ListeATrier)
    if choix == "2":
        Select(ListeATrier)
    if choix == "3":
        Bulle(ListeATrier)
    return

def Fct(mylist):
    print(" => Fonctions Python !!")
    print("")
    print("Avant : {}".format(mylist))
    mylist.sort(reverse=True)
    print("Après : {}".format(mylist))
    return

def Select(mylist):
    print("Methode Selection !!")
    return

def Bulle(mylist):
    print("Methode Bulle !!")
    return
        

debut()
