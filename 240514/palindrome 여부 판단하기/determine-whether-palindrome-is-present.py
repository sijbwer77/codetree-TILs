def tf(string):
    string1 = string
    string.reverse()
    if string == string1:
        print('Yes')
    else:
        print('No')

a = input()
li = []


for i in range(len(a)):
    li.append(a[i])


tf(li)