# 스택
import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    a = input().rstrip()
    if a[0] == 'p':
        if a[1] == 'u': data.append(a[5:])
        else:
            if len(data) == 0: print(-1)
            else: print(data.pop())
    elif a[0] == 's':
        print(len(data))
    elif a[0] == 'e':
        if len(data) == 0: print(1)
        else: print(0)
    else: 
        if len(data) == 0: print(-1)
        else: print(data[-1])