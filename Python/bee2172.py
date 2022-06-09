valores = input().split(" ")
x, m = valores
x = int(x)
m = int(m)

while (x + m) != 0:
    e = x * m
    print(e)
    valores = input().split(" ")
    x, m = valores
    x = int(x)
    m = int(m)