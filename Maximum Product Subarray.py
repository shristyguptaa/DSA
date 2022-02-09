# Maximum Product Subarray
nums = [2,3,-2,4]
curMax,curMin =1,1
res = max(nums)
for num in nums:
    if num ==0:
        curMax = 1
        curMin = 1
        continue
    temp = curMax*num
    curMax = max(curMax*num,num*curMin,num)
    curMin = min(temp,num*curMin,num)
    res = max(res,curMax)
print (res)
