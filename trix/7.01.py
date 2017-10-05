def equals(liste_en, liste_to):

    if len(liste_en) != len(liste_to):
        return False

    for idx, item in enumerate(liste_en):
        if liste_en[idx] != liste_to[idx]:
            return False

    return True


def sameSet(liste_a, liste_b):
    set_a = set(liste_a)
    set_b = set(liste_b)

    if set_a == set_b:
        return True
    else:
        return False


liste_en = [1, 4, 9, 16, 9, 7, 4, 9, 11, ]
liste_to = [11, 11, 7, 9, 16, 4, 1]

print (equals(liste_en, liste_to))
print (sameSet(liste_en, liste_to))
