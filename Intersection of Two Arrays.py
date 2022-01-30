# Intersection of Two Arrays
nums1 = [1,2,2,1]
nums2 = [2,2]

# Solution 1
out = []
for num in nums2:
    if num in nums1 and num not in out:
        out.append(num)
print (out)

# Solution 2
nums1.sort()
nums2.sort()
out = []
i,j =0,0
while i <len(nums1) and j < len(nums2):
    if nums1[i]==nums2[j] and nums1[i] not in out:
        out.append(nums1[i])
        i+=1
        j+=1
    elif nums1[i]<nums2[j]:
        i+=1
    else:
        j+=1
print (out)

# Solution 3
print (list(set(nums1) & set(nums2)))
