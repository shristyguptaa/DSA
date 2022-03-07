# Number of 1 Bits
n = 00000000000000000000000000001011
res = 0
while n:
    n&=(n-1)
    res+=1
    # res+= n % 2
    # n = n>>1
    # print(n)
print (res)
