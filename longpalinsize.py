def LCSubStr(X, Y, n):
    LCSuff = [[0 for k in range(n+1)] for l in range(n+1)]
    result = 0 
    for i in range(n + 1): 
        for j in range(n + 1): 
            if (i == 0 or j == 0): 
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]): 
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j]) 
            else: 
                LCSuff[i][j] = 0
    return result

a=input()
b=a[::-1]
c=LCSubStr(a,b,len(a))
print(len(a)- (0 if c==1 else c))
