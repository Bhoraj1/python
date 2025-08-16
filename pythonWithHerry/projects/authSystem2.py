# Use import module when you need many things from it.
# Use from module import X when you only need one or two items often.

import re   
import hashlib 
from datetime import datetime

#hash password
def hash_password(password):
   return hashlib.sha256(password.encode()).hexdigest()

#password checker function
def strong_password(password):
    if len(password) < 8:
        return False,"Passworld must be at least 8 characters long."
    
    if not re.search("[A-Z]", password):
        return False,"Password must include at least one uppercase."
    
    if not re.search("[0-9]", password):
        return False , "Passwod must be include at least one number"
    
    if not re.search("[!@#$%^&*]", password):
        return False, "Password must include one special symbol"
        
    return True, "Now password is Strong"

#Function to log user activities
def log_events(event):
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   with open("log.txt", 'a') as file:
    file.write(f"{timestamp} - {event}\n")

def register_user():
      username = input("Enter a username: ")
      password = input("Enter a password: ") 
      is_valid,feedback = strong_password(password)
      if not is_valid:
       print(feedback)  
       log_events(f"Failed registration attempt for user {username}")
       return #check without return as well.
      
      # If strong_password returned True → then hash the same password
      hashed_password = hash_password(password)
      with open("user.text",'a') as file:
       file.write(f"{username}:{hashed_password}\n")
       print("Registration successful!")
       log_events(f"Successful registration for user {username}") 

    #function to login a user

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("user.text", 'r') as file:
        users = file.readlines()
        for user in users:
            stored_username, stored_password = user.strip().split(':')
            if username == stored_username and hash_password(password) == stored_password:
                print("Login successful!, Welcom back")
                log_events(f"Successful login for user {username}")
                login_menu(username)
                return
            else:
             print("Invalid username or password. Please try again.")
             log_events(f"Failed login attempt for user {username}")
              
#function view log
def view_log(username):
    print(f"\nLogs for user {username}")
    with open("log.txt", 'r') as file:
        logs = file.readlines()
        # print(logs)
        user_log = [log.strip() for log in logs if username in log] #list
        # print(user_log)
        if user_log:
            for log in user_log:
                print(log)
            else:
                print("No logs found for this user.")

# function to diplay login menus first (1) 
def login_menu(username):
    while True:
        print("\nLogin Menu")
        print("1. View History")
        print("2. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_log(username)
        elif choice == "2":
            print("Logging out...")
            log_events(f"User {username} logged out")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")  


def main():
 while True:   
    print("Basic Authentication System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    options = input("Enter your choice: ") 
    if options == "1":
        register_user()
    elif options == "2":
        login_user()
    elif options == "3":
        print("Exiting the program. Goodbye!")
        log_events("Program exited")
        break 
    else:
        print("Invalid choice. Please Choose 1 , 2 and 3.")    

        