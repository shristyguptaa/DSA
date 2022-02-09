# Triangle
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
ans = triangle [-1][:]
for w in reversed (triangle[:-1]):
    for idx,ele in enumerate(w):
        ans[idx] = min(ans[idx],ans[idx +1])+ele
print (ans[0])
