#PROYECTO 4, CREACION DE UN MINI JUEGO DE ADIVINAR EL NUMERO
from random import *



# SE DEFINE LA FUNCION juego QUE SE ENCARGA DE REALIZAR EL FUNCIONAMIENTO COMPLETO DEL JUEGO
def juego():
    # ESTABLECEMOS NUESTRAS VARIBALES

    # LA VARIABLE INIT NOS SERVIRA PARA PODER SEGUIR EN EL BUCLE WHILE O SALIR DEL MISMO
    init = 0
    # LA VARIABLE numero_a_adivinar ESTA COMPUESTA POR EL METODO RANDINT IMPORTADO DEL PAQUETE RANDOM QUE NOS SERVIRA PARA GENERAR UN NUMERO ALEATORIO ENTRE 1 Y 100
    numero_a_adivinar = randint(1,100)
    #INICIALIZAMOS LA VARIABLE INTENTOS EN 8 PARA PODER LLEVAR UN CONTROL DE LOS INTENTOS UTILIZADOS POR EL USUARIO
    intentos = 8
    nombre_usuario = input("Por favor introduce tu nombre: ")

    ##print(f"\n\n{numero_a_adivinar}\n\n")  ## SE PUEDE QUITAR LOS COMENTARIOS DE ESTA LINEA PARA VER EL NUMERO QUE GENERA EL PROGRAMA Y COMPROBAR EL FUNCIONAMIENTO DEL MISMO
    
    print(f"Bueno, {nombre_usuario.capitalize()}, he pensado un numero entre 1 y 100\nEl reto consiste en adivinar el numero que he pensado y para ello tienes solo ocho intentos. ")
    opcion = int(input(("\n\nComencemos!\n\nDime un numero del 1 al 100: ")))
    
    # BUCLE WHILE QUE SE ENCARGA DE GESTIONAR SI LA OPCION INTRODUCIDA POR EL USUARIO CORRESPONDE CON EL NUMERO GENERADO POR EL PROGRAMA
    # O SI ESTA SE ENCUENTRA FUERA DE LOS RANGOS ESTABLECIDOS. ADICIONALMENTE SE LE MUESTRA POR PANTALLA UN MENSAJE AL USUARIO
    # INDICANDO SI EL NUMERO QUE ELIGIO ES MENOR, MAYOR O ES IGUAL AL NUMERO GENERADO POR LA MAQUINA

    while init == 0 and intentos > 0:
        if opcion < 1 or opcion >100:
            print("Lo siento, has elegido un numero que no esta dentro del rango (1:100)")
            opcion = int(input("\n\nIntena de nuevo: "))
            
        elif opcion < numero_a_adivinar:
            print("Lo siento el numero que haz elegido no es correcto. haz elegido un numero menor al que he pensado.")
            opcion = int(input("\n\nIntena de nuevo: "))
            
        elif opcion > numero_a_adivinar:
            print("Lo siento el numero que haz elegido no es correcto. haz elegido un numero mayor al que he pensado.")
            opcion = int(input("\n\nIntena de nuevo: "))

        # SE RESTA 1 INTENTOS CADA VEZ QUE ALGUNA DE LAS PRIMERAS TRES OPCIONES COINCIDEN CON EL NUMERO INTRODUCIDO POR EL USUARIO    
        intentos -= 1
        print(f"\nTe quedan {intentos} intentos\n")  
        if intentos == 0:
            print("\nLo siento, te haz quedado sin intentos. He ganado yo!")  
            break

        ## SI EL NUMERO INTRODUCIDO POR EL USUARIO ES IGUAL AL NUMERO GENERADO POR LA MAQUINA SE IMPRIME POR PANTALLA UN MENSAJE DE QUE EL JUGADOR HA GANADO
        ## SE CAMBIA LA VARIABLE INIT A 1 PARA SALIR DEL BUCLE WHILE Y FINALIZAR EL PROGRAMA

        if opcion == numero_a_adivinar:
            print(f"Felicidades! el numero {opcion} que me haz dicho es el correcto! haz ganado")
            init = 1

        
## FUNCION MAIN BASICA DONDE SE LLAMA A LA FUNCION juego QUE INICIALIZA EL PROGRAMA
def main():
    juego()

main()