def calculate(text:str) -> float:
    def exponenciacion(a,b):
        return float(a)**float(b)
    
    numeros = text.split()
    for i in range(len(numeros)):
        if numeros[i] == "**":
            return exponenciacion(numeros[i-1],numeros[i+1])
    
    
