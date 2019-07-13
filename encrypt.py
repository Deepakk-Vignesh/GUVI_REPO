a=list(input())
b=list(input())
c=len(a)
for i in range(c):
    print(chr(ord('a')+(ord(a[i])+1+ord(b[i])-2*ord('a'))%26),end="")
