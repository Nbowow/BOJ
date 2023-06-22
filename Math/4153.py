import sys
input = sys.stdin.readline

while(1):
    data = [-1 for i in range(3)]
    data[0], data[1], data[2] = map(int, input().split())
    if(data[0] == 0):
        break
    data.sort()
    if(data[0]**2 + data[1]**2 == data[2]**2):
        print("right")
    else:
        print("wrong")