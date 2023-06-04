texto = input("Introduce un texo a inspeccionar: ")
letras = []
texto = texto.lower()

# Utilizamos append para introducir el inpu del usuario a nuestra lista vacia

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

# Contando palabras con el metodo count e introduciendolas en variables separadas

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

# Imprimimos por pantalla la cantidad de letras encontradas

print(f"\nCANTIDAD DE LETRAS\n\nHemos encontrado la letra \"{letras[0].upper()}\" repetida {cantidad_letras1} veces.\nHemos encontrado la letra \"{letras[1].upper()}\" repetida {cantidad_letras2} veces.\nHemos encontrado la letra \"{letras[2].upper()}\" repetida {cantidad_letras3} veces.\n")


print(f"CANTIDAD DE PALABRAS EN EL TEXTO:\n\nSe han encontrado un total de {len(texto.split())} palabras dentro del texto.\n")
# Mostramos por pantalla la palabra inicial y final medianto el metodo de indexacion 
print(f"\nLETRA INICIAL Y FINAL\nLa letra inicial es \"{texto[0]}\" y la letra final es \"{letras[-1]}\".")

#Mostramos por pantalla el texto invertido
palabras = texto.split()
palabras.reverse()
print(f"\nTEXTO INVERTIDO\n\n{' '.join(palabras)}")

