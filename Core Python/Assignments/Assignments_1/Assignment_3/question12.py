##Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number: "))
num_str = str(num)
if num_str == num_str[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")