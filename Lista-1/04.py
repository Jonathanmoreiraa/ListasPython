# Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião em relação ao filme (3- ótimo; 2- bom; 1- regular).
#     Faça um programa que receba a idade e a opinião de um número indeterminado de pessoas. Para finalizar a entrada deve ser digitado uma idade negativa ou zero. Calcule e mostre:
# •	A média das idades das pessoas que responderam ótimo;
# •	A quantidade de pessoas que responderam regular;
# •	A quantidade de pessoas que responderam bom.


idade=int(input("Informe sua idade ou digite um número abaixo de 0 para encerrar: "))
ot=0
b=0
reg=0
total=0
media=0
while idade>0:
    op=int(input("Informe sua opinião do filme com o numero que corresponde a opção sua opinião: \n 3- Ótimo \n 2- Bom \n 1- Regular \n R: "))
    if op == 3:
        ot+=idade
    elif op == 2:
        b+=1
    elif op == 1:
        reg+=1
    else:
        print("Opção inválida! Tente outra vez!")
    total+=1
    idade=int(input("Informe sua idade ou digite um número abaixo de 0 para encerrar: "))

if total>1:
    media=ot//total
print("A média das idades das pessoas que responderam ótimo é", media)
print("A quantidade de pessoas que responderam 'bom' é",b)
print("A quantidade de pessoas que responderam 'regular' é",reg)
