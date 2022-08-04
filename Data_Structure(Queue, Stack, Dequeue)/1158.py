import sys
from collections import deque
# list를 쓰면 시간초과, 시간복잡도가 작은 deque를 쓰기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([i+1 for i in range(n)])
res = []
for i in range(n):
    for j in range(k):
        if j == k-1:
            res.append(queue.popleft())
            break
        a = queue.popleft()
        queue.append(a)

res_str = str(res)[1:-1]
print(f"<{res_str}>")