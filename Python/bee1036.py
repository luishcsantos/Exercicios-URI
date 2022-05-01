import math
linha1 = input().split(" ")
A, B, C = linha1
A = float(A)
B = float(B)
C = float(C)
delta = (B ** 2) - (4 * (A * C))
if A == 0:
    print('Impossivel calcular')
else:
    if delta < 0:
        print('Impossivel calcular')
    else:
        R1 = (- B + (math.sqrt(delta))) / (2 * A)
        R2 = (- B - (math.sqrt(delta))) / (2 * A)
        print('R1 = {:.5f}'.format(R1))
        print('R2 = {:.5f}'.format(R2))
