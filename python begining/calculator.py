def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Error: Invalid argument.')
while True:
    print("Select on of the operation avaible: \na. Add\nb. Subtract\nc. Multiply\nd. Divide")
    choice = input("Which function would you like to use: ")
    if choice in ('a', 'b', 'c', 'd'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 'a':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == 'b':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == 'c':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == 'd':
            print(num1, "÷", num2, "=", divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          print ("Thank you for using us!")
          break
    else:
        print("Invalid Input")