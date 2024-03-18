a = input().split()
a = list(map(int,a))

bmi = int(a[1]/((a[0]/100)**2))

if bmi>=25:
    print(bmi)
    print('Obesity')
else:
    print(bmi)