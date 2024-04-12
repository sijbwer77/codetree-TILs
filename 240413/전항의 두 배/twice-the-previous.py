a = list(map(int,input().split()))
temp = 0
for i in range(8):
    temp = a[-1] + 2*a[-2]
    a.append(temp)

for item in a:
    print(item,end=' ')