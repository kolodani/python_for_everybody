import re

hand = open("texto.txt")
for line in hand:
    line = line.rstrip()
    if re.search("mismo", line):
        print(line)
