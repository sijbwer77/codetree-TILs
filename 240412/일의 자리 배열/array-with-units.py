n = list(map(int,input().split()))

print(n[0], n[1],end=' ')

for i in range(8):
    if n[-1]+n[-2]>=10:
        n.append(n[-1]+n[-2]-10)
    else:
        n.append(n[-1]+n[-2])
    print(n[-1],end=' ')