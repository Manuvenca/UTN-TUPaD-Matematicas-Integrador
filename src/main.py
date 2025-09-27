# Conversor de números

HEX_DIGITS = "0123456789ABCDEF"

def is_nonnegative_integer(s):
    s = s.strip()
    return len(s) > 0 and s.isdigit()

def is_binary_string(s):
    s = s.strip()
    if len(s) == 0:
        return False
    i = 0
    while i < len(s):
        c = s[i]
        if c != '0' and c != '1':
            return False
        i += 1
    return True

def str_to_int(s):
    s = s.strip()
    n = 0
    i = 0
    while i < len(s):
        n = n * 10 + (ord(s[i]) - ord('0'))
        i += 1
    return n

def decimal_to_base(n, base):
    if n == 0:
        return "0"
    out = ""
    while n > 0:
        r = n % base
        out = HEX_DIGITS[r] + out
        n //= base
    return out

def binary_to_decimal(bstr):
    total = 0
    i = 0
    while i < len(bstr):
        total = total * 2
        if bstr[i] == '1':
            total = total + 1
        i += 1
    return total

print("Bienvenido al conversor de números")

while True:
    print("---------------------------------------")
    print("Presione la opción que desee")
    print("---------------------------------------")
    print("1. Decimal a Binario")
    print("2. Decimal a Octal")
    print("3. Decimal a Hexadecimal")
    print("4. Binario a Decimal")
    print("5. Terminar el programa")
    print("---------------------------------------")

    opcion = input("Ingrese su opción: ").strip()

    if opcion == "1":
        print("----------------------------------------------------")
        s = input("Ingrese el número decimal no negativo: ").strip()
        if not is_nonnegative_integer(s):
            print("Error: entrada inválida. Debe ser un entero no negativo, sin signos ni espacios.")
            continue
        n = str_to_int(s)
        print("\nEl número", n, "en binario es:", decimal_to_base(n, 2), "\n")

    elif opcion == "2":
        print("----------------------------------------------------")
        s = input("Ingrese el número decimal no negativo: ").strip()
        if not is_nonnegative_integer(s):
            print("Error: entrada inválida. Debe ser un entero no negativo, sin signos ni espacios.")
            continue
        n = str_to_int(s)
        print("\nEl número", n, "en octal es:", decimal_to_base(n, 8), "\n")

    elif opcion == "3":
        print("----------------------------------------------------")
        s = input("Ingrese el número decimal no negativo: ").strip()
        if not is_nonnegative_integer(s):
            print("Error: entrada inválida. Debe ser un entero no negativo, sin signos ni espacios.")
            continue
        n = str_to_int(s)
        print("\nEl número", n, "en hexadecimal es:", decimal_to_base(n, 16), "\n")

    elif opcion == "4":
        print("----------------------------------------------------")
        b = input("Ingrese un número binario (solo 0 y 1): ").strip()
        if not is_binary_string(b):
            print("Error: entrada inválida. Use solo 0 y 1, sin espacios.")
            continue
        print("\nEl binario", b, "en decimal es:", binary_to_decimal(b), "\n")

    elif opcion == "5":
        print("---------------------------------------")
        print("Muchas gracias. ¡Adiós!")
        print("---------------------------------------")
        break

    else:
        print("Opción no válida. Intente nuevamente.")