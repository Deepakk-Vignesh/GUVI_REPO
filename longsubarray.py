a=int(input())
b=list(map(int,input().split()))
l=0
for i in range(a-2):
    c=1
    while i<(a-1) and b[i]<b[i+1]:
        c=c+1
        i=i+1
    l=c if c>l else l;
    i=i-1
print(l)
