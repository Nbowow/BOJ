import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []

def recur(num):
    if len(data) == m:
        for j in range(len(data)-1):
            if data[j] > data[j+1]: return
        print(' '.join(map(str, data)))
        return
    for i in range(1, n+1):
        data.append(i)
        recur(i+1)
        data.pop()

recur(1)
