a=int(input())
b=2**a
for n in range(b):
    c=bin(n).replace("0b","")
    for i in range(a-len(str(c))):
        print(0,end="")
    print(c)
