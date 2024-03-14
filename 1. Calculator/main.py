#define the functions needed to the user which are add, sub, mul, div
#print options to the user
#ask for the values
#call the functions and return the value, also add a while loop to continue the program
def add(a,b):
    answer = a+b
    print(f"Answer of {a} + {b} = {answer}")

def sub(a,b):
    answer = a-b
    print(f"Answer of {a} - {b} = {answer}")

def mul(a,b):
    answer = a*b
    print(f"Answer of {a} x {b} = {answer}")

def div(a,b):
    answer = a/b
    print(f"Answer of {a} / {b} = {answer}")

print("Welcome to the Calculator!\n")
print("\n")
print("Choose one of the below options\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. QUIT")

    choice = input("Enter your choice\n")

    if choice == 'a' or choice == "A":
        print("Addition")
        a = int(input("Enter the first number\n"))
        b = int(input("Enter the second number\n"))
        add(a,b)

    elif choice == 'b' or choice == "B":
        print("Subtraction")
        a = int(input("Enter the first number\n"))
        b = int(input("Enter the second number\n"))
        sub(a,b)

    elif choice == 'c' or choice == "C":
        print("Multiplication")
        a = int(input("Enter the first number\n"))
        b = int(input("Enter the second number\n"))
        mul(a,b)

    elif choice == 'd' or choice == "D":
        print("Division")
        a = int(input("Enter the first number\n"))
        b = int(input("Enter the second number\n"))
        div(a,b)

    elif choice == 'e' or choice == "E":
        print("Program Terminated!")
        exit()
