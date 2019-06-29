n=int(input())
b=list(map(int,input().split()))
b=sorted(b)
sat=1
for i in range(1,n):
    b[i]+=b[i-1]
for i in range(1,n):
    if b[i-1]<=(b[i]-b[i-1]):
        sat+=1;
print(sat)
