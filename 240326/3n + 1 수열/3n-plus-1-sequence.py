n = int(input())
g = 0
while True:
    if n%2==0:
        n = n/2
    elif n%2==1:
        n=n*3+1
    g+=1
    if n==1:
        break
print(g)