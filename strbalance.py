a=input()
b=input()
c=a.index('|')
d=len(a)
if d%2==1 or c!=d//2-1 and c!=d//2:
    print("Impossible")
else:
    if c==d//2-1:
        a=b+a
    else:
        a=a+b
    print(a)
