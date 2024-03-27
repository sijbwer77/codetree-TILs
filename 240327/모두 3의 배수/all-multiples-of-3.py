a = []
for i in range(5):
    a.append(int(input()))

c = 0

for i in range(5):
    if a[i]%3==0:
        c+=1

if c==5:
    print(1)
else:
    print(0)