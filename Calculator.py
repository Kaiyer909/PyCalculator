#Funtion: adds two numbers together
def add(x, y):
    return x + y

#Function: subtracts two numbers
def subtract(x, y):
    return x - y

#Function: multiplies two numbers together
def multiply(x, y):
    return x * y 

#Funtion: divides two numbers
def divide(x, y):
    return x / y 

print("Select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#takes input from user
while True:
    choice = input("Enter a choice (1,2,3,4): ")

#Checks if choice is within the four options
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))

    # checks if user wants to perform another calculation 
    # or break loop

    next_calculation = input ("Would you like to perform another calculation? Yes/No: ")
    if next_calculation == "no":
        break

    else:
        print("Invalid input") 


