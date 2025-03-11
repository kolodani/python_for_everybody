han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    print("Line: ",line)
    wds = line.split()
    print("Words: ", wds)
    # sentencia guardian que evita que la siguiente de error
    # si la lista queda vacia, da error
    if len(wds) < 1 :
        continue
    if wds[0] != "From":
        continue
    print(wds[2])
