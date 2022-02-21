# Remove Element 
nums = [0,1,2,2,3,0,4,2]
val = 2

# Naive Solution
temp = [] 
count = 0
for i in range(len(nums)):
    if nums[i]!=val:
        temp.append(nums[i])
        count+=1
nums[:]=temp[:]
print (count)
print (nums)

# Best Solution
left = 0
right = len(nums)-1
counter = 0
while left<=right:
	if nums[left] == val:
		nums[left],nums[right]=nums[right],nums[left]
		right-=1
	elif nums[left]!=val:
		left+=1
		counter+=1
print (counter)
print(nums)
