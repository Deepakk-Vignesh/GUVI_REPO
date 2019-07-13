a=int(input())
b=list(map(int,input().split()))
c=[1]*a
for i in range(a):
    for j in range(i):
        if b[i]>b[j]:
            if (c[j]+1)>c[i]:
                c[i]=c[j]+1
print(max(c))
