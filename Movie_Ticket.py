# Movie ticket discount calculation based on age
age=int(input("Enter Your Age :"))
if  age<=0:
    print("Invalid age")
elif age<=15 :
    print("you are eligible for half price,£3.00")
elif age<=59:
    print("There is no discount for your age group,price is £6.00")
elif age>=60 :
    print("There is a discount for your age group , price £2.00")
else :
    print("Invalid age")