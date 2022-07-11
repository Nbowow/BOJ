n = int(input())

data = []
for i in range(n-1):
    a, b = map(int, input().split())
    data.append([a,b])

k = int(input())
#print(data)
#print(f"n : {n}, k : {k}")
ans = [0] * n
check = [0] * n
_ans = 1e9
if n == 1: 
    ans[n-1] = 0
    _ans = 0
elif n == 2:
    ans[n-1] = data[0][0] # 작은점프
    _ans = ans[n-1]
elif n == 3:
    ans[n-1] = min(data[0][0]+data[1][0], data[0][1])
    _ans = ans[n-1]
else:
    ans[0] = 0
    ans[1] = data[0][0]
    ans[2] = min(data[0][0]+data[1][0], data[0][1])
    for i in range(3, n):
        ans[i] = min(ans[i-2]+data[i-2][1], ans[i-1]+data[i-1][0]) # 우선 작점, 큰점만 고려
    _ans = ans[-1]
    for i in range(n): check[i] = ans[i]
    
    # 각 돌에서 매큰점했을때 고려하여 최솟값구함
    for i in range(3, n):
        check[i] = check[i-3] + k
        if i<n-1: 
            check[i+1] = check[i] + data[i][0]
            for j in range(i+2, n):
                #check[j] = min(check[j-2]+data[j-2][0]+data[j-1][0], check[j-2]+data[j-2][1])
                #위와 같이 작성할 경우, 밑 문장과 처음 for문 돌때 (j == i+2)일때는 같은 문장이지만, 그 이후에는 달라지게 된다.
                #한칸 점프할 경우와 두칸 점프할 경우를 비교하는 것이 아니라
                #한칸 점프를 두번 할 경우와 두칸 점프할 경우를 비교하게 되므로 오류가 발생한다.(한칸 점프 + 두칸 점프 + 한칸 점프를 계산 못함.)
                check[j] = min(check[j-1]+data[j-1][0], check[j-2]+data[j-2][1])
        _ans = min(_ans, check[n-1])
        #print(check)
        for i in range(n): check[i] = ans[i]
            
print(_ans)