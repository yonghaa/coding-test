students = [i for i in range(1,31)]

for _ in range(28):
    applied = int(input())
    students.remove(applied) #소거

print(min(students))
print(max(students))