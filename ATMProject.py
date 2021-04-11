import random
from datetime import datetime
now = datetime.now()
global balance
balance = 0
database = {}


print("*************Welcome to my ATM************* \n")


def init():
    

    choice = int(input("Do u have an account with us? 1(yes) 2(no) \n"))
    if(choice == 1):
        login()

    elif(choice == 2):
        register()

    else:
        print("invalid choice \n")
        init()


def register():
    print("***REGISTER HERE**** \n")
    first_name = input("Enter your first name \n")
    last_name = input("Enter your last name \n")
    email = input("Enter your email \n")
    password = input("choose your password \n")
    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]
    print(f"Account created successfully on {now} !!! \n")
    print(f"Your account number is: {accountNumber} \n")

    login()


def login():
    print("***Please login to your account*** \n")
    accountNumberFromUser = int(input("Enter your account number: \n"))
    passwordFromUser = input("Enter your Passord: \n")

    for accountNumber, userDetail in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetail[3] == passwordFromUser):
                bankOperations(userDetail)

    print("wrong account number or password \n")
    login()


def bankOperations(user):
    
    print(f"Welcome {user[0].upper()}, Time is: {now} \n")

    option = int(input(
        "what operation do u want to do? 1.(Deposit) 2.(Withdraw) 3.(Check Balance) 4.(Complaint) 5.(Profile) 6.(Logout) 7.(Exit) \n"))
        

    if (option == 1):
        depositOperation()
    elif (option == 2):
        withdrawOperation()
    elif (option == 3):
        checkBalance(user)
    elif (option == 4):
        complain()
    elif (option == 5):
        detail()
    elif (option == 6):
        logout()
    elif (option == 7):
        exit()

    else:
        print("you selected invalid option \n")

    bankOperations(user)


def depositOperation():
    amount = int(input("How much would you like to deposit? \n"))
    global balance
    balance += amount
    print(f"Your current balance is {balance}RWF \n")
    print("Thank you for banking with us \n")


def withdrawOperation():
    amount = int(input("How much would you like to withdraw? \n"))
    print(f"Take your cash: {amount}RWF \n")
    global balance
    balance -= amount
    print(f"Your current balance is {balance}RWF \n")

    print("Thank you for banking with us \n")

def checkBalance(user):
    print(f"Dear {user[0].upper()}, Your current balance is {balance}RWF \n")

def complain():
    complaint = input("What issue will you like to report? \n")
    print("Thank you for contacting us \n")

def detail():
    print("*********USER PROFILE***** \n")
    for accountNumber, userDetail in database.items():
        print(f"Account Number: {accountNumber}")
        print(f"First Name: {userDetail[0]}")
        print(f"Last Name: {userDetail[1]}")
        print(f"Email: {userDetail[2]} \n")
    
    


def logout():
    login()


def generateAccountNumber():

    return random.randrange(1111111111, 9999999999)


init()
