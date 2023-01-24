#키로거
import sys
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    case = input().rstrip()
    left = []
    right = []
    for i in range(len(case)):
        if case[i] == '<':
            if len(left) != 0:
                right.append(left.pop())
        elif case[i] == '>':
            if len(right) != 0:
                left.append(right.pop())
        elif case[i] == '-':
            if len(left) != 0:
                left.pop()
        else:
            left.append(case[i])
    print("".join(left) + "".join(reversed(right)))


            
