n = int(input())
c = 0
for i in range(1,n+1):
    if i%4==0:
        if i%100==0 and i%400!=0:
            pass
        else:
            c+=1

print(c)