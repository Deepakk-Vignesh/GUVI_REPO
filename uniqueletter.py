stri=input()
stri=list(stri)
for x in range(len(stri)):
	if stri[x]!=-1 :
		print(stri[x],end="")
		a=stri[x]
		for y in range(len(stri)):
			if a==stri[y] :
				stri[y]=-1
