n = int(input())
arr = list(map(float,input().split()))

j = sum(arr)/len(arr)

print('%.1f' %j)
if j>=4:
    print('Perfect')
elif j>=3:
    print('Good')
else:
    print('Poor')