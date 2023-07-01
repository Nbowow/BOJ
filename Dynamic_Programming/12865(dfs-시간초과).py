import sys
input = sys.stdin.readline

def dfs(row, w_total, v_total):
    global ans
    #print(f"ans : {ans}, row : {row}, w_total : {w_total}, v_total : {v_total}")
    if w_total > K:
        return
    ans = max(ans, v_total)

    for i in range(row+1, N):
        w_total += bag[i][0]
        v_total += bag[i][1]
        dfs(i, w_total, v_total)
        w_total -= bag[i][0]
        v_total -= bag[i][1]
        


N, K = map(int, input().split())

bag = []
ans = 0

for _ in range(N):
    w, v = map(int, input().split())
    bag.append([w, v])

for i in range(N):
    dfs(i, bag[i][0], bag[i][1])
    
print(ans)



# bag.sort(key = lambda x: (x[1], x[0]))

