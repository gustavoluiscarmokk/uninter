import hipotenusa.py

pessoas = []
pessoas.append({'nome':'Bruno','sexo':'M'})
pessoas.append({'nome':'Maria','sexo':'F'})
pessoas.append({'nome':'Clara','sexo':'F'})
pessoas.append({'nome':'Jose','sexo':'M'})

for pessoa in pessoas:
    s = pessoa['sexo']
    n = pessoa['nome']
    print(f"Bem vindo Sr. {n}" if s =="M" else f"Bem-vinda Sra. {n}")

imprimirBatata()