liste = [1, 2, 3, 4, 5]

# enumerate itererer over baade indeks og verdi i listen samtidig
for idx, item in enumerate(liste):
    liste[idx] = item ** 2

print (liste)
