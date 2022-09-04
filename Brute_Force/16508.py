# 전공책
import sys
input = sys.stdin.readline

def check():
    for i in range(26):
        if(cnt[i] > select_cnt[i]): return False
    return True

def dfs(idx, price):
    global res
    if(idx == N):
        if(check()): res = min(res, price)
        return
    
    for i in range(len(book[idx][1])):
        select_cnt[ord(book[idx][1][i]) - ord('A')] += 1
    dfs(idx + 1, price + book[idx][0])
    for i in range(len(book[idx][1])):
        select_cnt[ord(book[idx][1][i]) - ord('A')] -= 1
    dfs(idx + 1, price)


cnt = [0] * 26
select_cnt = [0] * 26
res = 1e9

T = input().rstrip()
for i in range(len(T)):
    cnt[ord(T[i]) - ord('A')] += 1
N = int(input())
book = []
for i in range(N):
    C, W = input().split()
    book.append([int(C), W])

dfs(0, 0)
if res == 1e9: print("-1")
else: print(res)
