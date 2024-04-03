n = int(input())
x = list(map(int,input().split()))
x.sort()
for i in range(len(x)):
    if x[i]%2==0:
        print(x[i])