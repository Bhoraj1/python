# user_credentials = {}

# #function to register a new user
# while True:
#   def register_user():
#       username = input("Enter a username: ")

#       #check if the username already exists
#       if username in user_credentials:
#         print("Username already exists. Please choose another one.")
#       else:
#         password = input("Enter a password: ") 
#         user_credentials[username] = password
#         print("Registration successful!")

#     #function to login a user
#   def login_user():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     #check if the username and password match
#     if username in user_credentials and user_credentials[username] == password:
#         print("Login successful!,Welcom back")
#     else:
#         print("Invalid username or password. Please try again.")
        

#   register_user()
#   login_user()







# part 2
user_credentials = {}

#function to register a new user
def register_user():

      username = input("Enter a username: ")

      #check if the username already exists
      if username in user_credentials:
        print("Username already exists. Please choose another one.")
      else:
        password = input("Enter a password: ")
        user_credentials[username] = password
        print("Registration successful!")

    #function to login a user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    #check if the username and password match
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!,Welcom back")
    else:
        print("Invalid username or password. Please try again.")
        

#Main Menu
def authentication_system():
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
        break 
    else:
        print("Invalid choice. Please Choose 1 , 2 and 3.")    

        
#Run Authentication system      
authentication_system()