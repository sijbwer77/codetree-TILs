a = int(input())
a_r = a
x=[]

while len(x)<2:
    print(a, end=' ')
    if a%5==0:
        x.append(a)
    a+=a_r