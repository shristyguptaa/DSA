# Two Sum II - Input Array Is Sorted
nums = [2,7,11,15]
target = 9
left = 0
right = len(nums)-1
while left<right:
    if nums[left]+nums[right]==target:
        print ([left+1,right+1])
        break
    elif nums[left]+nums[right]>target:
        right-=1
    else:
        left+=1
