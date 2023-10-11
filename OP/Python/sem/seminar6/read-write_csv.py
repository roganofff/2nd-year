import csv

filename = 'numbers.csv'

# with open(filename, 'r') as numbers_file:
#     reader = csv.reader(numbers_file)

#     for line in reader:
#         for value in line:
#             print(type(value), value)
#         print()

# attendance = [
#     [15, 14, 15, 15, 12, 12, 12, 10, 10, 10, 10, 11, 22, 14, 14, 14, 13, 13, 14, 13, 13, 11, 11],
#     [12, 10, 15, 15, 10],
# ]
# with open('7_2_attendance.csv', 'a') as numbers_file:
#     writer = csv.writer(numbers_file)

#     # 1
#     # for month in attendance:
#     #     writer.writerow(month)
    
#     # 2
#     writer.writerows(attendance)

students_attendance = [
    {
        'name': 'Бахтинов Владислав',
        'attendance': [0, 0, 1, 1, 0]
    },
    {
        'name': 'Цверкунов Богдан',
        'attendance': [1, 0, 1, 1, 1]
    },
    {
        'name': 'Роганов Егор',
        'attendance': [1, 1, 1, 1, 1]
    },
]

with open('students_attendance.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, students_attendance[0].keys())
    writer.writeheader()
    for student in students_attendance:
        writer.writerow(student)