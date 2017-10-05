liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

minste = min(liste)
storste = max(liste)

minste_idx = liste.index(minste)
storste_idx = liste.index(storste)

liste[minste_idx] = storste
liste[storste_idx] = minste


print (liste)
