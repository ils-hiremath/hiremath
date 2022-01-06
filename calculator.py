def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def devide(x,y):
    return x/y

print("select an operation?")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice=input("Enter your Choice?(1/2/3/4)")
    
    if choice in ["1","2","3","4"]:
        num1=int(input("enter the first number:"))
        num2=int(input("enter the second number:"))

        if choice == "1":
            print(num1, "+", num2, "=",add(num1,num2))

        elif choice == "2":
            print(num1, "-", num2, "=",sub(num1,num2))
    
        elif choice == "3":
            print(num1, "*", num2, "=",multi(num1,num2))

        elif choice == "4":
            print(num1, "/", num2, "=",devide(num1,num2))

        next_calulation = input("Do you want to perform any operation again?(yes/no)")

        if next_calulation == "no":
            break

    else:
        print("Enter a Valid input")        

    



        
