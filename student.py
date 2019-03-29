# This file will contain the Student class.  Student class contains attributes and methods for a student:
# student id (5-digit random number) is the unique identifier for each student, student first name, student list name,
# and a list that will be used to hold objects of the CollegeCourse class.  Each object represent a course the student
# has earned a letter grade in.

# Student Class
# Attributes:
# 1. studentId: this is a 5-digit random integer.  This value will be generated in the class.  It cannot be passed as a
# parameter in the class constructor
# 2. firstName: This is a string.  The value of this attribute will be passed as a parameter in the class constructor
# 3. lastName: This is a string.  The value of this attribute will be passed as a parameter in in the parameter in the
# class constructor
# 4. courses: this is a list containing all courses for the a student
# Method:
# 1. Create get method for the studentId.  The get method returns the student id.
# 2. Create get and set methods for the student first and last names.  The get method for the student first name will
# return the student first name.  The get method for the student last name will return the student last name.  The set
# methods will be used to change the student first and last names.  Each set method take one parameter, which represent
# the new value for the attribute.
# 3. addCourse: This method will be used to add a new course to the list.  This method takes one parameter, which is a
# course object.  This method does not return a value
# 4. deleteCourse: This method removes a course (courses) from the list of courses for a student and displays the course
# information.  This method takes the course id as parameter.  This method does not return a value.
import random
import sys

sys.path.append("C:/Users/rkyad/Documents/csc-401")

from collegecourse import *


class Student:

    def __init__(self, fname, lname, courses=[]):
        num = range(10000, 99999)
        self.studentId = random.choice(num)
        self.fname = fname
        self.lname = lname
        self.courses = courses

    def getstudentid(self):
        return self.studentId

    def setfirstname(self, firstn):
        self.fname = firstn

    def getfirstname(self):
        return self.fname

    def setlastname(self, lastn):
        self.lname = lastn

    def getlastname(self):
        return self.lname

    def addcourse(self, course):
        if len(self.courses) <= 5:
            sl = []
            sl.append(course.getcourseId())
            sl.append(course.getcreditHr())
            sl.append(course.getgrade())
            self.courses.append(sl)
        else:
            print("Reached Maximum Number of Courses.")

    def deletecourse(self, course):
        self.courses.remove(course)
        print(self.courses)

    def getcourses(self):
        return self.courses

#c = CollegeCourse("CSC401", 3, 'A')
#
#
# print(c.getcourseId())
# print(c.getcreditHr())
# print(c.getgrade())

# courselist = []
# courselist.append(CollegeCourse("CSC401", 3, 'A'))
# stu = Student("Salman", "Khan", courselist)
#
# print(stu.getstudentid())
# print(stu.getfirstname())
# print(stu.getlastname())
# stu.addcourse("test")
# stu.addcourse("test2")
# print(stu.deletecourse("test"))
