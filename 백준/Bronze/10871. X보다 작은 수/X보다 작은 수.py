N, X = map(int, input().split())
num = list(map(int, input().split()))
for i in range(N):
    if num[i] < X:
        print(num[i], end=" ")