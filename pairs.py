n,k=map(int,input().split())
b=list(map(int,input().split()))
b=sorted(b)
f=0
for x in range(n):
    s=x+1
    e=n-1
    while(s<=e):
        m=(s+e)//2
        if b[x]+b[m]==k:
            break;
        elif b[x]+b[m]>k:
            e=m-1
        else:
            s=m+1
    if s<=e:
        f=1
        print("yes")
        break;
if f==0:
    print("no")
