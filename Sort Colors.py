# Sort Colors
nums = [2,0,2,1,1,0]

# Naive Solution
dct = {0:0,1:0,2:0}
for i in range(0,len(nums)):
    dct[nums[i]]+=1
out = []
for key, value in dct.items():
    out+=([key]*value)
print(out)

# Best Solution
low,mid,right = 0,0,len(nums)-1
while mid<=right:
    if nums[mid] == 0:
        nums[low],nums[mid] = nums[mid],nums[low]
        mid += 1
        low += 1
    elif nums[mid] == 2:
        nums[right],nums[mid] = nums[mid],nums[right]
        right -= 1
    else:
        mid += 1
print(nums)
