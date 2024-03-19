m = input().split()
c = m[0]
n = int(m[1])

if c=='A':
    for i in range(1,n+1):
        print(i,end=' ')
elif c=='D':
    for i in range(n):
        print(n,end=' ')
        n = n-1