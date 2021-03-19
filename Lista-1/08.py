# Faça um programa que receba um número, calcule e mostre a tabuada desse número na tela.
n=int(input("Insira um número: "))
print("A tabuada do", n, "de 1 à 10 é: ")
for i in range (1, 11):
    print (n,"x",i,"=",n*i)
