hand = open('texto.txt')
for line in hand:
    line = line.rstrip()
    if line.find("mismo") >= 0:
        print(line)