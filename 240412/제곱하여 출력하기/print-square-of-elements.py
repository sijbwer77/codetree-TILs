n = int(input())
li = list(map(int,input().split()))
li2 = []

for i in range(n):
    li2.append(li[i]**2)

for i in range(n):
    print(li2[i],end=' ')