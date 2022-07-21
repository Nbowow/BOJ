import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# a,n,t,i,c > 5개
word = []
for i in range(n): # rstrip() > 개행문자 지워주는 작업.
    word.append(input().rstrip())

alpa = ['a', 'n', 't', 'i', 'c']
max_count = 0

def recur(num, start):
    global max_count
    if num == k-5: # 임의로 뽑은 k-5개의 문자로 단어 검사
        count = 0
        for i in range(n):
            if len(word[i]) == 8: # 단어가 antatica 일 때(예외처리)
                count += 1
                continue
            for j in range(4, len(word[i])-4):
                if j == len(word[i])-5:
                    if word[i][j] in alpa: count += 1
                if word[i][j] not in alpa:break
        max_count = max(max_count, count) # 임의로 뽑은 k-5개의 문자로 만들 수 있는 단어의 최댓값 갱신
        return
    for i in range(start, 26): 
        # start가 있는 이유는 사전식으로 앞 문자부터 순차검색(중복검사x)
        # ex) b,d 검사한후 d,b를 검사안하기 위한 목적
        if chr(97+i) not in alpa:
            alpa.append(chr(97+i))
            recur(num+1, i)
            alpa.pop()


if k < 5: print(0)
elif k == 26: print(n)
else:
    recur(0, 0)
    print(max_count)
