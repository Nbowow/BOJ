import sys
input = sys.stdin.readline

dp = [0 for _ in range(100)]
dp[0] = 0
dp[1] = 1

for i in range(2, 91):
    dp[i] =  dp[i-2] + dp[i-1]


N = int(input())
print(dp[N])