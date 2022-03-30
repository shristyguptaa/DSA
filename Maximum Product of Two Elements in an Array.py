# Maximum Product of Two Elements in an Array
nums = [3,4,5,2]

# Naive Solution
nums = sorted(nums)
res = (nums[-1]-1)*(nums[-2]-1)
return res
