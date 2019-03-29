# This file will contain a class, CollegeCourse.  This class contains attributes for a course:
# course id (for example, “CSC401”) is the unique identifier for each course, credit hours (for example, 3),
# and a letter grade (for example, ‘A’).  Include get and set methods for each attribute.

# CollegeCourse Class
# Attributes:
# 1.	courseId: this is a string.  The value for this attribute will be passed as a parameter in the class constructor
# 2.	creditHr: This is an integer.  The value for this attribute will be passed as a parameter in the class constructor
# 3.	grade: This is a string.  The value for this attribute will be passed as a parameter in the class constructor
# Methods:
# 1.	Create get methods for each attribute.  The get method will return the value of an attribute.  The get method
# for each attribute takes no parameters
# 2.	Create a set method for each attribute.  The set method takes one parameter.  This parameter represents the new
# value for the attribute. Set method does not return a value


class CollegeCourse:

    def __init__(self, courseId, creditHr, grade):
        self.courseId = courseId
        self.creditHr = creditHr
        self.grade = grade

    def setcourseId(self, cid):
        self.courseId = cid

    def getcourseId(self):
        return self.courseId

    def setcreditHr(self, credhr):
        self.creditHr = credhr

    def getcreditHr(self):
        return self.creditHr

    def setgrade(self, grd):
        self.grade = grd

    def getgrade(self):
        return self.grade


# c = CollegeCourse("CSC401", 3, 'A')
#
# print(c)
# print(c.getcourseId())
# print(c.getcreditHr())
# print(c.getgrade())
