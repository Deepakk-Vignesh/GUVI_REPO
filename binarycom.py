def f(l):
    l.sort(key=lambda n:bin(n).count('1'))
    return l
a=int(input())
b=2**a
d=[i for i in range(b)]
d=f(d)
for n in d:
    c=bin(n).replace("0b","")
    for i in range(a-len(str(c))):
        print(0,end="")
    print(c)
