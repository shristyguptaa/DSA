# Maximum Subarray
nums = [-2,1,-3,4,-1,2,1,-5,4]
globalMax = nums[0]
localMax = nums[0]
for num in nums[1:]:
    localMax = max(num,localMax+num)
    globalMax = max(globalMax,localMax)
print (globalMax)
