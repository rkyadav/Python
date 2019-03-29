# 1.	A function that reads the data from the file into a list and return the list.
# This function will take the name of the file as a parameter.

def readfile(text):
    infile = open(text, 'r')
    test = infile.readlines()
    return test

testdoc = input("Please enter a file name: ")
sample = readfile(testdoc)
print(sample)
print('=' * 40)


# 2.	A function that calculates and stores each employees data: name, total hours worked, overtime hours,
# overtime pay, regular pay, total pay.
#   The list containing the data from the file will be passed to this function as parameter.
# This function returns a list or dict containing all employees data.

def employeeData(sheet):
    flist = []

    for employee in sheet:
        tsheet = {}
        empsplit = employee.split(',')
        if (int(empsplit[1]) - 40) > 0:
            ohours = int(empsplit[1]) - 40
        else:
            ohours = 0
        opay = (float(empsplit[2]) * 1.5)
        ototal = round(opay * ohours, 2)
        rtotal = round(40 * float(empsplit[2]), 2)
        tsheet['name'] = empsplit[0]
        tsheet['total hours worked'] = int(empsplit[1])
        tsheet['overtime hours'] = ohours
        tsheet['overtime pay'] = ototal
        tsheet['regular pay'] = rtotal
        tsheet['total pay'] = rtotal + ototal
        flist.append(tsheet)
    return flist

temp = employeeData(sample)
print(temp)
print('=' * 40)

# 3.	A function that calculates and returns the average pay.
#   This function takes the list or dict containing all employees data.

def averagePay(pay):
    paySum = []
    for payment in pay:
        total = payment.get("total pay")
        paySum.append(total)


    averageSum = round(sum(paySum)/ len(paySum),2)
    return averageSum

payAverage = averagePay(temp)
print(payAverage)
print('=' * 40)

# 4.	A function that displays the names of all the employees whose pay is greater than
# or equal to the average weekly pay.
#  This function takes the list or dict containing all employees data and the average pay.
#  Your program must display the average pay

def greaterAverage(aver,employees):
    print('The average pay for employees is $' + str(aver) + '.')
    for emp in employees:
        if emp.get("total pay") >= aver:
            print(emp.get("name") + " makes more than or equal to the average pay, making " + str(emp.get('total pay')) + ".")

greaterAverage(payAverage,temp)
print('=' * 40)



# 5. A function to output each employee’s data properly formatted on screen.
#  This function takes the list or dict containing all employees data.
# name		total_hours	overtime_hours	regular_pay	overtime_pay	total_pay
# Jane Doe    	45		5		740		138.75		878.75
def display(employees):
    print("name		 total_hours  overtime_hours  regular_pay	overtime_pay	  total_pay")
    print('=' * 85)
    for emp in employees:
        formatString = "{:17} {:5} {:10} {:15} {:15} {:15}".format(emp.get('name'), emp.get('total hours worked'), emp.get('overtime hours'), emp.get('regular pay'), emp.get('overtime pay'), emp.get('total pay'))
        print(formatString)
display(temp)
