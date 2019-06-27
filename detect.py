a=int(input())
arr=list(map(int,input().split()))
sum=0
for x in range(1,a):
    for y in range(x):
        if arr[x]>arr[y]:
            sum+=arr[y]
print(sum)
