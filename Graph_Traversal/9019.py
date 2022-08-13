# DSLR
import sys
from collections import deque
input = sys.stdin.readline

def Double(num):
    if num*2 > 9999:
        return (num*2)%10000
    else: return num*2

def Subtract(num):
    if num != 0: return num-1
    else: return 9999

def Left(num):
    return (num%1000)*10+num//1000

def Right(num):
    return (num%10)*1000+num//10

def bfs(C1, C2):
    queue = deque()
    visited = [False] * 10000
    queue.append((C1,""))

    while queue:
        num, path = queue.popleft()
        if num == C2: 
            print(path)
            break

        a = Double(num)
        if visited[a] == False:
            visited[a] = True
            queue.append((a, path+"D"))
        
        b = Subtract(num)
        if visited[b] == False:
            visited[b] = True
            queue.append((b, path+"S"))

        c = Left(num)
        if visited[c] == False:
            visited[c] = True
            queue.append((c, path+"L"))
        
        d = Right(num)
        if visited[d] == False:
            visited[d] = True
            queue.append((d, path+"R"))

for _ in range(int(input())):
    A, B = map(int, input().split(" "))
    bfs(A, B)
