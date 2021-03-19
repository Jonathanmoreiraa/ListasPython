# Foi realizada uma pesquisa para determinar o índice de mortalidade infantil em um certo período. Faça um programa que:
# a.	Leia o número de crianças nascidas no período
# b.	Identifique o sexo (M ou F)
# c.	Identifique o tempo de vida de cada criança em meses.
# O programa deve calcular:
# •	A percentagem de crianças do sexo masculino mortas no período
# •	A percentagem de crianças do sexo feminino mortas no período
# •	A percentagem de crianças que viveram 24 meses ou menos no período

b=0
g=0
t=0
sex = []
per =str(input("Informe um período de meses: "))
cri = int(input("Informe quantas crianças nasceram nesse período: "))
for i in range (1, cri+1):
    sex=int(input("Informe o sexo da " + str(i) + "ª criança, como '1' para menino e/ou '2' para menina!: \n"))
    comp = str(input("Essa criança faleceu? Responda com 's' para sim ou 'n' para não: \n"))
    if comp == 'S' or comp == 's':
        tem=int(input("Informe o tempo de vida dessa criança em meses: "))
        if tem <= 24:
            t+=1
    if sex == 1 and comp == 's':
        b+=1
    elif sex == 2 and comp == 's':
        g+=1

porcm=(b/cri)*100
porcg=(g/cri)*100
porc=(t/cri)*100

print("A porcentagem de crianças do sexo masculino mortas nesse período é de", porcm, "%")
print("A porcentagem de crianças do sexo feminino mortas nesse período é de", porcg, "%")
print("A porcentagem de crianças que faleceram com 24 meses ou menos nesse período é de", porc, "%")

