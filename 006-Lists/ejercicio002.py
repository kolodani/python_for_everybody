han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    if line == "" :
        continue
    wds = line.split()
    if wds[0] != "From":
        continue
    print(wds[2])
