def add(a, b):
    addition = a + b
    return addition


def subtract(a, b):
    sub = a - b
    return sub


def multiply(a, b):
    mutli = a * b
    return mutli


def divide(a, b):
    dividee = a / b
    return dividee


print("Select an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Put your first number into the calculator = "))
num2 = int(input("Put your second number into the calculator = "))

if choice == '1':
    print(num1, " + ", num2, " = ", add(num1, num2))
elif choice == '2':
    print(num1, " - ", num2, " = ", subtract(num1, num2))
elif choice == '3':
    print(num1, " * ", num2, " = ", multiply(num1, num2))
elif choice == '4':
    print(num1, " / ", num2, " = ", divide(num1, num2))
else:
    print("Invalid Syntax")
