# 문자열 집합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = []
for i in range(N):
    data.append(input().rstrip())
count = 0
dataset = set(data)

for i in range(M):
    a = input().rstrip()
    if a in dataset: count += 1

print(count)

# 리스트에서의 x in s 연산의 평균 시간 복잡도 : O(n)
# 셋에서의 x in s 연산의 평균 시간 복잡도: O(1)