n = int(input())
nh = n // 3600
n = n - nh*3600

nm = n // 60
n = n - nm*60

ns = n // 1
n = n - ns*1

print('{}:{}:{}'.format(nh, nm, ns))