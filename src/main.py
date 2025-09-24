from Fuctions import Menu_opciones
from Fuctions import decimal_binario
from Fuctions import decimal_octal
from Fuctions import decimal_hexadecimal

print("Bienvenido Al convensor de numeros: ")
while True:
    Menu_opciones()
    opciones=int(input())
    match opciones:
        case 1:
            print("----------------------------------------------------")
            print("Ingrese el numero que desea convertir a binario : ")
            decimal_binario()
        case 2:
            print("----------------------------------------------------")
            print("Ingrese el numero que desea convertir a octal :")
            decimal_octal()
        case 3:
            print("----------------------------------------------------")
            print("Ingrese el numero que desea convertir a hexadecimal:")
            decimal_hexadecimal()
        case 4:
            print("---------------------------------------")
            print("Muchas Gracias . Adios!")
            print("---------------------------------------")
            break
            