n = int(input())
for i in range(1,n+1):
    if i==1:
        print('* '*n)
    else:
        if i%2==1:
            print('    '*int((i-1)/2),end='')
            print('   *'*(int(n/2)-int((i-1)/2)))
        else:
            print('    '*int((i-2)/2),end='')
            print('   *'*(int(n/2)-int((i-2)/2)))