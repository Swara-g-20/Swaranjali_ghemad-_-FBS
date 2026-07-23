##Write a program to check if user has entered correct userid and password.
userid = input("Enter the userid: ")
password = input("Enter the password: ")

if userid == "admin" and password == "password":
    print("Login successful.")
else:
    print("Invalid userid or password.")    