# Number of Good Pairs
nums = [1,2,3,1,1,3]

# Naive Solution
count = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]==nums[j] and i<j:
            count+=1
return count
