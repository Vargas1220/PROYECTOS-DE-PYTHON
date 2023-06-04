#Crear un programa en python que calcule las comisiones que le correspondan a un vendedor de una empresa
#para ello el programa debe preguntar al usuario su nombre y cuanto ha vendido este mes
# ha de calcular las comisiones del 13% y ha de mostrarlo por pantalla

def comisiones(ventas,nombre_empleado):
    comision = (ventas*13)/100
    print(f"OK {nombre_empleado.capitalize()} tus ventas han sido de {ventas} por lo que este mes tus comisiones seran: {round(comision,2)}")


def main():
    nombre_empleado = input("Bienvenido al sistema de calcula de comisiones de Credicoches Canarias:\nPor favor indicame tu nombre.\n=>")
    ventas = float(input(f"Muy bien {nombre_empleado.capitalize()} me puedes indicar cuanto haz vendido este mes?\n=>"))
    comisiones(ventas,nombre_empleado)
    




main()