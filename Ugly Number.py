# Ugly Number

if n <= 0:
    return False

for p in [2,3,5]:
    while n % p == 0:
        n = n // p
return n == 1
