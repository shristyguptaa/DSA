# Contain Duplicates
# Solution 1
seen = {}
for num in nums:
  if num in seen:
    return True
  seen[num] = True
return False

# Solution 2
seen = set()
for num in nums:
  if num in seen:
    return True
  seen.add(num)
return False

# Solution 3
nums.sort()  #nlogn
for i in range(1,len(nums)):  #n
  if nums[i] == nums[i-1]:
    return True
return False
