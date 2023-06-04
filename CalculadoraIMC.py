# Programa dedicado a la realizacion de una calculadora en python
#(IMC = peso (kg)/ [estatura (m)]2
import platform
import os
import time

def CalculateIMC(UserHeight,UserWeight):
    
    UserHeight = (UserHeight/100)
    ImcResult = UserWeight / pow(UserHeight,2)
    return ImcResult




def main():
    print("-------------------\nCALCULADORA DE IMC\n-------------------")
    OfferedOptions = input("1. Realizar prueba\n2. Entender Resultados\n3. Salir\n\n=>  ")
    if OfferedOptions == '1':
        time.sleep(1)
        os.system('clear')
        UserName = input("Muy Bien para continuar necesito que me indiques tu nombre: ")
        UserName = UserName.capitalize()
        UserHeight = int(input(f"Mcuho gusto {UserName} para poder calcular tu indice de masa corporal necesatare de algunos datos.\n Indica tu altura en cm: "))
        UserWeight = float(input("Perfecto! ahora introduce tu peso en kilogramos: "))
        time.sleep(1)
        os.system('clear')
        print(f"Vale {UserName} ya hemos analizados tus resultados y de acuerdo a los datos que nos has proporcionado tu IMC actual es de {CalculateIMC(UserHeight,UserWeight)}")

        



    
main()