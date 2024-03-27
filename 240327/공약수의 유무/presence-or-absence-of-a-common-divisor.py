a,b = map(int,input().split())

x = 0

for i in range(2,b+1):
    if 1920%i==0 and 2880%i==0:
        x = 1
if x==0:
    print(0)
else:
    print(1)