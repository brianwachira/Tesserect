#!/usr/bin/env python3.6

from password_locker import Password_Locker

def initialize_password_locker(username,password):
    '''
    Function to initialize password locker
    '''
    new_password_locker = Password_Locker(username,password)
    return new_password_locker

def create_account(password_locker):
    '''
    Function to create user account
    '''
    return Password_Locker.create_account(password_locker)

def login(password_locker):
    '''
    Function to log in user
    '''
    return Password_Locker.login(password_locker)

def add_credentials(password_locker,account_name,account_username,account_password):
    '''
    Function that adds user's credentials
    '''
    return Password_Locker.add_credentials(password_locker,account_name,account_username,account_password)

def generate_credentials(password_locker):
    '''
    Function that generates user's credentials
    '''
    return Password_Locker.generate_credentials(password_locker)

def generate_password(password_locker):
    '''
    Function that generates passwords
    '''
    return Password_Locker.generate_password(password_locker)

def set_password_length(password_locker,length):
    '''
    Function that generates a password based on the user's length of choice
    '''
    return Password_Locker.set_password_length(password_locker,length)

def main():
    print("Hi there\n")
    print("What would you like to do")
    print('\n')
    instance = ""
    while True:
        print("Use these short codes\n li - Log in, ca - Create an account, ac - Add credentials, gc - Generate credentials, gp - Generate passwords, gsp - Generate password with a set length, ex - exit")
        choice = input()

        if(choice == 'li'):
            print("Enter your username")
            username = input().lower()
            print("Enter password")
            password = input()
            instance = initialize_password_locker(username,password)
            if(login(instance)):
                print("Login succesful")
            else:
                print("It seems your account does not exist")

        elif(choice == 'ca'):
            print("Enter your username")
            username = input().lower()
            print("Enter password")
            password = input()
            instance = initialize_password_locker(username,password)
            if(create_account(instance)):
                print("Account creation succesful\n")
                print(f"Welcome {username}")
            else:
                print("Account already exists")

        elif(choice == 'ac'):
                print("Enter the account you wish to save")
                account_name = input()
                print("Enter the username")
                username = input()
                print("Enter the password")
                password = input()
                if(add_credentials(instance,account_name,username,password)):
                    print("Succesful!")
                else:
                    print("Your account does not exist")
        
        elif(choice == 'gc'):
            credentials = generate_credentials(instance)
            print("The credentials are :\n")
            print(f"{credentials}")

        elif(choice == 'gp'):
            password = generate_password(instance)
            print("Kindly copy the password below :")
            print(f"{password}")
    
        elif(choice == 'gsp'):
            print("Enter the length of a password you'd want")
            length_of_password = input()
            password = set_password_length(instance,length_of_password)
            print("Kindly copy password to clipboard")
            print(f"{password}")
        
        else:
            print("Bye")
            break


if __name__ == '__main__':
    main()
