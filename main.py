
from operation import *
from write import *
from read import *

while True:
    #call to Action
    print("Welcome to Ghimire Electronic")
    print()
    print("Start your transaction!")
    print()
    print("1)  Buy\n2)  Sell\n3)  Exit\n")
    try:
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            #Buy from Manufacturers
            validate_form("buy")

        elif choice == 2:
            validate_form("sell")

        elif choice == 3:
            #Exit the program
            print("Thank You, For your valueable time")
            break
        else:
            #Validate Choice
            print("Please enter the valid number")
    except:
        print("Please enter a number")
