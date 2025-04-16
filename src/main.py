def calculate(text: str) -> float:
    numeros = text.split(" ")

    i = 0
    while i < len(numeros):
        if numeros[i] == '**':
            resultado = exponenciar(numeros[i - 1], numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0
        else:
            i += 1
    i = 0
    while i < len(numeros):
        if numeros[i] == '*':
            resultado = multiplicacion(numeros[i - 1], numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0
        else:
            i += 1

    i = 0
    while i < len(numeros):
        if numeros[i] == '/':
            resultado = division(numeros[i - 1], numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0
        else:
            i += 1
    i = 0
    while i < len(numeros):
        if numeros[i] == '+':
            resultado = suma(numeros[i - 1], numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0
        else:
            i += 1
    i = 0
    while i < len(numeros):
        if numeros[i] == '-':
            resultado = resta(numeros[i - 1], numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0
        else:
            i += 1
    return resultado


def multiplicacion(a, b):
    try:
        return float(a) * float(b)
    except ValueError:
        return ValueError


def suma(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return ValueError


def division(a, b):
    try:
        if b == 0: raise ZeroDivisionError
        return float(a) / float(b)
    except ValueError:
        return ValueError


def resta(a, b):
    try:
        return float(a) - float(b)
    except ValueError:
        return ValueError


def exponenciar(a, b):
    try:
        if a == 0 and b == 0: raise ArithmeticError
        return float(a) ** float(b)
    except ValueError:
        return ValueError