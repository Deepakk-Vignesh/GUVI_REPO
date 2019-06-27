a=int(input())
b=0
while 2**b < a:
    b=b+1
if 2**b == a:
    print(0)
elif a-2**(b-1)<=2**b-a:
    print(a-2**(b-1))
else:
    print(2**b-a)
