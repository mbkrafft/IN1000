f = open("navn.txt", 'r')

liste = []

for lines in f:
    liste.append(lines)

print (liste)

f.close()
