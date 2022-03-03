# Find All Numbers Disappeared in an Array
nums = [4,3,2,7,8,2,3,1]
lst=[]
nums.sort()
i = 1
idx = 0
while idx<len(nums) :
    if i==nums[idx]:
        i+=1
        idx+=1
    # if value is repeated
    elif nums[idx]==nums[idx-1]  :
        idx+=1
    else:
        lst.append(i)
        i+=1
print(lst)
