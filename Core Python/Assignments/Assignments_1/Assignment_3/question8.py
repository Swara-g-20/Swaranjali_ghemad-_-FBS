##Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)


from random import random


userid = input("Enter the userid: ")
password = input("Enter the password: ")

if userid == "admin" and password == "password":
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_input = int(input("Enter the captcha: "))
    if user_input == captcha:
        print("Success!")
    else:
        print("Failed.")
else:
    print("Invalid userid or password.")