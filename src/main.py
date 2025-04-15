
def calculate(text:str) -> float:
    def exponenciacion(a,b):
        return float(a)**float(b)
    
    numeros = text.split()
    for i in range(len(numeros)):
        if numeros[i] == "**":
            return exponenciacion(numeros[i-1],numeros[i+1])
    
def calculate() -> float:
    pass

def multiplicacion(a, b ):
    return a*b

  
def division(a, b):
    return float(a) / float(b)
  
def resta(a,b):
    return a-b

