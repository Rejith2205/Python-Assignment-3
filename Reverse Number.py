# #############everse the input number#################
num=int(input("Enter the number to be reversed:"))
reversed_num = 0
while num != 0:
    rev_digit = num % 10                            # to store the remainder of the number dived by 10
    reversed_num = reversed_num * 10 + rev_digit    #0*10+3=3
    num //= 10                                      #num is then divided by 10 526
print("Reversed Number: " + str(reversed_num))