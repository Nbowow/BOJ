import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rs = []
check = [False] * (n+1)
res = []

def recur(num):
    if len(rs) == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(num, n+1): # num으로 받은 수보다 큰 수만 확인
        if check[i] == False:
            check[i] = True
            rs.append(i)
            recur(i+1) # i번째의 수보다 큰 수만 확인
            rs.pop()
            check[i] = False

recur(1)

