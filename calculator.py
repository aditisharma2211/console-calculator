print(f"---CALCULATOR---")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))  # input by default gives you string. 

def addition():
    result = num1 + num2
    return result

def subtraction():
    result = num1 - num2
    return result 

def multiplication():
    result = num1 * num2
    return result

def division():
    result = num1 / num2
    return result

def modulas():
    result = num1 % num2
    return result 

while True:
    print("Enter 1 for + ")
    print("Enter 2 for - ")
    print("Enter 3 for * ")
    print("Enter 4 for / ")
    print("Enter 5 for % ")
    task = int(input("Enter the operator: "))

    match task:
       
       case 1:
        print(addition())
       case 2:
        print(subtraction())
       case 3:
        print(multiplication())
       case 4:
        print(division())
       case 5:
        print(modulas())
       case _:
        print("Invalid operator")


