a=int(input())
b=[]
for x in range(a):
    b.insert(x,input())
b=sorted(b)
i=0
s1=list(b[0])
s2=list(b[a-1])
while i<len(s1) and s1[i]==s2[i]:
    print(s1[i],end="")
    i+=1
