n, k = map(int, input().split())
sum = 0

data = list(map(int, input().split()))
#print(data)

subtract = []
for i in range(n):
    if i==n-1: break
    subtract.append(data[i+1]-data[i])
#print(subtract)

subtract.sort(reverse=False)
#print(subtract)

for i in range(n-k):
    sum += subtract[i]

print(sum)