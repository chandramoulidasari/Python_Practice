n = int(input())
for i in range(n):
	a,b,c=map(int,input().split())
	if a+c<=b:
		print("YES")
	else:
		print("NO")