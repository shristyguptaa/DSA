# Find First and Last Position of Element in Sorted Array

# Solution 1(Naive Solution)
if len(nums) == 0:
    print ([-1,-1])
left = 0
right = len(nums)-1
mid = (left+right)//2
while left<=right:
    mid = (left+right)//2
    if nums[mid]==target:
        break
    if nums[mid]<target: 
        left = mid+1
    else:
        right = mid-1
if nums[mid]!=target:
    print ([-1,-1])
left = mid
right = mid
while left-1 >= 0 and nums[left-1]==target: 
    left-=1
while right+1 < len(nums) and nums[right+1]==target: 
    right+=1

print ([left,right])

# Solution 2(Best Solution)
if len(nums) == 0:
    print ([-1,-1])
left = 0
right = len(nums)-1
mid = (left+right)//2
while left<=right:
    mid = (left+right)//2
    if nums[mid]==target:
        break
    if nums[mid]<target:
        left = mid+1
    else:
        right = mid-1
if nums[mid]!=target:
    print ([-1,-1])
temp = mid
midTemp = mid
while left<=temp:
    mid = (left+temp)//2
    if nums[mid]==target:
        temp = mid-1
    else:
        left = mid+1
ans = []
ans.append(left)
temp = midTemp
while temp<=right:
    mid = (right+temp)//2
    if nums[mid]==target:
        temp = mid+1
    else:
        right = mid-1
ans.append(right)
print (ans)
