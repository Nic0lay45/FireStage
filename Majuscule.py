phrase = input("Saisir votre phrase à convertir : ")

z = 0
newphrase = []
for l in phrase:
    if z % 2 != 0:
        newphrase.append(phrase[z].capitalize())
    else:
        newphrase.append(phrase[z].lower())
    z += 1
print("".join(newphrase))

