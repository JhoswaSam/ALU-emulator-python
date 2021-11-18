#Funcion de cambiar un Decimal a un Hexadecimal
#return --> answer == string con el numero

def DecimalAHexa(number):
    #Diccionario de Variables
    Hexa_CODES = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    restos = []
    valores = []
    o = 0
    answer = ""
    #Cambio de numeros por el Diccionario
    while (number > 0):
        float(number)
        resto = number % 16
        restos.append(resto)
        number = int((number - resto) / 16)

    for x in restos:
        if x in Hexa_CODES.keys():
            o = Hexa_CODES.get(x)
        else:
            o = x
        valores.append(o)
        valores.reverse()

    for i in valores:
        answer += str(i)

    return answer

#Funcion de cambiar un Hexadecimal a un Decimal.
# return --> answer == string que tiene el número.
def HexaADecimal(number):
    number = number.upper()
    answer = 0
    Hexa_CODES = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    indice = len(str(number))
    for i in number:
        indice = int(indice) - 1
        if i in Hexa_CODES.keys():
            k = Hexa_CODES.get(i)
        else:
            k = i
        answer += int(k) * (16 ** (indice))
    return answer


#Suma de HExagesimales. Recibe como parametros 2 numeros hexadecimales "nro1" y "nro2"
#Return --> suma == string con la respuesta
def suma_hexa(nro1, nro2):
    plus_total = []
    id = -1
    Hexa_CODES = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    nro1_list = []
    nro2_list = []
    for i in nro1.upper():
        if i in Hexa_CODES.keys():
            i = Hexa_CODES.get(i)
        nro1_list.append(int(i))

    for j in nro2.upper():
        if j in Hexa_CODES.keys():
            j = Hexa_CODES.get(j)
        nro2_list.append(int(j))

    # Igualar las cifras en ambos numero (listas)
    idx_1 = len(nro1_list)
    idx_2 = len(nro2_list)
    if idx_1 != idx_2:
        if idx_1 > idx_2:
            idx_general = idx_1
            count = idx_2
            while count < idx_1:
                nro2_list.insert(0, 0)
                count += 1
        else:
            idx_general = idx_2
            count = idx_1
            while count < idx_2:
                nro1_list.insert(0, 0)
                count += 1
    else:
        idx_general = idx_1
    # empezando procedimiento de suma
    ctn = 0
    while (id * -1) != idx_general + 1:
        if ctn == 0:
            plus = nro1_list[id] + nro2_list[id] + ctn
        else:
            plus = nro1_list[id] + nro2_list[id] + ctn
            ctn = 0
        if plus >= 16:
            while plus >= 16:
                plus -= 16
                ctn += 1

        plus_total.insert(id, plus)
        id -= 1

    #Traducir la suma decimal en hexadecimales    
    Hexa2_CODES = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    suma = ""
    for h in plus_total:
        if h in Hexa2_CODES.keys():
            h = Hexa2_CODES.get(h)
        suma += str(h)

    return suma

#Funcion de Resta
#return --> resta == string
def resta_hexa(nro1, nro2):
    resta_total = []
    id = -1
    Hexa_CODES = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    nro1_list = []
    nro2_list = []
    for i in nro1.upper():
        if i in Hexa_CODES.keys():
            i = Hexa_CODES.get(i)
        nro1_list.append(int(i))

    for j in nro2.upper():
        if j in Hexa_CODES.keys():
            j = Hexa_CODES.get(j)
        nro2_list.append(int(j))

    # Igualar las cifras en ambos numero (listas)
    idx_1 = len(nro1_list)
    idx_2 = len(nro2_list)
    if idx_1 != idx_2:
        if idx_1 > idx_2:
            idx_general = idx_1
            count = idx_2
            while count < idx_1:
                nro2_list.insert(0, 0)
                count += 1
        else:
            idx_general = idx_2
            count = idx_1
            while count < idx_2:
                nro1_list.insert(0, 0)
                count += 1
    else:
        idx_general = idx_1

    # restaaa
    while (id * -1) != idx_general + 1:
        if nro2_list[id] > nro1_list[id]:
            nro1_list[id] += 16
            nro1_list[id - 1] -= 1
        resta = nro1_list[id] - nro2_list[id]
        resta_total.insert(id, resta)
        id -= 1

    # Traducir decimales en Hexagecimales.
    Hexa2_CODES = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    resta = ""
    for h in resta_total:
        if h in Hexa2_CODES.keys():
            h = Hexa2_CODES.get(h)
        resta += str(h)
    # !!!---- Si el sustraendo es mayor al minuendo el algoritmo falla pero se puede hacer un control de errores

    return resta

#Funcion de convertir los numeros en decimales, multiplcarlos y convertirlos de vuelta.
#return --> xcion_hexa == string
def xcion_hexa(nro1, nro2):
    nro1_deci = HexaADecimal(nro1)
    nro2_deci = HexaADecimal(nro2)
    float(nro1_deci)
    float(nro2_deci)
    xcion = nro1_deci* nro2_deci
    xcion_hexa = DecimalAHexa(xcion)
    str(xcion_hexa)
    return xcion_hexa

#Funcion de convertir los numeros a Hexa y dividirlos si tienen 0 como seguro numero no se realizara
#Return --> division_hexadecimal == str
def division_hexa(nro1, nro2):
    nro1_deci = HexaADecimal(nro1)
    nro2_deci = HexaADecimal(nro2)
    float(nro1_deci)
    float(nro2_deci)
    if nro2_deci != 0:
        division = nro1_deci/nro2_deci
        division_hexadecimal = DecimalAHexa(division)
    else:
        division = '!Error calculo no posible'
        division_hexadecimal = division
    str(division_hexadecimal)
    return division_hexadecimal
