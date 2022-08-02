# 빙산
import sys, copy
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input().split())))

year = 0
# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def meltedice(row, col):
    for i in range(4):
        x = row + dx[i]
        y = col + dy[i]
        if ice[x][y] == 0:
            melt_ice[row][col] += 1  # 해당 칸 녹는 만큼 카운트

def dfs(row, col):
    for i in range(4):
        x = row + dx[i]
        y = col + dy[i]
        if ice[x][y] != 0 and visited[x][y] == False:
            visited[x][y] = True
            dfs(x,y)

while True:
    visited = [[False]*m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and visited[i][j] == False:
                count += 1
                if count>1: break # 빙산이 두개이상이라면 더이상 dfs돌 필요없음
                dfs(i, j)

    if count > 1: # 빙산이 두개이상 > 종료조건
        print(year)
        break

    melt_ice = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0:
                meltedice(i, j)
    for i in range(n):
        for j in range(m):
            ice[i][j] -= melt_ice[i][j]
            if ice[i][j] < 0: ice[i][j] = 0

    if sum(map(sum, ice[1:-1])) == 0: # 빙산이 다 녹을 때까지 한개라면
        print("0")
        break
    year += 1
