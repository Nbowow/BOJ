import sys
input = sys.stdin.readline

N = int(input())

house = [[0 for _ in range(3)] for _ in range(1005)]
paint = [[0 for _ in range(3)] for _ in range(1005)]

for i in range(N):
    house[i][0], house[i][1], house[i][2] = map(int, input().split())

paint[0][0], paint[0][1], paint[0][2] = house[0][0], house[0][1], house[0][2]

for i in range(1, N):
    #i번째 집에 빨간색을 칠할 경우
    paint[i][0] = min(paint[i-1][1], paint[i-1][2]) + house[i][0]

    #i번째 집에 초록색을 칠할 경우
    paint[i][1] = min(paint[i-1][0], paint[i-1][2]) + house[i][1]

    #i번째 집에 파란색을 칠할 경우
    paint[i][2] = min(paint[i-1][0], paint[i-1][1]) + house[i][2]

print(min(paint[N-1][0], paint[N-1][1], paint[N-1][2]))
