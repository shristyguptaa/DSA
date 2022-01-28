# Two Sum
nums = [2,7,11,15]
target = 9

# Naive Solution
for i in range(0, len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print ([i,j])

# Best Solution
dct = {}
for i,num in enumerate(nums):
    if num in dct:
        print ([dct[num],i])
    else:
        dct[target-num]=i
