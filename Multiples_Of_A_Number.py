############## Function to print multiples of a number
number=int(input("Enter the number to find the multiplier :"))
count=int(input("Enter the count, number to be multiplied:"))
counter=1
while counter <= count:
    result = counter *number
    print(f"{counter} x {number} = {result}")
    counter += 1