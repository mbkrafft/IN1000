f = open('navn.txt', 'r')

personer = []
hunder = []

for line in f:
    if line[0:1] == "P":
        personer.append(line[2:-1])
    elif line[0:1] == "H":
        hunder.append(line[2:-1])

print (f"Personer: {personer}")
print (f"Hunder: {hunder}")

f.close()
