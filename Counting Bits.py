# Counting Bits
n = 2
arr = [0]
for i in range(1,n+1):
    if i % 2 == 1:
        arr.append(arr[i-1]+1)
    else:
        arr.append(arr[i//2])
print(arr)
