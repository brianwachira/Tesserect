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
