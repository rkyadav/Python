gprofit = 20000
expenses = 35000
nprofit = gprofit - expenses

for x in range(20):
    print("Year " + str(x + 1))
    print("The " + str(x + 1) + " year's gross profit is $" + str(round(gprofit, 2)) + ".")
    print("The " + str(x + 1) + " year's expenses is $" + str(round(expenses, 2)) + ".")
    print("The " + str(x + 1) + " year's net profit is $" + str(round(nprofit, 2)) + ".")
    gprofit = gprofit * 1.10
    expenses = expenses * 1.04
    nprofit = gprofit - expenses
    print()
