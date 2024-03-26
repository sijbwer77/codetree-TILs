t = []

while True:
    a = int(input())
    if a>29 or a<20:
        break
    else:
        t.append(a)
print('%.2f'%(sum(t)/len(t)))