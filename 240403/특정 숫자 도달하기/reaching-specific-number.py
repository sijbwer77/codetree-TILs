a = list(map(int,input().split()))
b = []
for i in range(10):
    if a[i]>=250:
        break
    b.append(a[i])
print(sum(b), '%.1f'%(sum(b)/len(b)))