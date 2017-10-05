oliste = []
stjerneliste = []

for times in range(5):
    oliste.append("o")
    stjerneliste.append("*")

rutenett = []

rutenett.append(oliste)
rutenett.append(stjerneliste)
rutenett.append(oliste)


print (rutenett[0])
print (rutenett[1])
print (rutenett[2])

for lists in rutenett:
    print (lists)
