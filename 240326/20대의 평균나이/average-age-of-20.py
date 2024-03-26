t = []

while True:
    a = int(input())
    if a<=29 and a>=20:
        break
    else:
        t.append(a)
print(sum(t))