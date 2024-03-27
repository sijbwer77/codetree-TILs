a,b,c = map(int,input().split())
s = 0
for i in range(a,b+1):
    if i%c==0:
        print('YES')
        s = 0
        break
if s!=0:
    print('NO')