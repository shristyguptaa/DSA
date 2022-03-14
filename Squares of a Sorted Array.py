# Squares of a Sorted Array
nums = [-4,-1,0,3,10]
ans = [0 for i in range(len(nums))]  #n
idx = len(nums)-1
l = 0
r = len(nums)-1
while l<=r:
    x = nums[l]**2
    y = nums[r]**2
    if x<y:
        ans[idx]=y
        r-=1
    else:
        ans[idx]=x
        l+=1
    idx-=1
print(ans)
