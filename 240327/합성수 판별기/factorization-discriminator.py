n = int(input())
s = 0

for i in range(1,n):
    if n%i==0:
        print('C')
        break
    if n-1==i:
        print('N')