
# Define Functions
#Addition - Function
def addition (a, b):
        return a + b

#Substraction - Function
def substraction(a, b):
        return a - b

#Multiplication - Function        
def multiplication(a, b):
        return a * b

#Division - Function
def division(a, b):
        if b == 0:
                print("You can not devide by 0")
        else:
                return a / b 

#Start of the Calculator
print("Welcome to the Calculator Application")
print("You can add, substract, multipy and divide two numbers!")
operatorChoice = input("What do you want to do? Type:\n+ for Addition\n- for Substraction\n* for Multiplication\n/ for Division\n\n")

if operatorChoice == "+" or operatorChoice == "-" or operatorChoice == "*" or operatorChoice == "/":
        print(f"Your Choice is: {operatorChoice}")
else:
        print("Invalid Input, try again!")



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

