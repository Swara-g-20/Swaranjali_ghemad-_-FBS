##Write a program to swap two numbers without using third variable.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)