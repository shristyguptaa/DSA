# Final Value of Variable After Performing Operations
lst = ["--X","X++","X++"]
X=0
for i in range(0,len(lst)):
    if lst[i] == '--X'or lst[i] == "X--" :
        X-=1
    elif lst[i] == 'X++' or lst[i] == '++X' :
        X+=1
print (X)
