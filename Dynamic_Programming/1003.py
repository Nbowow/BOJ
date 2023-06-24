import sys
input = sys.stdin.readline
       

T = int(input())

for _ in range(T):
    N = int(input())

    data = [[0 for _ in range(2)] for _ in range(200)]
    
    data[0][0] = 1
    data[1][1] = 1

    for i in range(2, 100):
        for j in range(2):
            data[i][j] = data[i-1][j]+data[i-2][j]
   
    print(str(data[N][0])+' '+str(data[N][1]))

    