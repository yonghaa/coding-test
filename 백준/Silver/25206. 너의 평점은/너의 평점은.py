n = 20

grade_dict = {'A+':4.5,
              'A0':4.0,
             'B+':3.5,
             'B0':3.0,
             'C+':2.5,
             'C0':2.0,
             'D+':1.5,
             'D0':1.0,
              'F':0}
total = 0
result = 0
for _ in range(n):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade != 'P':
        total += credit
        result += credit * grade_dict[grade]
print('{:.6f}'.format(result / total))