import csv
import json

with open('7_2.json', 'r') as json_file:
    students_data = json.load(json_file)

with open('students_attendance.csv', 'r') as csv_file:
    attendance_data = list(csv.reader(csv_file))[1:]
    for student, attendance in attendance_data:
        attendance = attendance[1:-1].strip().split(',')
        students_data[student] = list(map(int, attendance))
    with open('7_2.json', 'w') as json_file:
        json.dump(students_data, fp=json_file, ensure_ascii=False)


