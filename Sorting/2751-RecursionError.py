import sys
input = sys.stdin.readline

def quick_sort(array, start, end):
    if start>=end:
        return

    # 피벗 설정
    pivot = start
    left = start+1
    right = end

    while(left<right):
        # 피벗보다 큰 수 찾기
        while(left <= end and array[left] <= array[pivot]):
            left+=1
        # 피벗보다 작은 수 찾기
        while(right > start and array[right] >= array[pivot]):
            right-=1
        if(left>right): 
            # left, right 엇갈리면 피벗이랑 right랑 바꿈 -> 
            # 피벗보다 왼쪽 data는 피벗보다 작고, 오른쪽 data는 피벗보다 크다
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


N = int(input())

data = []
for _ in range(N):
    data.append(int(input()))

quick_sort(data, 0, len(data)-1)

for i in range(len(data)):
    print(data[i])