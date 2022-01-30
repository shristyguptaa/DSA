# Valid Palindrome
s = "A man, a plan, a canal: Panama"

# For Loop
st = ""
for ch in s:
    if ch.isalnum():
        st+=(ch.lower())
start = 0
end = -1
for i in range(len(st)//2):
    if st[start]!=st[end]:
        print (False)
    start+=1
    end-=1
print (True)

# While Loop
st = ""
for ch in s:
    if ch.isalnum():
        st+=(ch.lower())
start = 0
end = len(st)-1
while (start<end):
    if st[start]!=st[end]:
        print(False)
    start+=1
    end-=1
print (True)
