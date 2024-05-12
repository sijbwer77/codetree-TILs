def swap(x,y):
    return y,x

m,n = map(int,input().split())

m,n = swap(m,n)
print(m,n)