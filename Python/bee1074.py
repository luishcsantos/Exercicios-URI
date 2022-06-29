N = int(input())
valor = 0

for i in range(1, N+1):
    valor = int(input())
    if valor == 0:
        print("NULL")
    elif (valor%2 == 0) and valor >= 0:
        print("EVEN POSITIVE")
    elif (valor%2 != 0) and valor >= 0:
        print("ODD POSITIVE")
    elif (valor%2 == 0) and valor < 0:
        print("EVEN NEGATIVE")
    elif (valor%2 != 0) and valor < 0:
        print("ODD NEGATIVE")