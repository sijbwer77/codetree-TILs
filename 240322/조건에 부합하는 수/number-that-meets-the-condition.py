a = int(input())
s = []
for i in range(1,a+1):
    if i%4!=0 and i%2==0:
        continue
    if (i//8)%2==0:
        continue
    if i%7<4:
        continue
    print(i, end=' ')