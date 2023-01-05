# 랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lan = []
for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

while start<=end:
    sum_ = 0
    mid = (start + end)//2
    for i in range(len(lan)):
        sum_ += lan[i]//mid
    
    if sum_ >= n:
        start  = mid + 1
    elif sum_ < n:
        end = mid - 1

print(end)
