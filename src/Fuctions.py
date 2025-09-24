def Menu_opciones():
        print("---------------------------------------")
        print("Presione la opcion que desee ")
        print("---------------------------------------")
        print("1. Si desea el numero en binario ")
        print("2. Si desea el numero en ocal")
        print("3. Si desea el numero en hexadecimal")
        print("4. Si Desea terminar el programa")
        print("---------------------------------------")
        
#Esta funcion cumple el rol de divir el decimal mediante la base que seria 2        
def decimal_binario():
    decimal=int(input())
    ingreso=decimal
    if decimal<=0:
        return "0"
    binario =""
    while decimal>0:
        residuo=int(decimal % 2)
        decimal=int(decimal/2)
        binario=str(residuo)+binario
    print("//////////////////////////////////////////////////")
    print(f"El numero: {ingreso} en binario es {binario}")
    print("//////////////////////////////////////////////////")  
    
#Esta funcion cumple el rol de divir el decimal mediante la base que seria 8
def decimal_octal(): 
    decimal=int(input())
    ingreso= decimal
    octal=""
    while decimal>0:
        residuo = decimal % 8
        octal= str(residuo) + octal
        decimal=int (decimal/8)
    print("//////////////////////////////////////////////////")
    print(f"El numero: {ingreso} en octal es {octal}")
    print("//////////////////////////////////////////////////")
    
#Esta funcion convierte los equivalentes de los numeros en letras correspondiente a cada una    
def Valor_equivalente(valor):
    valor=str(valor)
    equivalente = {
        "10":"A",
        "11":"B",
        "12":"C",
        "13":"D",
        "14":"E",
        "15":"F"}
    if valor in equivalente:
        return equivalente[valor]
    else:
        return valor
#Esta funcion cumple el rol de divir el decimal mediante la base que seria 16
def decimal_hexadecimal():
    decimal = int(input())
    ingreso = decimal
    hexadecimal = ""
    while decimal >0:
        residuo= decimal % 16
        valor_final = Valor_equivalente(residuo)
        hexadecimal = valor_final+hexadecimal
        decimal = int(decimal/16)
    print("//////////////////////////////////////////////////")
    print(f"El numero: {ingreso} en hexadecimal es "+str(hexadecimal))
    print("//////////////////////////////////////////////////")

 

        
        
        
        
               
