a,b = map(int,input().split())
l = a//b
print(l,end='')
print('.',end='')
o = a%b
for i in range(20):
    o = o*10
    print(o//b,end='')
    o = o%b