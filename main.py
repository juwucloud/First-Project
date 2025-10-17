def addition (a, b):
        return a + b

addition_result = addition(5,7)
print(f"The addition result is : {addition_result}")

def multiplication(a, b):
        return a * b

multiplication_result = multiplication(5,7)
print(f"the multiplication result is: {multiplication_result}")

def substraction(a, b):
        return a - b

substraction_result = substraction(7,5)
print(f"The substraction result is: {substraction_result}")

def devision(a, b):
        if b == 0:
                print("You can not devide by 0")
        else:
                return a / b 
        
devision_result = devision(8,4)
print(f"The devision result is: {devision_result}")