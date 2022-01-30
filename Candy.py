# Candy
scores = [1,0,2]
rewards = [1 for _ in scores]
for i in range(1,len(scores)):
    if scores[i]>scores[i-1]:
        rewards[i]=rewards[i-1]+1

for i in range(len(rewards)-2,-1,-1):
    if scores[i]>scores[i+1] and rewards[i]<=rewards[i+1]:
        rewards[i]=rewards[i+1]+1

print (sum(rewards))
