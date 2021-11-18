# Creation of the methods ToOctal, ToDecimalOctal, OctalAddition, OctalSubtraction, OctalMultiplication and OctalDivision

# Creation of the method ToOctal
def ToOctal(number): 
    octal = []
    while number >=1:
        octal.append(str(number % 8))
        number //= 8
    return ("".join(octal[::-1]))

# Creation of the method ToDecimalOctal
def ToDecimalOctal(octal):
    decimal = 0
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    octal = octal[::-1]
    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal

# Creation of the method OctalAddition
def OctalAddition(num1,num2)
    #Declaracion del 1er numero
    num1 = input("Input number 1: ")
    num1 = ("".join(num1[::-1]))

    #Mover el 1er numero a una lista
    num1 = str(num1)
    list_num1 = []

    #Separar el 1er numero cifra por cifra
    for n1 in num1:
        n1 = int(n1)
        list_num1.append(n1)

    #Declaracion del 2do numero
    num2 = input("Input number 2: ")
    num2 = ("".join(num2[::-1]))

    #Mover el 2do numero a una lista
    num2 = str(num2)
    list_num2 = []

    #Separar el 2do numero cifra por cifra
    for n2 in num2:
        n2 = int(n2)
        list_num2.append(n2)

    #Declaracion de la lista para operar
    newList = []
    newListComp = []
    convNewList = []
    compList = [7]

    #Adicion y comparacion de terminos para sistema octal
    j = 0
    k = len(list_num1)+1
    for i in range(len(list_num1)):
        newList.append(list_num1[i] + list_num2[i]+j) #Suma de num1 y num2 junto al sobrante de la cifra inferior
        j = j - j #Reinicio del sobrante de la cifra inferior
        if int(newList[i]) >= 8: #Condicional para comparar la cifra con el sistema octal
            h = i #Declaracion de nueva iteracion
            while newList[i] >= 8: #Inicio de repetitiva para transformar en octal
                newList[i]-8
                if newList[i]<=7
                    break
                j += 1

    #Resultado de OctalAddition
    converter = ("".join([str(_) for _ in newList]))
    converter = ("".join(converter[::-1]))

    converter = str(converter)
    listConverter = []

    for c1 in converter:
        c1 = int(c1)
        listConverter.append(c1)
    return(converter)

'''
def min_max(numeros):
    menor = numeros[0]
    mayor = numeros[0]

    for n in numeros:
        if n < menor:
            menor = n

        if n > mayor:
            mayor = n

    return menor, mayor

datos = [9, 3, 2, 13, 0, 23, 8, 7]

print(min_max(datos))

'''
def ToNegativeDecimalOctal(octal):
    #Calculando octal
