# Escreva um programa que leia um conjunto de 10 números inteiros. Calcule e mostre:
#     a) o menor número
#     b) a soma dos números pares e maiores que 10
#     c) a quantidade de números ímpares
#     d) a média dos números maiores que 20

n=[]
soma=[]
mai=[]
imp=0
tot=0
for i in range (10):
    n.append(int(input("Insira um número inteiro: ")))
    if n[i]%2==0 and n[i]>10:
        soma.append(n[i])
    if n[i]%2:
        imp+=1
    if n[i]>20:
        mai.append(n[i])
    tot+=1

print("O menor número é:", min(n))
print("A soma dos números pares e maiores que 10 é:", sum(soma))
print("A quantidade de números ímpares é: ", imp)
print("A média dos números maiores que 20 é: ", sum(mai)/tot)
