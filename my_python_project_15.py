#It is my 15th python project
#This code is for password hashing and recheck if the password is matched or not matched
#For this I am using "bcrypt" 
#To install "bcrypt" type "pip install bcrypt" in the terminal
import bcrypt

#There is the password
password = b"SecretPassord44"

#Here it will be hashed using bcrypt
hashed = bcrypt.hashpw(password , bcrypt.gensalt())
#Here it will print hashed password 
print(hashed)

#Here it will check if the password is matched or not matched
if bcrypt.checkpw(password ,hashed):
    print("It is matched")
else:
    print("It is not matched")
    

    
    
