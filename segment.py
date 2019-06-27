n,q=map(int,input().split())
b=list(map(int,input().split()))
for x in range (1,n):
    b[x]+=b[x-1]
for x in range (q):
    s,t=map(int,input().split())
    y=b[t-1] if s==1 else b[t-1]-b[s-2]
    print(y)
