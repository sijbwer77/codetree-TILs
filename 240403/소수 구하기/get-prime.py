n = int(input())
b = False
k = []

for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            b = True
    if b==False:
        k.append(i)
    b = False
for i in range(len(k)):
    print(k[i],end=' ')