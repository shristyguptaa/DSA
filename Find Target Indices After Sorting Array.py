# Find Target Indices After Sorting Array
nums = [1,2,5,2,3]
target = 2

# Naive Solution
lst = []
nums = sorted(nums)
for i in range(len(nums)):
    if nums[i]==target:
        lst.append(i)
print(lst)

# Optimized Solution
count = 0
idx = 0
for num in nums:
    if num <target:
        idx+=1
    if num == target:
        count+=1
ans = []
for i in range(count):
    ans.append(idx+i)
print(ans)
