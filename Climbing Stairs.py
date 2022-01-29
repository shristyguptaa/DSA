# Climbing Stairs
n = 2
a=0
b=1
for i in range(0,n):
    next=a+b
    a=b
    b=next
print(next)
