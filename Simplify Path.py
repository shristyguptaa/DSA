# Simplify Path
path = "/home/"

stack = []
path2 = path.split("/")
for dir in path2:
    if dir == '..':
        if len(stack)>0: # so it doesn't underflow
            stack.pop()
    elif dir == '.' or dir == '':
        continue
    else:
        stack.append(dir)
return "/"+"/".join(stack)
