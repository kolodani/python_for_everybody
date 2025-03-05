str = "X-DSPAM-Confidence: 0.8475"
# primero busco la posicion de los dos puntos
ipos = str.find(":")
print(ipos)
# le sumo dos para no tomar el espacio
piece = str[ipos + 2 :]
print(piece)
# lo convierto a flotante
value = float(piece)
print(value)
print(value + 42.0)
