import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    data.append(input().rstrip())

for i in range(n):
    alpa = [0] * 26
    max_count = 0
    for j in range(len(data[i])):
        if data[i][j] == " ": continue
        else:
            alpa[ord(data[i][j])-97] += 1
    for j in range(len(alpa)):
        if alpa[j] > max_count:
            max_count = alpa[j]
            max_alpa = chr(j+97)
    alpa.sort()
    if alpa[-1] == alpa[-2]:
        max_alpa = "?"
    print(max_alpa)
