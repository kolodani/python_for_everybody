fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Vinzia'):
        continue
    print(line)