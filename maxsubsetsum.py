n=int(input())
l1=list(map(int,input().split()))
k=0
for x in l1:
	if x<0 :
		k=k+1
if k==0 :
	print(sum(l1),end="")
elif k==n :
	print(max(l1),end="")
else :
	for x in l1 :
		if x<0 :
			l1.remove(x)
	print(sum(l1),end=" ")
