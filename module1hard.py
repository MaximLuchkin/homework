grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
students_grades = {}
for i, students in enumerate(students_sorted):
        students_grades_list = grades[i]
        average_grade = sum(students_grades_list) / len(students_grades_list)
        students_grades[students] = average_grade
print(students_grades)
