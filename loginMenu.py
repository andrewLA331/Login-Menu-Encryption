#Andrew Allen
#CS195

import os
import os.path
import sys
import base64

# Program Instructions-
# First, register a username and password
# Second, login with that username and password

def loginMenu():
   choice = raw_input("Enter L to login or R to register: ")
   
   key = "Swordfish"
   
   if choice == "L":
      username = raw_input("Please enter username: ")
      password = raw_input("Please enter password: ")
      file = "Users/" + username + ".txt"
      try:
         info = open(file, "r")
         for line in info.readlines():
            p, a = line.strip().split("|")
            loginMenu.access = a
            password = encrypt(key, password)

            if os.path.isfile(file):
               if (password in p) and len(password) >= 7:
                  print("Logging in...")
                  return True
               else:
                  print("Incorrect password. Please try again.")
                  return False
        
      except IOError as e:
         print("Username does not exist. Please try again.")
         return False
    
   elif choice == "R":
      
      username = raw_input("Please create username: ")
      print("Password must be between 8 and 25 characters with atleast one letter and one number.")
      password = raw_input("Please create password: ")
      
      if len(password) >= 8 and len(password) <= 25:
         if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
            encrypted = encrypt(key, password)
            file = "Users/" + username + ".txt"
            info = open(file, "w+")
            info.write(encrypted + "|1")
            info.close()
            loginMenu.access = "1"
            return True
            
         else:
            print("Password does not meet requirements. Please try again.")
            return False
            
      else:
         print("Password does not meet requirements. Please try again.")
         return False
 
#encrypts password        
def encrypt(key, password):
   encrypted_chars = []
   
   for i in xrange(len(password)):
      key_c = key[i % len(key)]
      encrypted_c = chr(ord(password[i]) + ord(key_c) % 256)
      encrypted_chars.append(encrypted_c)
      
   encrypted_string = "".join(encrypted_chars)
   
   return base64.urlsafe_b64encode(encrypted_string)

      
#options menu asks user to select an option          
def optionsMenu():
   
   #access levels 1, 2, and 3
   admin = 1
   inter = 2
   #basic = 3
   accessLevel = int(loginMenu.access)
 
   print("-------------------")
   print("| Access level " + loginMenu.access + " |")
   print("-------------------")
   print("-1 for Time Reporting \n"
          "-2 for Accounting \n"
          "-3 for IT Helpdesk \n"
          "-4 for Engineering Documents \n"
          "-5 for Current Projects \n"
          "-6 for Training \n"
          "-7 for Logout \n"
          "-8 for Exit and End Session \n")
   print("-----------------")
   option = input("Select an option: ")
   
   if option == 1: #only admin or inter can access
      if accessLevel == admin or accessLevel == inter:
         timeReporting()
      else:
         print("You are not authorized to access this area.")
         optionsMenu()
   
   elif option == 2: #only admin can access
      if accessLevel == admin:
         accounting()
      else:
         print("You are not authorized to access this area.")
         optionsMenu() 
   
   elif option == 3: #anyone logged in can access
      itHelpdesk()
         
   elif option == 4: #only admin can access
      if accessLevel == admin:
         engineeringDocuments()
      else:
         print("You are not authorized to access this area.")
         optionsMenu()
         
   elif option == 5: #only admin or inter can access
      if accessLevel == admin or accessLevel == inter:
         currentProjects()
      else:
         print("You are not authorized to access this area.")
         optionsMenu()
         
   elif option == 6: #anyone logged in can access
      training() 
         
   elif option == 7:
      logout()
      
   elif option == 8:
      exitEnd()
      
   else:
      print("Enter a valid option.")
      optionsMenu()
   
#represents the different menu areas-------------  
def timeReporting():
   print("You have accessed Time Reporting.")
   print("---------------------------------")
   optionsMenu()
   
def accounting():
   print("You have accessed Accounting.")
   print("-----------------------------")
   optionsMenu()
   
def itHelpdesk():
   print("You have accessed IT Helpdesk.")
   print("------------------------------")
   optionsMenu()
   
def engineeringDocuments():
   print("You have accessed Engineering Documents.")
   print("----------------------------------------")
   optionsMenu()
   
def currentProjects():
   print("You have accessed Current Projects.")
   print("-----------------------------------")
   optionsMenu()
   
def training():
   print("You have accessed Training.")
   print("---------------------------")
   optionsMenu()
   
def logout():
   print("Logging out...")
   print("--------------")
   main()
   
def exitEnd():
   print("Goodbye.")
   print("--------")
   sys.exit()
#-------------------------------------------------


#starts the program
def main():
   login = loginMenu()
   if login == True:
      optionsMenu()
   else:
      main()
       
#calls to start the program
main()