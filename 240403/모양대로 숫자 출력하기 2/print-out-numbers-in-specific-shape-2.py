a = [2,4,6,8]
n = int(input())
cnt = 0
for i in range(n):
    for j in range(n):
        print(a[cnt],end=' ')
        if cnt>=3:
            cnt=0
        else:
            cnt+=1
    print()