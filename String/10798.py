import sys

input = sys.stdin.readline

data = []
data_len = []
result = ''

for i in range(5):
    data.append(list(map(str, input().rstrip())))
for i in range(5):
    data_len.append(len(data[i]))

data_len.sort()

for i in range(data_len[-1]):
    for j in range(5):
        if len(data[j]) != 0:
            result += data[j][0]
            data[j].remove(data[j][0])
print(result)