# Find Numbers with Even Number of Digits
nums = [12,345,2,6,7896]

# Naive Solution
count = 0
for num in nums:
    if len(str(num))%2==0:
        count+=1
return count
