#!/usr/bin/env python3.6
from user import User
from Credentials import Credentials
def create_user(fname,lname,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,username,password)
    return new_user
def create_Credentials(webname,username,password):
    '''
    Function to create a new Credentials
    '''
    new_Credentials = Credentials(webname,username,password)
    return new_Credentials
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def save_Credentials(Credentials):
    '''user
    Function to save Credentials
    '''
    Credentials.save_Credentials()
def del_Credentials(Credentials):
    '''
    Function to delete a contact
    '''
    Credentials.delete_Credentials()
def find_Credentials(name):
    '''
    Function that finds a Credentials by number and returns the Credentials
    '''
    return Credentials.find_by_name(name)

def check_existing_Credentials(name):
    '''
    Function that check if a Credentials exists with that number and return a Boolean
    '''
    return Credentials.Credentials_exist(name)
def display_Credentials():
    '''
    Function that returns all the saved Credentials
    '''
    return Credentials.display_Credentials()
def main():
        print("Hello Welcome to your Password-Locker Account. What is your name?")
        user_name = input()
        print(f"Hello {user_name}. what would you like to do?")
        print('\n')
        while True:
                print("Use these short codes : cc - create a new Account, dc - display Credentials, fc -find a credential, ex -exit the App-Locker")
                short_code = input().lower()
                if short_code == 'cc':
                        print("New Account")
                        print("-"*10)
                        print ("First name ....")
                        first_name = input()
                        print("Last name ...")
                        last_name = input()
                        print("Username ...")
                        username = input()
                        print("Password ...")
                        password = input()
                        save_user(create_user(first_name,last_name,username,password)) # create and save new contact.
                        print ('\n')
                        print(f"New User {first_name} {last_name} created")
                        print('\n')
                elif short_code == 'dc':
                        if display_Credentials():
                                print("Here is a list of all your Credentials")
                                print('\n')
                                for Credentials in display_Credentials():
                                        print(f"{Credentials.webname} {Credentials.user_name} .....{Credentials.password}")
                                        print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any Credential saved yet")
                                print('\n')
                elif short_code == 'fc':
                        print("Enter the Website name you want to search for")

                        search_web_name = input()
                        if check_existing_Credentials(search_web_name):
                                search_Credentials = find_Credentials(search_web_name)
                                print(f"{search_Credentials.user_name} {search_Credentials.password}")
                                print('-' * 20)
                        else:
                                print("Those Credentials do not exist")

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
        main()