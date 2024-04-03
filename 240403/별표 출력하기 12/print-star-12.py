l = int(input())
n = 0
if n%2==1:
    n = l-1
else:
    n = l


for i in range(1,n+1):
    if i==1:
        print('* '*l)
    else:
        if i%2==0:
            print('    '*int(i/2-1),end='')
            print('  * '*int((n+2)/2-(i/2)))
            
        else:
            print('    '*int((i+1)/2-2),end='')
            print('  * '*int((n+2)/2-(i/2)))