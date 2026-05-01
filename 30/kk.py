def calcular_fatorial(numero):
    if numero < 0:
        return "Não existe fatorial de número negativo."
    
    else:
        resultado = 1
        for i in range(1, numero + 1 ) :
            resultado *= i
        return resultado

# Exemplo de uso:
numero = 5
print(f"o fatorial de {numero} é: {calcular_fatorial (numero)}")