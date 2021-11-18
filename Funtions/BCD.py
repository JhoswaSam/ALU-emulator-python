#IDENTIFICA Y TRANSFORMA LA CANTIDAD DE CIFRAS POR SEPARADO
def count_digits(number, digits):
    i = 0
    while (number != 0):
        temp = number % 10
        digits.append(temp)
        i = i + 1
        number = number // 10
    return i

#CONVERSIÓN DE DECIMAL A BCD
def dec_to_bcd(digits, bcd, n):
    for i in range(n):
        bcd[(4 * i)] = ((digits[i] >> 3) & 1)
        bcd[(4 * i) + 1] = ((digits[i] >> 2) & 1)
        bcd[(4 * i) + 2] = ((digits[i] >> 1) & 1)
        bcd[(4 * i) + 3] = (digits[i] & 1)
    return bcd

#FUNCIÓN SUB MAIN QUE EJECUTE LAS DOS FUNCIONES ANTERIORES Y RETURNA UN VALOR GENERAL
def mainBCD(number):
    list1 = []
    digits = []
    n = count_digits(number, digits)
    digits.reverse()
    bcd = []
    for i in range(4 * n):
        bcd.append(0)
    dec_to_bcd(digits, bcd, n)
    for i in range(4 * n):
        if i % 4 == 3:
            list1.append(bcd[i])
        else:
            list1.append(bcd[i])
    return list1
#RETORNO DE LA TRANSFORMACIÓN FINAL
def final():
    resultadoFinal = mainBCD(number)
    stringbcd = ""
    for i in resultadoFinal:
        stringbcd += str(i)
    return stringbcd

#SIMULACIÓN DE MAIN(CAMBIE VARIABLE A SU GUSTO :3)
#result = int
number = int(input("Ingrese un número en sistema decimal:"))
print(final())

# Creation of the method ToDecimalBCD

def bcdToDecimal(s):
    length = len(s)
    check = 0
    check0 = 0
    num = 0
    sum = 0
    mul = 1
    rev = 0

    for i in range(length - 1, -1, -1):

        sum += (ord(s[i]) - ord('0')) * mul
        mul *= 2
        check += 1

        if (check == 4 or i == 0):
            if (sum == 0 and check0 == 0):
                num = 1
                check0 = 1

            else:

                num = num * 10 + sum

            check = 0
            sum = 0
            mul = 1

    while (num > 0):
        rev = rev * 10 + (num % 10)
        num //= 10

    if (check0 == 1):
        return rev - 1

    return rev

# Driver Code
def MainBcdToDecimal():
    if __name__ == "__main__":
        s = input("Ingrese un número en sistema BCD: ")
        print(bcdToDecimal(s))

def HacerLista():
    resultFinal = MainBcdToDecimal()
    stringbcd = ""
    for i in range(len(resultFinal)-1):
        stringbcd += resultFinal[i]
    return stringbcd


print(HacerLista())
