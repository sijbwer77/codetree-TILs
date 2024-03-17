a = input().split()
a = list(map(int,a))

print(sum(a))
print(int(sum(a)/len(a)))
print(int(sum(a)-sum(a)/len(a)))