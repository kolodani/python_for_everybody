fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('Vinzia'):
        print(line)