# 괄호의 값
import sys
input = sys.stdin.readline

round = input().rstrip()
st = []
cal = []
ans = 0
flag = 0
for i in range(len(round)):
    if round[i] == '(' or round[i] == '[':
        st.append(round[i])
    
    elif round[i] == ')':
        if i == 0: # ) 로 시작 예외 처리
            flag = 1
            break
        if len(st) == 0: # st 비었을 경우 예외 처리
                flag = 1
                break

        if round[i-1] == '(':
            if st.pop() != '(': # ( 가 나오지 않을 경우 오류
                flag = 1
                break
            if len(st) != 0:
                cal.append(2)
            else:
                ans += 2
        elif round[i-1] == ')' or round[i-1] == ']':
            if st.pop() != '(': # ( 가 나오지 않을 경우 오류
                flag = 1
                break
            if len(st) != 0:
                cal.append(cal.pop() * 2)
            else:
                val = 0
                for x in cal:
                    val += x
                cal.clear()
                val *= 2
                ans += val
        else:
            flag = 1
            break
    
    elif round[i] == ']':
        if i == 0: # ] 로 시작 예외 처리
            flag = 1
            break
        if len(st) == 0: # st 비었을 경우 예외 처리
                flag = 1
                break

        if round[i-1] == '[':
            if st.pop() != '[': # [ 가 나오지 않을 경우 오류
                flag = 1
                break
            if len(st) != 0:
                cal.append(3)
            else:
                ans += 3
        elif round[i-1] == ')' or round[i-1] == ']':
            if st.pop() != '[': # [ 가 나오지 않을 경우 오류
                flag = 1
                break
            if len(st) != 0:
                cal.append(cal.pop() * 3)
            else:
                val = 0
                for x in cal:
                    val += x
                cal.clear()
                val *= 3
                ans += val
        else:
            flag = 1
            break
    else:
        flag = 1
        break

    # print(cal, st, ans)
if flag == 1:
    print(0)
elif len(st) != 0: # st 안비어있으면 오류
    print(0)
else:
    print(ans)
        
