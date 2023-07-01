import sys
input = sys.stdin.readline

N = int(input())
rest = 1000 - N
cnt = 0

if rest >= 500:
    cnt += 1
    rest -= 500

while(rest>=100):
    cnt += 1
    rest -= 100

while(rest>=50):
    cnt += 1
    rest -= 50

while(rest>=10):
    cnt+=1
    rest -= 10

while(rest>=5):
    cnt+=1
    rest -= 5

while(rest>=1):
    cnt+=1
    rest -= 1
print(cnt)
    
