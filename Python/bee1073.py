N = int(input())
pot = 0

for i in range(2, N+1, 2):
    pot = i ** 2
    print("{}^2 = {}".format(i, pot))