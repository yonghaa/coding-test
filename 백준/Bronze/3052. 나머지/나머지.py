n = list()
for i in range(10):
    a = int(input())
    n.append(a % 42)

n = set(n)
print(len(n))