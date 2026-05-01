
def bhaskara(a,b,c):
    delta = b**2 - 4 * a * c
    x1 = (-b + delta**0.5) / (2 * a) 
    x2 = (-b - delta**0.5) / (2 * a)
    return x1, x2



V1 = int(input("digite o valor de a: "))
V2 = int(input("digite o valor de b: "))
V3 = int(input("digite o valor de c: "))

x1,x2 = bhaskara(V1,V2,V3)

print(f"o x1 é {x1} e o x2 é {x2}   :))))))))):):):):):):):):):):):)")