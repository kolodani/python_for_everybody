# ingreso el nombre del archivo
name = input("Enter file: ")
# abro el archivo
handle = open(name)

# creo un diccionario vacio
counts = dict()
# extraigo cada linea del texto
for line in handle:
    # creo una lista, con cada palabra de la linea
    words = line.split()
    # recorro la lista
    for word in words :
        # si la palabra no esta la agrego al diccionario con valor de 1
        # si la palabra esta, le agrego 1
        counts[word] = counts.get(word,0) + 1

# Creo dos variables a comparar, las creo vacias
bigcount = None
bigword = None
# tomo mi diccionario y cuento item por item
for word,count in counts.items() :
    # comparo si bigcount tiene un valor o si es menor a lo que estoy comparando
    # si lo es cambio los valores de bigword y bigcount
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

# imprimo por pantalla la palabra que salio y la cantidad de veces
print(bigword, bigcount)