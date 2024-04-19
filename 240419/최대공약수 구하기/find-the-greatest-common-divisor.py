m,n = map(int,input().split())

def eo(m,n):
    for i in range(m+n+1,1,-1):
        if m%i==0 and n%i==0:
            return(i)
            break
print(eo(m,n))