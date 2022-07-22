# M<=13 : 백트래킹 가능
import sys
input = sys.stdin.readline

N, M = map(int ,input().split())

data = []
for i in range(N):
    a = list(map(int, input().split()))
    data.append(a)

min_totaldis = 1e9
check = []
for i in range(N):
    check_col = []
    for j in range(N):
        check_col.append(0)
    check.append(check_col)

for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            check[i][j] = 1

def cal_distance(row, col):
    mindis = 1e9
    for i in range(N):
        for j in range(N):
            if check[i][j] == 2:
                mindis = min(mindis, abs(i-row)+abs(j-col))
    return mindis

def recur(num, row, col):
    global count, min_totaldis
    if num == M: # 치킨집 M개 골랐을 때, 치킨 거리 계산
        totaldis = 0
        for i in range(N):
            for j in range(N):
                if check[i][j] == 1:
                    totaldis += cal_distance(i,j)
        min_totaldis = min(min_totaldis, totaldis)
        check[row][col] = 0 # 고려했던 치킨집 제외(pop)
        return
    for i in range(row, N):
        for j in range(N):
            if i == row: j == col
                # 중요한부분 for문 범위를 (col, N)으로 해버리면
                # i값이 증가해도 열 검사를 (col, N)범위만 검사하기 때문에 오류가 발생한다.
            if check[i][j] == 2: 
                continue
            if data[i][j] == 2:
                check[i][j] = 2
                recur(num+1, i, j)
                check[i][j] = 0 # recur문에서 i, j에 치킨집이 있을 때 모든 경우 검사완료
        
recur(0, 0, 0)
print(min_totaldis)
