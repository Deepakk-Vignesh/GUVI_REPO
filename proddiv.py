n=int(input())
l1=list(map(int,input().split()))
k=1
for x in l1:
	k=k*x
for x in l1:
	print(k//x,end=" ")
