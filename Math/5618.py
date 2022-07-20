import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

num.sort()

for i in range(1, num[-1]+1):
    if n == 2:
        if num[0] % i == 0 and num[1] % i == 0: print(i)
    else:
        if num[0] % i == 0 and num[1] % i == 0 and num[2] % i == 0: print(i)


