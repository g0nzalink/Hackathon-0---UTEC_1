def validate_expression(text: str) -> None:
    if not text.strip():
        raise ValueError("Empty expression or only whitespace")

    allowed_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '+', '-', '*', '/', ' ', '.', '(', ')', '**'}
    for char in text:
        if char not in allowed_chars and not char.isspace():
            raise ValueError(f"Invalid character in expression: '{char}'")

    last_char = text.strip()[-1]
    if last_char in {'+', '-', '*', '/'}:
        raise SyntaxError("Incomplete expression (ends with operator)")

def calculate(text):
    validate_expression(text)

    i = 0
    while "(" in text:
        paren1 = 0
        paren2 = 0
        for j in range(len(text)):
            if text[j] == "(":
                paren1 = j
            if text[j] == ")":
                paren2 = j
                break
        parentesis = text[paren1 + 1:paren2].split()
        dejarlo = text[paren2 + 1:]
        i = 0
        while i < len(parentesis):
            if parentesis[i] == '**':
                resultado = exponenciar(parentesis[i - 1], parentesis[i + 1])
                parentesis = parentesis[:i - 1] + [resultado] + parentesis[i + 2:]
                i = 0
            else:
                i += 1
        i = 0

        while i < len(parentesis):
            if parentesis[i] == '*':
                resultado = multiplicacion(parentesis[i - 1], parentesis[i + 1])
                parentesis = parentesis[:i - 1] + [resultado] + parentesis[i + 2:]
                i = 0
            else:
                i += 1

        i = 0
        while i < len(parentesis):
            if parentesis[i] == '/':
                resultado = division(parentesis[i - 1], parentesis[i + 1])
                parentesis = parentesis[:i - 1] + [resultado] + parentesis[i + 2:]
                i = 0
            else:
                i += 1
        i = 0
        while i < len(parentesis):
            if parentesis[i] == '+':
                resultado = suma(parentesis[i - 1], parentesis[i + 1])
                parentesis = parentesis[:i - 1] + [resultado] + parentesis[i + 2:]
                i = 0
            else:
                i += 1
        i = 0
        while i < len(parentesis):
            if parentesis[i] == '-':
                resultado = resta(parentesis[i - 1], parentesis[i + 1])
                parentesis = parentesis[:i - 1] + [resultado] + parentesis[i + 2:]
                i = 0
            else:
                i += 1
        text = text[:paren1] + str(parentesis[0]) + text[paren2 + 1:]

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
            resultado = round(multiplicacion(numeros[i - 1], numeros[i + 1]), 1)
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