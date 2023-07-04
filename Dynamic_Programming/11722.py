import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

dp[0] = 1
for i in range(N):
    if dp[i] == 0:
        dp[i] = 1
    for j in range(i+1, N):
        if seq[j] < seq[i]:
            dp[j] = max(dp[j], dp[i] + 1)
    
print(max(dp))