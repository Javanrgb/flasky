student = {'name': 'Jane', 'Age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
student.update({'name': 'John', 'Age': 26, 'phone': '2319-29101'})
# del student['Age']
age = student.pop('Age')
print(student)
print(age)
print(student.items())

for key,value in student.items():
    print(key,value)
