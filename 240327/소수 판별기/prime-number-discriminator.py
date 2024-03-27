n = int(input())
k= 0
for i in range(2,n):
    if n%i==0:
        print('C')
        k = 1
        break
if k==0:
    print('P')