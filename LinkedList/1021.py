# 회전하는 큐
# 풀긴 풀었지만 맘에 들지 않는 풀이,,,
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
while len(data) != 0:
    a = data[0]-1
    b = (N+1)-data[0]
    if a>=b :
        tmp = b
        data.pop(0)
        for i in range(len(data)):
            data[i] += tmp
            data[i] -= 1 # 앞 번호 하나 pop됐으므로 -1
            if data[i] >= N:
                data[i] = data[i] - N
            elif data[i]<0:
                data[i] = N + data[i]

    else:
        tmp = a
        data.pop(0)
        for i in range(len(data)):
            data[i] -= tmp
            data[i] -= 1
            if data[i] >= N:
                data[i] = data[i] - N
            elif data[i]<0:
                data[i] = N + data[i]

    N -= 1

    ans += tmp

print(ans)