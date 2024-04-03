n = int(input())

for i in range(1,n+1):
    if i==1:
        print('* '*n)
    else:
        if i%2==0:
            print('    '*int((i-2)/2))
            print('   *'*int((n/2)+1-i))
        else:
            print('    '*int((i-1)/2))
            print('   *'*int((n/1)+1-i))