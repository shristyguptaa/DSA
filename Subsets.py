# Subsets
nums = [1,2,3]
set = [[]]
# print(len(set))
for a in nums:
    for i in range(len(set)):  #2^n
        set.append(set[i]+[a])
print(set)
