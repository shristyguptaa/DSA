# Minimum Domino Rotations For Equal Row
tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]

for target in [tops[0],bottoms[0]]:
    rotateBot = rotateTop = 0
    for i in range(len(tops)):
        if tops[i]!=target and bottoms[i]!=target:
            break
        if tops[i]!=target:
            rotateBot+=1
        if bottoms[i]!=target:
            rotateTop+=1
        if i == len(tops)-1:
            return min(rotateBot,rotateTop)
return -1
