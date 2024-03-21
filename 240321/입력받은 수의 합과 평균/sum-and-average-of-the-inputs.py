n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))
print('%s %.1f'%(sum(l),sum(l)/n))