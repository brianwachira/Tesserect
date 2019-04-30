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
        else:
            print("Bye")
            break


if __name__ == '__main__':
    main()
