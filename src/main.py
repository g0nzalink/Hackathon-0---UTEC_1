
def calculate(text:str) -> float:
    numeros = text.split()
    if len(numeros)%2==1: raise SyntaxError
    for i in range(len(numeros)):
        if numeros[i] == "+":
            return suma(numeros[i-1], numeros[i+1])
        if numeros[i] == "**":
            return exponenciacion(numeros[i-1], numeros[i+1])
        if numeros[i] == "-":
            return resta(numeros[i-1], numeros[i+1])
        if numeros[i] == "/":
            return division(numeros[i-1], numeros[i+1])


def multiplicacion(a, b):
    if a.isdigit()==False or b.isdigit()==False: return ValueError
    return float(a) * float(b)

def suma(a, b):
    if a.isdigit() == False or b.isdigit() == False: return ValueError
    return float(a) + float(b)
  
def division(a, b):
    if a.isdigit() == False or b.isdigit() == False: return ValueError
    if b==0: raise ZeroDivisionError
    return float(a) / float(b)

def resta(a,b):
    if a.isdigit() == False or b.isdigit() == False: return ValueError
    return float(a)-float(b)

def exponenciacion(a,b):
    if a.isdigit() == False or b.isdigit() == False: return ValueError
    if a==0 and b==0: raise ArithmeticError
    return float(a)**float(b)
