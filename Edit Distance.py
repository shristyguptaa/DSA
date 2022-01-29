# Edit Distance
str1 = "horse"
str2 = "ros"

editDistance = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
for i in range(len(str1)+1):
    editDistance[0][i]=i
for j in range(len(str2)+1):
    editDistance[j][0]=j

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1]==str2[j-1]:
            editDistance[j][i]=editDistance[j-1][i-1]
        else:
            editDistance[j][i]=min(editDistance[j-1][i-1],editDistance[j-1][i],
            editDistance[j][i-1])+1

print (editDistance[-1][-1])
