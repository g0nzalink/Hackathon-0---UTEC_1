def calculate(text:str) -> float:
    def suma(a,b):
        return float(a)**float(b)
    
    numeros = text.split()
    for i in range(len(numeros)):
        if numeros[i] == "+":
            return suma(numeros[i-1],numeros[i+1])