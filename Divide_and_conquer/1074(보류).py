# Z
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
data = []

def recur(row, col):
    data.append([row, col])
    data.append([row, col+1])
    data.append([row+1, col])
    data.append([row+1, col+1])


i = 1
for _ in range(N):
    recur(i, i)
    i *= 2
recur(0, 0)
print(data)