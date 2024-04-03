n = int(input())
a =[]
cnt=0
s = 0

for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    for j in range(4):
        s = s + a[i][j]
    if s/4<60:
        print('fail')
    else:
        print('pass')
        cnt+=1
    
    s = 0
print(cnt)