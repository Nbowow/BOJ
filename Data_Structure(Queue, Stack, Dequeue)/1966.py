# 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline

case = int(input())
ans = []
for _ in range(case):
    N, M = map(int, input().split())
    letter = list(map(int, input().split()))

    M += 1
    count = 0
    while(letter):
        if letter[0] == max(letter):
            letter.pop(0)
            count += 1
            if M == 1:
                ans.append(count)
                break
            
            M -= 1
            if M == 0:
                M = len(letter)
        else:
            letter.append(letter.pop(0))
            M -= 1
            if M == 0:
                M = len(letter)

for i in range(len(ans)):
    print(ans[i])
        
        



