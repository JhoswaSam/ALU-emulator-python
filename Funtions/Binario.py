# Creation of the methods ToBinary, ToDecimalBinary, SumOfBinary, BinarySubtraction, BinaryMultiplication and BinaryDivision

# Creation of the method ToBinary
def ToBinary(number):

    binary = [] 
    result = ""

    while (number > 0):

        division = int(float(number % 2))

        binary.append(division)

        number = (number - division) / 2

    for i in binary[:: -1]:

        result += str(i)

    return result


# Creation of the method ToDecimalBinary
def ToDecimalBinary(binary):

    decimal = 0
    posicion = 0
    # Invertir binary, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    binary = binary[::-1]
    for digito in binary:

        valor_entero = int(digito)

        numero_elevado = int(2 ** posicion)

        equivalencia = int(numero_elevado * valor_entero)

        decimal += equivalencia

        posicion += 1

    return decimal


# Creation of method SumOfBinary
def SumOfBinary(number1, number2):
    
    maxTamaño = max(len(number1), len(number2))

    number1 = number1.zfill(maxTamaño)
    number2 = number2.zfill(maxTamaño)

    result = ""

    carry = 0

    for i in range(maxTamaño - 1, -1, -1):

        r = carry

        r += 1 if number1[i] == "1" else 0

        r += 1 if number2[i] == "1" else 0

        result = ("1" if r % 2 == 1 else "0") + result

        carry = 0 if r < 2 else 1

    if carry != 0:

        result = "1" + result
    
    return result.zfill(maxTamaño)


# Creation of method BinarySubtraction

def normaliseString(str1,str2):
    diff = abs((len(str1) - len(str2)))
    if diff != 0:
        if len(str1) < len(str2):
            str1 = ('0' * diff) + str1
            
        else:
            str2 = ('0' * diff) + str2
           
    return [str1,str2]


def BinarySubtraction(number1, number2):

    if len(number1) == 0:
        return
    
    if len(number2) == 0:
        return
    
    number1, number2 = normaliseString(number1, number2)

    starIdx = 0

    endIdx = len(number1) - 1

    carry = [0] * len(number1)

    result = ""

    while endIdx >= starIdx:

        x = int(number1[endIdx])
        y = int(number2[endIdx])

        sub = (carry[endIdx] + x) - y

        if sub == 1: 

            result += "1"

        elif sub == 0:
            
            result += "0"

        else:
            raise Exception("Error")

        endIdx -= 1

    return result[:: -1]


# Creation of method BinaryMultiplication and BinaryDivision

def BinaryMultiplication(number1, number2):
    pass