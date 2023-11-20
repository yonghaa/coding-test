n,m = map(int, input().split())

basket = [0]*n

for i in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        basket[x-1] = k
        
for x in range(n):
    print(basket[x], end= " ")