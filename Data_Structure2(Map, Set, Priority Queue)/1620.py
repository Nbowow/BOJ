# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = dict()

for i in range(1, n+1):
    data[i] = input().rstrip()

key = {v:k for k,v in data.items()} # key, value값 바꾸기

for i in range(m):
    a = input().rstrip()
    if a.isdigit(): print(data[int(a)])
    else: print(key[a])