a = list(map(int,input().split()))

for n in a:
    if n==0:
        break
    elif n%2==0:
        print(n//2,end=' ')
    else:
        print(n+3,end=' ')