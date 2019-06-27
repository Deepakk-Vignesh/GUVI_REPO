#changed
n,q=map(int,input().split())
b=list(map(int,input().split()))
for x in range (q):
    s,t=map(int,input().split())
    y=0
    for a in range(s-1,t):
        y=y^b[a]
    print(y)
