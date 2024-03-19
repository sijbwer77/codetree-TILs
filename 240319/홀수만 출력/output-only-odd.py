m = input().split()
a,b = map(int,m)

for i in range(a,b+1,2):
    if a%2==1:
        print(i,end=' ')
    else:
        print(i+1,end=' ')