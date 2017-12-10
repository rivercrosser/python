courses = ['History', 'Maths', 'Science', 'ComputerSc']
print(len(courses))
print(courses[0])
print(courses[-1])
# slicing
print(courses[:2])
print(courses[1:3])
# adding items to the list
courses.append('Art')
print(courses)
courses.insert(0, 'Political Science')
print(courses)
# list within a list
new_list = ['Education', 'Drama']
courses.extend(new_list)
print(courses)
# removing values
courses.remove('Maths')
print(courses)
# poping removes from the end of the list and removes
popped = courses.pop()
print(courses)
print(popped)
# Sorting
print(sorted(courses))
print(courses)
print('Art' in courses)
for item in courses:
    print item

# to see the indexes
for course in enumerate(courses):
    print course

print (courses.index('Art'))

# joining the items
course_str = '-'.join(courses)
print course_str

newer_list = course_str.split('-')
print newer_list
