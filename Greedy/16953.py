import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0
flag = 0

while True:
    if A == B:
        break
    elif A>B:
        flag = 1
        break

    if B % 2 == 0: # 짝수일 때
        B /= 2
        cnt += 1
    elif B % 10 == 1: # 1의 자리 숫자가 1일 때
        B = B//10
        cnt += 1
    else:
        flag = 1
        break

if flag == 0:
    print(cnt+1)
else:
    print(-1)