# Guess Number Higher or Lower
n = 10
pick = 6

low = 0
high = n
while low<=high:
    mid = (low+high)//2
    t = guess(mid)
    if t==0:
        return mid
    if t ==-1:
        high = mid-1
    else:
        low= mid+1
return -1
