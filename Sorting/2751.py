import sys
input = sys.stdin.readline

N = int(input())

data = []
for i in range(N):
    data.append(int(input()))

data.sort()

for i in range(len(data)):
    print(data[i])