n = int(input())
a =[]
cnt=0
sum = 0
for n in range(n):
    a.append(list(map(int,input().split())))


for i in range(n):
    for j in range(4):
        sum +=a[i][j]
    if sum/4>=60:
        print('pass')
        cnt+=1
    else:
        print('fail')
    sum = 0
print(cnt)