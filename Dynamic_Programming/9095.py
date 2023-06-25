import sys
input = sys.stdin.readline


T = int(input())

data = [0 for _ in range(15)]
data[0] = 0
data[1] = 1
data[2] = 2
data[3] = 4
for i in range(4, 11):
    data[i] = data[i-3] + data[i-2] + data[i-1]

for _ in range(T):
    print(data[int(input())])


