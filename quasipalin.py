#edited
a = int(input())
while a%10==0:
    a=a//10
a=str(a)
b=a[::-1]
if a==b:
    print("yes")
else:
    print("no")
