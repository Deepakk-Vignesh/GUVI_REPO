from collections import Counter 
a=input()
if len(Counter(a))>=26:
    print("yes")
else:
    print("no")
print(Counter(a))
