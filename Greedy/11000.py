import heapq
import sys

n = int(input())
data = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    # a,b = map(int, input().split()) 으로하면 시간초과 남..
    data.append([a,b])
data.sort()

room = []
heapq.heappush(room, data[0][1])

for i in range(1,n):
    if room[0] > data[i][0]: # 수업 시작시간보다 수업끝나는 시간이 늦을 때
        heapq.heappush(room, data[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, data[i][1])
        
print(len(room))