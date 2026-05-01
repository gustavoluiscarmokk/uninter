# EQUAÇÃO DE BASKARA
print("resolvendo equação de baskara: ")
print("ax**+bx+c=0")
a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))

delta = b**2 - 4 * a * c

x1 = (-b + delta**0.5) / (2 * a)
x2 = (-b - delta**0.5) / (2 * a)
print(f"As raízes da equação são {a} x** + {b} x + {c} = 0 ")
print(f"delta = {delta}")
print(f"são = {x1} e {x2}")