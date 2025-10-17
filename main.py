# Define Functions
# Addition - Function
def addition (a, b):
        return a + b

# Substraction - Function
def substraction(a, b):
        return a - b

# Multiplication - Function        
def multiplication(a, b):
        return a * b

# Division - Function
def division(a, b):
        return a / b 

def calculator():
        # Start of the Calculator
        print("Welcome to the Calculator Application")
        print("You can add, substract, multipy and divide two numbers!\n")

        # User Input for Operator Choice /w validity check
        while True:
                operatorChoice = input("What do you want to do?\n+ for Addition\n- for Substraction\n* for Multiplication\n/ for Division\n\n")

                if operatorChoice == "+" or operatorChoice == "-" or operatorChoice == "*" or operatorChoice == "/":
                        print("")
                        print(f"Your Choice is: {operatorChoice}\n")
                        break
                else:
                        print("Invalid Input, try again!\n\n")

        # User Input for Number Choice
        print("Now it is time to choose your numbers. Decimals are allowed!\n")

        # checking if Input is valid (repeats the input query when not a number)
        while True:
                try:
                        InputNumberA = float(input("What is your first number? "))
                        print("")

                        while True: # Second loop to check if division by 0
                                InputNumberB = float(input("What is your second number? "))
                                if operatorChoice == "/" and InputNumberB == 0:
                                        print("You cannot divide by 0. Please enter another number!\n")
                                else:
                                        break
                        break

                except ValueError:
                        print("Invalid Input, try again!\n")


        print(f"Your first number is {InputNumberA} and your second number is {InputNumberB}\n")
        print("Calculating ... \n")


        # Calculting the Result
        if operatorChoice == "+":
                result = addition(InputNumberA, InputNumberB)
        elif operatorChoice == "-":
                result = substraction(InputNumberA, InputNumberB)
        elif operatorChoice == "*":
                result = multiplication(InputNumberA, InputNumberB)
        elif operatorChoice == "/":
                result = division(InputNumberA, InputNumberB)

        print(f"Your Result: {InputNumberA} {operatorChoice} {InputNumberB} = {result}\n")


# Program starts!
calculator()

while True:
        again = input ("Do you want to calculate again? (y/n)" ).lower()
        if again == "y":
                calculator()
        elif again == "n":
                print("\n/Thank you for using the calculator. See you next time!")
                break
        else:
                print("Invalid input, please type 'y' or 'n'.")




# Function testing Area
#-----------------------
# addition_result = addition(5,7)
# print(f"The addition result is : {addition_result}")
# multiplication_result = multiplication(5,7)
# print(f"the multiplication result is: {multiplication_result}")
# substraction_result = substraction(7,5)
# print(f"The substraction result is: {substraction_result}")
# division_result = division(8,4)
# print(f"The devision result is: {devision_result}")

