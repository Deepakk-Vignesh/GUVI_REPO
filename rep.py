n = int(input())
l=list(map(int,input().split()))
k=0
for i in range(n):
	if l.count(l[i])>1:
		print(l[i],end="")
		break;
	else :
		k=k+1
if k==n :
	print("unique",end="")
