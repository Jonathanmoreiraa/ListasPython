# Faça um programa que receba dez números inteiros. Calcule e mostre:
# •	A soma dos números primos
# •	A média dos números múltiplos de 3 que são maiores que 10


n=[]
pr=[]
total=0
me=0
for i in range (10):
    n.append(int(input("Insira um número: ")))
    l=0
    for r in range(1, n[i]+1):
        if n[i]%r==0:
            l+=1
    if (l==2):
        pr.append(n[i])
    for m in range (1):
        if n[i]%3==0 and n[i]>10:
            me+=n[i]
    total+=1
    
soma=sum(pr)
media=me/total
print ("A soma dos números primos é: ", soma)
print ("A média de números múltiplos de 3 que são maiores que 10 é: ", media)
