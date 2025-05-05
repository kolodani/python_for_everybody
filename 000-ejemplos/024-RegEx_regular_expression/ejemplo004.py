hand = open("texto.txt")
for line in hand:
    line = line.rstrip()
    if line.startswith("el"):
        print(line)
