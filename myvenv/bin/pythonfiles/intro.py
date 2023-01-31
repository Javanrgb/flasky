courses = ['History', 'Math', 'Art', 'Physics', 'CompSci']
courses_2 = ['Biology', 'Chem']
course_3 = 'Psychology'
nums = [1, 2, 5, 6, 4, 3, 2]
sorted_courses = sorted(courses)
print(sorted_courses)
courses.insert(5, course_3)
print(courses)
courses.extend(courses_2)
print(courses)
##mid_course = len((courses/2)+1)
"""courses.pop()
print(courses)
courses.remove('Physics')

print(courses)
print(sorted(nums))
print(sum(nums))
print(nums.index(5))
"""

"""for index,item in enumerate(courses,start=1):
    print(index,item)"""
course_str = '-'.join(courses)
course_split = course_str.split('-')
print(course_str)
print(course_split)