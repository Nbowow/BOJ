# 전쟁 - 전투
import sys
input = sys.stdin.readline

def Wcheck(row, col, color):
    global count
    for i in range(4):
        rx = row + dx[i]
        ry = col + dy[i]
        if 0 <= rx <= M-1 and 0 <= ry <= N-1 and field[rx][ry] == color and visited[rx][ry] == 0:
            visited[rx][ry] = 1
            count += 1
            Wcheck(rx, ry, color)
    return count

def dfs(color):
    global count
    for i in range(M):
        for j in range(N):
            count = 1
            if field[i][j] == color and visited[i][j] == 0:
                visited[i][j] = 1
                ans.append(Wcheck(i, j, color))

    return

# M이 행 N이 열
N, M = map(int, input().split())

field = []
ans = []
for _ in range(M):
    field.append(input().rstrip())

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0]*N for _ in range(M)]
dfs('W')
white = 0
for i in ans:
    white += i*i
print(white, end = ' ')

ans.clear()
visited = [[0]*N for _ in range(M)]
dfs('B')
black = 0
for i in ans:
    black += i*i
print(black)