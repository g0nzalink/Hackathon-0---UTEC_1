def Calculate(text):
    numeros = text.split(" ")
    i = 0

    while i < len(numeros):
        if numeros[i] == '**':
            resultado = exponenciar(numeros[i - 1],numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0  
        else:
            i += 1
    
    while i < len(numeros):
        if numeros[i] == '*':
            resultado = multiplicacion(numeros[i - 1],numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0  
        else:
            i += 1
            
    i = 0
    while i < len(numeros):
        if numeros[i] == '/':
            resultado = division(numeros[i - 1],numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0  
        else:
            i += 1
    i = 0
    while i < len(numeros):
        if numeros[i] == '+':
            resultado = suma(numeros[i - 1],numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0  
        else:
            i += 1
    i = 0
    while i < len(numeros):
        if numeros[i] == '-':
            resultado = resta(numeros[i - 1],numeros[i + 1])
            numeros = numeros[:i - 1] + [resultado] + numeros[i + 2:]
            i = 0  
        else:
            i += 1
    return resultado

def exponenciar(a, b):
    return float(a)**float(b)
     
def multiplicacion(a, b):
    return float(a)*float(b)

def suma(a, b):
    return float(a)+float(b)
  
def division(a, b):
    return float(a) / float(b)
  
def resta(a,b):
    return float(a)-float(b)

