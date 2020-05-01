NbMarches = int(input("Nombre de marches : "))

z = 0
while z <= NbMarches :
    print((NbMarches - z) * " " + "#" * z)
    z += 1