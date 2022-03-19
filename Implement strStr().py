# Implement strStr()
haystack = "hello"
needle = "ll"
# O(n^2) time and O(n) space because of slicing
n = len(needle)
for i in range(len(haystack)-n+1):
    if needle == haystack[i:i+n]:
        return i
return -1
