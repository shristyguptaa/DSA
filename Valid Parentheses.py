# Valid Parentheses
s = "()"
dct = {"}":"{","]":"[",")":"("}
stack = []
for i in s:
    if i in "[({":
        stack.append(i) # append into stack
    if i in "])}":
        if len(stack)==0:
            print (False)
        temp = stack.pop()
        if dct[i]==temp:
            continue
        else:
            print (False)
if len(stack)!=0:
    print (False)
print (True)
