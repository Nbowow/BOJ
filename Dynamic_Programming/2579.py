# -*- coding: utf-8 -*- 
import sys
input = sys.stdin.readline

N = int(input())
stairs = []
ans = [[0 for _ in range(2)] for _ in range(305)]

for _ in range(N):
    stairs.append(int(input()))
if(N == 1):
    print(stairs[0])
elif(N == 2):
    print(stairs[0]+stairs[1])
else:
    ans[0][0] = stairs[0]
    ans[1][0] = stairs[0] + stairs[1]
    ans[1][1] = stairs[0]

    for i in range(2, N):
        #i번째 계단 밟을 때
        ans[i][0] = stairs[i] + max(ans[i-2][0], ans[i-2][1]+stairs[i-1])
        #i번째 계단 안 밟을 때
        ans[i][1] = ans[i-1][0]

    print(ans[N-1][0])