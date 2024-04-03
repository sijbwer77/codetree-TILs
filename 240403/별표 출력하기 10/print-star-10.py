n = int(input())

for i in range(1,n+1):
	if i%2==1:
		print('* '*int((i+1)/2))
	else:
		print('* '*int(n+1-i/2))

for i in range(n,0,-1):
	if i%2==1:
		print('* '*int((i+1)/2))
	else:
		print('* '*int(n+1-i/2))