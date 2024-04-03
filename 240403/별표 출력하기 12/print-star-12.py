n = int(input())
odd = False
if n %2==1:
    if n==0:
        print('*')
    n = n-1
    odd = True
for i in range(1,n+1):
    if i==1:
        if odd:
            print('* '*(n+1))
        else:
            print('* '*n)
    else:
        if i%2==0:
            print('    '*int(i/2-1),end='')
            print('  * '*int((n+2)/2-(i/2)))
            
        else:
            print('    '*int((i+1)/2-1),end='')
            print('  * '*int((n+2)/2-(i/2)))