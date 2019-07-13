a=input()
b=input()
c=a.index('|')
d=len(a)+len(b)
if d%2==0:
    print("Impossible")
else:
    if c<=d//2-1:
        a=b+a
    else:
        a=a+b
    c=a.index('|')
    if c!=d//2-1 and c!=d//2:
        print("Impossible")
    else:
        print(a)
