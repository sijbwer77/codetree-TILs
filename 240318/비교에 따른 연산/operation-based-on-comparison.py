a = input().split()
a = list(map(int,a))

b = a[1]
a = a[0]

if a>b:
    print(a*b)
else:
    print(b/a)