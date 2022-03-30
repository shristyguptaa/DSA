# Roman to Integer
S = "MCMXCIV"
roman ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
res = 0
for i in range(len(S)):
    if i+1<len(S) and roman[S[i]]<roman[S[i+1]]:
        res-=roman[S[i]]
    else:
        res+=roman[S[i]]
print (res)
