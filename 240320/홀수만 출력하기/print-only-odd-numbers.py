n = int(input())
b = []
for i in range(n):
    a = int(input())
    if a%3==0 and a%2==1:
        b.append(a)
for i in range(len(b)):
    print(b[i])