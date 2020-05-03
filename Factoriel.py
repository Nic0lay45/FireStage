fact = int(input("Saisir un nombre : "))

result = 1

while fact != 1:
    print("Resultat Intermédiaire : {} * {}".format(result,fact))
    result = result * fact
    fact -= 1

print("Resultat Final : {}".format(result))