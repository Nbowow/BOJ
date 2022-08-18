# 카드2
import sys
from collections import deque 
input = sys.stdin.readline

n = int(input())
data = deque()
for i in range(n):
    data.append(i+1)

while True:
    if len(data) == 1:
        print(data.pop())
        break
    data.popleft()
    data.append(data.popleft())