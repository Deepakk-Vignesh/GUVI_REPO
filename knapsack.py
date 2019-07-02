from itertools import combinations
n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(k-1):
    a=a+a
b=list(combinations(a, k))
c=[sum(i) for i in b]
c=list(set(c))
for i in c:
    print(i,end=" ")
