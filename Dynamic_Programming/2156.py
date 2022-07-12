n = int(input())

data = []
for i in range(n):
    k = int(input())
    data.append(k)

print(data)

a = [0] * n
if n == 0:
    a[0] = data[0]
elif n == 1:
    a[0] = data[0]
    a[1] = data[0]+data[1]
elif n == 2:
    a[0] = data[0]
    a[1] = data[0]+data[1]
    a[2] = max(a[1], data[0]+data[2], data[1]+data[2])
else:
    a[0] = data[0]
    a[1] = data[0]+data[1]
    a[2] = max(a[1], data[0]+data[2], data[1]+data[2])
    for i in range(3,n):
        a[i] = max(a[i-1], a[i-2] + data[i], a[i-3] + data[i-1] + data[i])
        # 잘 이해가 안되네..

print(a[n-1])