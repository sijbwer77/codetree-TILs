a,b = map(int,input().split())

if a>b:
    for i in range(b-a+1):
        print(a,end=' ')
        a = a-1
if a<=b:
    for i in range(b-a+1):
        print(b,end=' ')
        b-=1