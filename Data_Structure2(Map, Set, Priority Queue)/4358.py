# 생태학(S2)
import sys
input = sys.stdin.readline

data = []
cnt = 0
while True:
    word = input().rstrip()
    if not word: break # 공백입력되면 break
    data.append(word)
    cnt +=1

data.sort()
datalen = len(data)
dic = {}
for i in range(len(data)):
    if data[i] in dic: dic[data[i]] += 1
    else: dic[data[i]] = 1

for key in dic:
    print("%s %.4f" %(key, dic[key]/cnt*100))