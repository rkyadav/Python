def findPerfectAndImperfect(perfect,imperfect):
    for number in range(1, 1000):
        total = []
        for num in range(1,number):
            if number % num == 0:
                total.append(num)

        numTotal = sum(total)
        if numTotal == number:
            perfect.append(number)
        else:
            imperfect.append(number)

def displayValues(list):
    for variable in list:
        print(variable,end=' ')

list1 = []
list2 = []

findPerfectAndImperfect(list1,list2)
displayValues(list1)
print()
displayValues(list2)
