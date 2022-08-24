# 최대 힙(S2)
import sys, heapq
input = sys.stdin.readline

N = int(input())

heap = []
for i in range(N):
    a = int(input())
    if a == 0:
        if len(heap) != 0: 
            print(heapq.heappop(heap)[1])
        else: print("0")
    else: heapq.heappush(heap, (-a, a))

