import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rs = [] # 결과값 저장
check = [False] * (n+1) # 방문여부 저장

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, n+1):
        if check[i] == False:
            check[i] = True
            rs.append(i)
            recur(num+1)
            rs.pop()
            check[i] = False

recur(0)
    
# pop안해줬을 경우
# 0 > rs = [1, 2, 3, 4]
# 1 > rs = [1, 2, 3]
# 2 > rs = [1, 2] 