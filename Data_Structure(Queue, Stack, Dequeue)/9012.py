# 괄호
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = input()
    stack = []
    isprinting = False
    for j in range(len(a)):
        if a[j] == '(':
            stack.append(a[j])
        elif a[j] == ')':
            if len(stack) != 0: stack.pop()
            else: 
                print('NO')
                isprinting = True
                break
    if len(stack) == 0 and isprinting == False: print('YES')
    elif len(stack) !=0 and isprinting == False: print('NO')