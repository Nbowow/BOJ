# 바이러스
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

com = []
for i in range(m):
    a, b = map(int, input().split())
    com.append([a,b])

connect = []
check = []

def recur(num):
    check.append(num) # 검사한 컴퓨터라고 알려주는 역할
    for i in range(m):
        if com[i][0] == num:
            connect.append(com[i][1])
            if com[i][1] not in check: # 이미 검사한 컴퓨터이면 재귀안들어감
                recur(com[i][1])
        elif com[i][1] == num:
            connect.append(com[i][0])
            if com[i][0] not in check:
                recur(com[i][0])

recur(1)
set_connect = set(connect) # 중복제거
set_connect.remove(1)
print(len(set_connect))