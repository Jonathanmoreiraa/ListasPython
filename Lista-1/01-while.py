menor = float('inf')
soma = 0
x=0
i=1
media=0
total=0
while i <= 10:
    num = int(input("Digite o número inteiro: "))
    if num<menor:
        menor = num
    if num%2==0 and num>10:
        soma+=num
    if num%2:
        x+=1
    if num > 20:
        media+=1
    total+=1
    i+=1

me=(media/total)*100

print("a) O menor número é: ", menor)
print("b)a soma dos números pares e maiores que 10: ", soma)
print("c)a quantidade de números ímpares: ", x)
print("d)a média dos números maiores que 20: ", me, "%")
