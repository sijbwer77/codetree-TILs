a,b = map(int,input().split())
prod = 1
for i in range(a,b,a):
    prod *=i
print(prod)