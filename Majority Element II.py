# Majority Element II
nums = [3,2,3]

# Naive Solution
count = {}
ans = []
for n in nums:
    if n in count:
        count[n]+=1
    else:
        count[n]=1
for key,value in count.items():
    if value>len(nums)/3:
        ans.append(key)
print(ans)

# Optimized Solution
n1 = n2 = float("inf")
c1 = c2 = 0
for num in nums:
    if n1 == num:
        c1+=1
    elif n2 == num:
        c2+=1
    elif c1 == 0:
        n1 = num
        c1 = 1
    elif c2 ==0:
        n2 = num 
        c2 = 1
    else:
        c1-=1
        c2-=1
x = len(nums)/3
ans = []
if nums.count(n1)>x:
    ans.append(n1)
if nums.count(n2)>x:
    ans.append(n2)
print(ans)
