# 치즈
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

edge = 0
time = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            edge += 1

def bfs(edge):
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx <n and 0<= ny <m and visited[nx][ny] ==0:
                visited[nx][ny] = 1
                if board[nx][ny] == 1:
                    board[nx][ny] = 2 # 녹을 치즈조각 2로 변경
                    edge -= 1
                else: queue.append([nx,ny])   
    return edge

def afteronehour():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                board[i][j] = 0
                cnt += 1
    return cnt

queue = deque()
while True:
    visited = [[0]*m for _ in range(n)]
    queue.append([0,0])
    edge = bfs(edge)
    cnt = afteronehour() # cnt변수에 마지막으로 녹은 치즈조각 수량 저장
    time += 1

    if edge == 0: break
    
print(time)
print(cnt)


