n = int(input())
k = 0
for i in range(1,2*n):
    if k<=4:
        print('*'*(i))
        print()
        k+=1
    else:
        print('*'*(10-i))
        print()