m,n = map(int,input().split())

def ri(n,m):
    k = n
    while True:
        if k%n==0 and k%m==0:
            return k
        k+=1

print(ri(n,m))