# Monotonic Array
nums = [1,2,2,3]

# Solution 1
isInncreasing = True if nums[0]<=nums[-1] else False
i,j=0,1
if isInncreasing:
    while j<len(nums):
        if nums[i]<=nums[j]:
            i+=1
            j+=1
        else:
            print (False)
else:
    while j<len(nums):
        if nums[i]>=nums[j]:
            i+=1
            j+=1
        else:
            print (False)
print (True)

# Solution 2
inc, dec = True, True 
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        inc = False
    if nums[i]<nums[i+1]:
        dec =  False

print (inc or dec)
