def even(k,s):
    if k%2==0:
        l[s]=k/2
    print(int(l[s]),end='')

l = []
n = int(input())

l = list(map(int,input().split()))
for i in range(n):
    even(l[i],i)