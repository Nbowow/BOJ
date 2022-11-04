# 치킨치킨치킨
import sys
from itertools import combinations
input = sys.stdin.readline

# combination으로 구한 모든 숫자 조합에 대해 각 회원들의 만족도 최댓값을 구함
def cal(ite):
    ans = []
    for i in range(N):
        max_ = 0
        for j in combi[ite]:
            max_ = max(max_,chiken[i][j-1])
        ans.append(max_)
    
    return sum(ans)

N, M = map(int, input().split())
chiken = []
nums = []
for _ in range(N):
    chiken.append(list(map(int, input().split())))

for i in range(M):
    nums.append(i+1)
combi = list(combinations(nums, 3))

ans = 0
for i in range(len(combi)):
    ans = max(ans, cal(i))
print(ans)
