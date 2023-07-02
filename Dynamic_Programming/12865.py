import sys
input = sys.stdin.readline

N, K = map(int, input().split())

bag = []
dp = [[0 for _ in range(K+1)] for _ in range(N)]


for _ in range(N):
    w, v = map(int, input().split())
    bag.append([w, v])

for i in range(N):
    if i == 0:
        l = bag[i][0]
        while l<=K:
            dp[i][l] = bag[i][1]
            l+=1
        continue #
    for j in range(K):        
        if j+1>=bag[i][0] :
            dp[i][j+1] = max(bag[i][1] + dp[i-1][j+1-bag[i][0]], dp[i-1][j+1])
        else:
            dp[i][j+1] = dp[i-1][j+1]

print(dp[N-1][K])