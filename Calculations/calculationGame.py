import random

randomNum = random.randint(1, 100)
    
print(randomNum)


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


print("The random number is " + str(randomNum) + ". Calculate the number!")  #hello there.

print("How are you going to solve this question?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice(1/2/3/å4):")

num1 = int(input("Put your first value here: "))
num2 = int(input("Put your second value here: "))

if choice == '1':
    sum = add(num1, num2)
elif choice == '2':
    sum = subtract(num1, num2)
elif choice == '3':
    sum = multiply(num1, num2)
elif choice == '4':
    sum = divide(num1, num2)
else:
    print("Invalid Syntax")

if sum != randomNum:
    print("You haven't calculated the correct number, try again!")
elif sum == randomNum:
    print("Well done! The sum of " + str(num1) + " and " + str(num2) + " is equal to " + str(randomNum))


print(num1)
print(num2)
