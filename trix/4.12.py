liste = ["ifa", "aifns", "miaet"]


for idx, item in enumerate(liste):
    print (f"Index = {idx}\nItem = {item}\n")


liste.append(input("Skriv inn noe du vil legge inn i liste.\n> "))
print (liste)
