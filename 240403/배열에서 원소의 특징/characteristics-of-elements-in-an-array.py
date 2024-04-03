a = list(map(int,input().split()))
ms = 0
for i in range(len(a)):
    if a[i]%3==0:
        print(a[i-1])
        break