n = int(input())
li = [1]
li.append(n)

num = 0
while num<100:
    num = li[-1]+li[-2]
    li.append(num)

for item in li:
    print(item,end=' ')