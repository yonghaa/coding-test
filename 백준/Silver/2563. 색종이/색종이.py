N = int(input())
array = [[0] * 100 for _ in range(100)]
for _ in range(N):
    y1, x1 = map(int, input().split())
    
    for i in range(x1, x1 + 10):
        for j in range(y1, y1 + 10):
            array[i][j] = 1

result = 0
for k in range(100):
    result += array[k].count(1)
print(result) 