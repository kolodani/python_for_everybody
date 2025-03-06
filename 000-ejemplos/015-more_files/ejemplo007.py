fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not 'Vinzia' in line:
        continue
    print(line)