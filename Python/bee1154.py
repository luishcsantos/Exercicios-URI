media = 0
soma = 0
n = 0
idade = int(input())

while idade > 0:
    soma = soma + idade
    n = n + 1
    idade = int(input())

media = soma / n

print("{:.2f}".format(media))