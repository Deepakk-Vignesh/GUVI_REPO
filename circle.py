x=[1,0,-1,0]
y=[0,1,0,-1]
s=list(input())
pos=16384
c=[0,0]
for x1 in s:
    if x1=='G':
        p=pos%4
        c[0]+=x[p]
        c[1]+=y[p]
    elif x1=='L':
        pos+=1;
    else:
        pos-=1
if c[0]==0 and c[1]==0:
    print("yes")
else:
    print("no")
