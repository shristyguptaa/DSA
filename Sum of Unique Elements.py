# Sum of Unique Elements
nums = [1,2,3,2]

# Naive Solution
lst = []
for num in nums:
    if nums.count(num)==1:
        lst.append(num)
return sum(lst)
