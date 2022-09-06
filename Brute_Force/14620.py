# 꽃길
import sys
input = sys.stdin.readline

def cal():
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1: count += garden[i][j]
    return count

def check(row, col):
    for i in range(4):
        rx = row + dx[i]
        ry = col + dy[i]
        if visited[rx][ry] == 1: return False
    return True
    
def plant(row, col):
    for i in range(4):
        rx = row + dx[i]
        ry = col + dy[i]
        visited[rx][ry] = 1
    visited[row][col] = 1
    return

def unplant(row, col):
    for i in range(4):
        rx = row + dx[i]
        ry = col + dy[i]
        visited[rx][ry] = 0
    visited[row][col] = 0
    return

def dfs(idx):
    global min_cost
    if idx == 3:
        min_cost = min(min_cost, cal())
        return

    for i in range(1, N-1):
        for j in range(1, N-1):
            if visited[i][j] == 0:
                if check(i,j): 
                    plant(i,j)
                    dfs(idx+1)
                    unplant(i,j)

N = int(input())
garden = []
for i in range(N):
    data = list(map(int, input().split()))
    garden.append(data)

visited = [[0]*N for _ in range(N)]

#동 서 남 북
dx = [0 ,0 , 1, -1]
dy = [1, -1, 0, 0]

min_cost = 1e9
dfs(0)
print(min_cost)
