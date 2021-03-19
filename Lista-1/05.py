# Faça um programa que receba dez números inteiros. Calcule e mostre:
# •	A quantidade de números primos
# •	A soma dos números ímpares
# •	A média dos pares

n=[]
pr=0
par=0
imp=[]
tot=0
for i in range (10):
    n.append(int(input("Insira um número inteiro: ")))
    l=0
    for x in range (1, n[i]+1):
        if n[i]%x==0:
            l+=1
    if l == 2:
        pr+=1
    if n[i]%2==0:
        par+=n[i]
    else:
        imp.append(n[i])
    tot+=1

print("A quantidade de números primos é",pr)
print("A soma dos números ímpares é",sum(imp))
print("A média dos pares é",par/tot)
