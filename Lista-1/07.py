# Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas. Finalize digitando idade igual 0.
tot=0
s=0
idade=int(input("Informe uma idade ou digite 0 para encerrar: "))
while idade!=0:
    if idade>0:
        s+=idade
        tot+=1
    else:
        print("Idade inválida, tente outra vez!")
    idade=int(input("Informe outra idade ou digite 0 para encerrar: "))
if tot>0:
    print("A média das idades é: ", s//tot, "anos")
