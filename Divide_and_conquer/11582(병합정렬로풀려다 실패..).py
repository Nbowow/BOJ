import sys
input = sys.stdin.readline

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    if len(left_sorted) == k and len(right_sorted) == k:
        for i in range(len(left_sorted)):
            print(left_sorted[i], end = ' ')
        for i in range(len(right_sorted)):
            print(right_sorted[i], end = ' ')
        sys.exit(0)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    i, j = 0
    result = []

    if i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    
    return result

N = int(input())
chi = list(map(int, input().split()))
k = int(input())

num = 0
while True:
    if 2**num == k:
        break
    num += 1


merge_sort(chi)