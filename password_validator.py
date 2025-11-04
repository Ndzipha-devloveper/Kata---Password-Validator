def is_password_secure():
  while True:
    password = input("Please enter your password")
    valid = True
    
    if not password:
      print("Password cannot be blank")
      valid = False
      
      #Length of the password
      if not len(password) < 8:
        print("Password must be at least 8 characters long")
        valid = False
        
      if not any(char.isupper) for char in password:
        print("Password must containt at least one uppercase letter")
        valid = False
        
      if not any(char.islower() for char in password:
        print("Password must contain at least one lowercase letter")
        valid = False
        
      if not any(char.isdigit() for char in password:
        print("Password must contain at least one digit")
        value = False
        
        if valid:
          print("Your password is secure")
          break
          
#calling my function
is_password_secure()
