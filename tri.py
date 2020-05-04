
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


#======================================================
# 
#      TRI EN UTILISANT LES FONCTIONS PYTHON
#
#======================================================

def Fct(mylist):
    print(" => Fonctions Python !!")
    print("")
    print("Avant : {}".format(mylist))
    mylist.sort(reverse=True)
    print("Après : {}".format(mylist))
    return



#======================================================
# 
#      TRI EN UTILISANT LA METHODE DE SELECTION
#
#======================================================

def Select(mylist):
    print(" => Methode Selection !!")
    print("")
    print("Avant : {}".format(mylist))

    for i in range(0 , len(mylist)):
        max = i
        for j in range(i + 1 , len(mylist)):
            if mylist[j] > mylist[max]:
                max = j
        if max != i:
            temp = mylist[i]
            mylist[i] = mylist[max]
            mylist[max] = temp

    print("Après : {}".format(mylist))
    return




#======================================================
# 
#      TRI EN UTILISANT LA METHODE BULLE
#
#======================================================
def Bulle(mylist):
    print(" => Methode Bulle !!")
    print("")
    print("Avant : {}".format(mylist))

    for i in range(len(mylist) - 1, -1 , -1):
        for j in range(0 , i):
            if mylist[j+1] > mylist[j]:
                temp = mylist[j+1]
                mylist[j+1] = mylist[j]
                mylist[j] = temp

    print("Après : {}".format(mylist))
    return
        

debut()
