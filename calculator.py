# This function adds two numbers
def add(x,y):
    return x+y
#This function subtracts two  numbers
def subtract(x,y):
    return x-y
#This function multiplies two  numbers
def multiply(x,y):
    return x*y
#This function multiplies two numbers
def divide(x,y):
    return x/y
#to select the operations 
print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    #take input from the user
    choice=input("enter choice(1/2/3/4):")

    #check if choice is one of the below options
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("Enter the first number :"))
            num2=float(input("Enter the second number :"))
        except ValueError:
            print("Invalid input.Please enter a number.")
            continue
        if choice =='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=",divide(num1,num2))

            # check if user wants to continue with anaother caolculation

            #break the while loop if answer is no
        next_calculation=input("lets do next calculation ?(yes/no):")
        if next_calculation=="no":
            break
    else:
        print("Invalid input")                




