students = input('Total Number of Students')
studentsf = input ('Female Students')
studentsm = input ('Male Students')
students = int(students)
studentsf = int(studentsf)
studentsm = int(studentsm)
pstudentsf = studentsf/students
pstudentsm = studentsm/students
print ("Total Students")
print (students)
print ("Male Students")
print (format(pstudentsm, '.2%'))
print ("Female Students")
print (format(pstudentsf, '.2%'))