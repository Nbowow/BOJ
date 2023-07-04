import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] < A[j]:
            dp[j] = max(dp[j], dp[i] + 1)
    print(dp)

print(max(dp))
