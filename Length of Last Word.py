# Length of Last Word

# Naive Solution
st = st.strip()
st = st.split(" ")
return len(st[-1])

# Best Solution
i,length = len(s)-1,0
while s[i]==" ":
    i-=1
while i>=0 and s[i]!=" ":
    length+=1
    i-=1
return length
