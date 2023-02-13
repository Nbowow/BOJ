# 쇠막대기
import sys
input = sys.stdin.readline

data = list(map(str, input().rstrip()))
st = []
pipe = 0
lazer = 0

for i in range(len(data)):
    if data[i] == '(':
        st.append(data[i])
        pipe += 1
    else: # ')' 일경우
        if data[i-1] == '(': # '()' -> lazer
            st.pop()
            pipe -= 1
            lazer += 1
            pipe += len(st)
        else: # ')' -> pipe
            st.pop()
    
print(pipe)

