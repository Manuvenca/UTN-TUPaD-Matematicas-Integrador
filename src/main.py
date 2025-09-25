# Programa para convertir números decimales a otras bases
print("Bienvenido Al conversor de numeros")

while True:
    print("---------------------------------------")
    print("Presione la opcion que desee ")
    print("---------------------------------------")
    print("1. Si desea el numero en binario ")
    print("2. Si desea el numero en octal")
    print("3. Si desea el numero en hexadecimal")
    print("4. Si Desea terminar el programa")
    print("---------------------------------------")
    
    opcion = int(input("Ingrese su opcion: "))
    
    if opcion == 1:
        print("----------------------------------------------------")
        numero = int(input("Ingrese el numero que desea convertir a binario: "))
        if numero <= 0:
            print("El numero en binario es: 0")
        else:
            binario = ""
            numero_original = numero
            while numero > 0:
                residuo = numero % 2
                numero = numero // 2
                binario = str(residuo) + binario
            print("\n")
            print("El numero", numero_original, "en binario es:", binario)
            print("\n")
    
    elif opcion == 2:
        print("----------------------------------------------------")
        numero = int(input("Ingrese el numero que desea convertir a octal: "))
        octal = ""
        numero_original = numero
        while numero > 0:
            residuo = numero % 8
            numero = numero // 8
            octal = str(residuo) + octal
        print("\n")
        print("El numero", numero_original, "en octal es:", octal)
        print("\n")
    
    elif opcion == 3:
        print("----------------------------------------------------")
        numero = int(input("Ingrese el numero que desea convertir a hexadecimal: "))
        hexadecimal = ""
        numero_original = numero
        while numero > 0:
            residuo = numero % 16
            if residuo == 10:
                hexadecimal = "A" + hexadecimal
            elif residuo == 11:
                hexadecimal = "B" + hexadecimal
            elif residuo == 12:
                hexadecimal = "C" + hexadecimal
            elif residuo == 13:
                hexadecimal = "D" + hexadecimal
            elif residuo == 14:
                hexadecimal = "E" + hexadecimal
            elif residuo == 15:
                hexadecimal = "F" + hexadecimal
            else:
                hexadecimal = str(residuo) + hexadecimal
            numero = numero // 16
        print("\n")
        print("El numero", numero_original, "en hexadecimal es:", hexadecimal)
        print("\n")
    
    elif opcion == 4:
        print("---------------------------------------")
        print("Muchas Gracias . Adios!")
        print("---------------------------------------")
        break
    
    else:
        print("Opcion no valida. Intente nuevamente.")
            