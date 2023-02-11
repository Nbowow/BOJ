# AC
import sys
from collections import deque
input = sys.stdin.readline

case = int(input())
ans = []

for i in range(case):
    fx = input().rstrip()
    n = int(input())
    x = input().rstrip()
    x = x[1:-1]
    if len(x) != 0:
        x = list(map(int, x.strip().split(",")))


    xd = deque(x)

    count = 0
    tag = 0
    for j in range(len(fx)):
        if fx[j] == 'R':
            count += 1
           
        elif fx[j] == 'D':
            if len(xd) == 0:
                ans.append('error')
                tag = 1
                break
            if count%2 == 0: # 짝수번만큼 뒤집었으면 왼쪽수 제거
                xd.popleft()
            else: #홀수번만큼 뒤집었으면 오른쪽수 제거
                xd.pop()

    if count%2 != 0: #홀수번만큼 뒤집었으면 최종적으로 뒤집어진상태
        xd.reverse()

    if tag != 1:
        ans.append(list(xd))

for i in range(len(ans)):
    if ans[i] != 'error':
        print('[' + ','.join(map(str, ans[i])) + ']') #수 사이에 공백이 안생기게 하는방법
    else:
        print(ans[i])