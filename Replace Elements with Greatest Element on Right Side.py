# Replace Elements with Greatest Element on Right Side
arr = [17,18,5,4,6,1]

# Naive Solution
for i in range(len(arr)-1):
    newMax = max(arr[i+1:])
    arr[i]=newMax
arr[-1]=-1 
print(arr)

# Optimised Solution
rightMax = arr[-1]
arr [-1] = -1
for idx in reversed(range(len(arr)-1)):
  temp = arr[idx]
  arr[idx]=rightMax
  rightMax = max(temp,rightMax)
print(arr)
