# Exercise : Password strength Checker 
# Problem statement : Create a program that checks whether a password is strong. 
# Conditions : 
# At least 8 characters 
# Contains uppercase letters
# Contains lowercase letters
# contains numbers


# Now : Let's solve the problem...

password = input("Enter password:")
has_upper = False
has_lower = False
has_digit = False

for char in password:
          if char.isupper() :
                    has_upper = True
          elif char.islower() :
                    has_lower = True
          elif char.isdigit () :
                    has_digit = True
                    if len(password) >+ 8 and has_upper and has_lower and has_digit:
                              print("Strong Password")
                    else:
                              print("Weak Password")
                              
#### Thats a nice problem can help a developer or a programmer to understand the code and realtime problem.