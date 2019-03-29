# This file will contain a class, StudentDatabase.  This class will contain a dictionary containing all student objects.

# studentDatabase Class
#        Attributes:
# 1. allStudents: This a is dictionary that contains key/value pairs.  Each key is a student id and the corresponding
# value is a student object.
#    Methods:
# 1. addStudent: This method takes a student object as parameter and adds the student to the allStudents dictionary.
# This method does not return a value
# 2. listStudents: This method takes no parameters.  It loops through the items in allStudents and displays details
# about each student.  This method does not return a value
# 3. listStudent: This method takes one parameter, a student id, and displays details about the student.  This method
# does not return a value

from student import *
from collegecourse import *

class StudentDatabase:
    def __init__(self, students={}):
       self.students = students

    def addstudent(self, student):
       key = student.getstudentid()
       slist = []
       slist.append(student.getfirstname())
       slist.append(student.getlastname())
       slist.append(student.getcourses())
       self.students[key] = slist

    def liststudents(self):
       for stu,ste in self.students.items():
           print("Student ID: ", stu)
           print("First Name: ", ste[0])
           print("Last Name: ", ste[1])
           print("Corse Id:", ste[2][0][0])
           print("Credit Hours: ", ste[2][0][1])
           print("Grade Earned: ", ste[2][0][2])

    def liststudent(self, student):
       stu = self.students.get(student)
       print("First Name: ", stu[0])
       print("Last Name: ", stu[1])
       print("Corse Id:", stu[2][0][0])
       print("Credit Hours: ", stu[2][0][1])
       print("Grade Earned: ", stu[2][0][2])

    def removestudent(self, student):
       del self.students[student]



# courselist = []
# print("course list = ", courselist)
# c = CollegeCourse("CSC401", 3, 'A')
# ctest = []
# ctest.append(c.getcourseId())
# ctest.append(c.getcreditHr())
# ctest.append(c.getgrade())
# courselist.append(ctest)
# print("course list = ", courselist)
# stu = Student("Salman", "Khan", courselist)
#
# print(stu.getstudentid())
# print(1)
# print(stu.getfirstname())
# print(2)
# print(stu.getlastname())
# print(3)
# stu.addcourse("test")
# print(4)
# stu.addcourse("test2")
# print(5)
# stu.deletecourse("test")
# print(6)
# print(7)
# d = StudentDatabase()
# print(8)
# d.addstudent(stu)
# print(9)
# d.liststudents()
# print(10)