def calcAge(year, birth):
    customer_age = year - birth
    return customer_age

def calcPremium(age):
    decades = age//10
    premium = (decades + 15) * 20
    return premium

for x in range(5):

    current_year = int(input("What is the current year: "))

    birth_year = int(input("What year were you born: "))

    age = calcAge(current_year, birth_year)
    policy = calcPremium(age)

    if age < 18:
        print("Sorry, you are not old enough to purchase life insurance.")
    else:
        print("The annual policy premium is $",str(policy),".",sep="")

print("Thanks for using our services.")
