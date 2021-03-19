# Faça um programa que receba 10 números inteiros. Calcule o fatorial de cada número e mostre na tela.
n=[]
for i in range (10):
    n.append(int(input("Informe um número inteiro: ")))
    r=1
    for e in range (1, n[i]+1):
        r = r*e
    print("O fatorial de", n[i], "é:", r)
