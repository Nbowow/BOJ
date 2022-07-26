import sys
input = sys.stdin.readline

R, C = map(int, input().split())
data = []
for i in range(R):
    data.append(input().rstrip())

row_len = len(data)
col_len = len(data[0])

alpa = [False] * 26
alpa[ord(data[0][0])-65] = True
max_count = 0

def recur(row, col, last):
    global max_count
    if row>0:
        # if data[row-1][col] not in alpa: 
        # alpa에 새로운 문자 넣어주는 식으로 알고리즘 짜면 시간초과남...
        if alpa[ord(data[row-1][col])-65] == False: # 상
            alpa[ord(data[row-1][col])-65] = True
            recur(row-1, col, ord(data[row-1][col])-65)
    if row<row_len-1:
        if alpa[ord(data[row+1][col])-65] == False: # 하
            alpa[ord(data[row+1][col])-65] = True
            recur(row+1, col, ord(data[row+1][col])-65)
    if col>0:
        if alpa[ord(data[row][col-1])-65] == False: # 좌
            alpa[ord(data[row][col-1])-65] = True
            recur(row, col-1, ord(data[row][col-1])-65)
    if col<col_len-1:
        if alpa[ord(data[row][col+1])-65] == False: # 우
            alpa[ord(data[row][col+1])-65] = True
            recur(row, col+1, ord(data[row][col+1])-65)

    count = 0
    for i in range(len(alpa)):
        if alpa[i] == True: count += 1
    max_count = max(max_count, count)
    alpa[last] = False
    return

recur(0, 0, 0)
print(max_count)