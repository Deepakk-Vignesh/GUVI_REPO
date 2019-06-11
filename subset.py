n,m = map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
if (all(x in l1 for x in l2)):
	print("YES",end="")
else :
	print("NO",end="")
