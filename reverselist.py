#changed
n=int(input())
l1=list(map(int,input().split()))
for x in range(n-1):
	print(l1[n-1-x],end="->")
print(l1[0],end="")
