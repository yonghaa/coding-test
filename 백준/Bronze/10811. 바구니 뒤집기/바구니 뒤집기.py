N, M = map(int, input().split())
basket = [n for n in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp
    
for i in range(N):
    print(basket[i], end=" ")