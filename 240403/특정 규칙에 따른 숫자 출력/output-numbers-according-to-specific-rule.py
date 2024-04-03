n = int(input())
k = list(range(1,10))
cnt = 0

for i in range(n):
    print('  '*(i),end='')
    for j in range(n-i):
        print(k[cnt],end=' ')
        cnt+=1
        if cnt>=9:
            cnt=0
    print()