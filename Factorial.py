def factorial(n):
    fact = 1
    print(f"{n}! = ", end="")
    for i in range(n, 0, -1):
        fact *= i
        if i > 1:
            print(f"{i} × ", end="")
        else:
            print(f"{i} = ", end="")
    print(fact)

# Get input from the user
num = int(input("Enter a number: "))
factorial(num)