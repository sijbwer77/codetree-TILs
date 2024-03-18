m = input().split()
m = list(map(int,m))

a = m[0] if m[0]>m[1] else m[1]
print(a)