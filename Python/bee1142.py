N = int(input())

for i in range(1, 4*N + 1):
    if i%4 == 0:
        print("PUM")
    else:
        print(i, end=" ")