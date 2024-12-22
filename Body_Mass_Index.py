# BMI Calculation
weight=float(input("Enter your weight in Kg: "))
Height=float(input("Enter your Height in Meter: "))
BMI=weight/(Height*Height)
print("Body Mass Index :", {BMI})
if BMI<=0 :
    print("invalid BMI")
elif BMI<18.5 :
    print("You are under weight, you need more nutritious food to maintain the Normal BMI")
elif BMI<24.9 :
    print ("you have an Ideal BMI,Maintain the current lifestyle to keep it Ideal")
elif BMI<29.9:
    print("you are over weight,Need regulare exercise and good eating habits")
elif BMI >=30:
    print("You are Obese,you need to have rigorous excercise and well contolled eating habits")
else    :
    print( "Invalid BMI")