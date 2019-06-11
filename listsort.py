n=int(input())
l1=list()
for x in range(n):
	l2=list(map(int,input().split()))
	l1=l1+l2
l1=sorted(l1)
for x in l1:
	print(x,end=" ")
