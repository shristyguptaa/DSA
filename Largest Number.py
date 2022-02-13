# Largest Number
nums = [10,2]

def greaterOrEqual(self, digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))

ans = ''
while nums != []:
    maxDigit = 0
    for num in nums:
        if self.greaterOrEqual(num, maxDigit):
            maxDigit = num
    ans += str(maxDigit)
    nums.remove(maxDigit)
print (0) if ans[0]=='0' else ans
