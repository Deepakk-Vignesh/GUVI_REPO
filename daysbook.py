n,t=map(int,input().split())
a=list(map(int,input().split()))
d=0
i=0
while t>0:
    t=t-86400+a[i];
    i=i+1
    d=d+1
print(d)
