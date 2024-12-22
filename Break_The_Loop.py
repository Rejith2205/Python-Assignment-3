#### break the operation when input from the user is 'done'
while True:
    word= input("Enter what you want to print: ")
    print("The word you want to print is",word)
    if word.lower()== 'done':
        break
        print(word)
