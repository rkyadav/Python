import sys

sys.path.append("C:/Users/rkyad/Documents/csc-401")

import student
import collegecourse
import studentDatabase


studentdata = studentDatabase.StudentDatabase()
status = True

while status == True:

    print("")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Display grades for a student")
    print("4. Display grades for all students")
    print("5. Exit")
    choice = int(input("Please make a selection from the menu above: "))

    if choice == 1:
        sFirst = input("What is students first name: ")
        sLast = input("What is students last name: ")
        courseId = input("What is the course id: ")
        courseCredit = input("How many credit hours is it worth: ")
        courseGrade = input("What was the grade achieved: ")

        studentInfo = student.Student(sFirst, sLast)
        course = collegecourse.CollegeCourse(courseId, courseCredit, courseGrade)
        studentInfo.addcourse(course)
        studentdata.addstudent(studentInfo)
    elif choice == 2:
        try:
            sId = int(input("What is the student id of the student you wish to remove: "))
            studentdata.removestudent(sId)
        except KeyError:
            print("ID not found.")
    elif choice == 3:
        try:
            sId = int(input("Which student grades do you wish to see: "))
            studentdata.liststudent(sId)
        except ValueError:
            print("Please enter a valid student id.")
    elif choice == 4:
        studentdata.liststudents()
    elif choice == 5:
        status = False
    else:
        print("Please make a selection from the above menu: ")


