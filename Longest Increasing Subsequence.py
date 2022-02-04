# Longest Increasing Subsequence
array = [10, 9, 2, 5, 3, 7, 101, 18]
maxSeq = [1 for a in array]
seq = [None for x in array]
for i in range(len(array)):
    currNum = array[i]
    for j in range(i):
        otherNum = array[j]
        if currNum>otherNum and maxSeq[i]< maxSeq[j]+1:
            maxSeq[i] = maxSeq[j]+1
            seq[i] = j
print(max(maxSeq))
print(seq)     
