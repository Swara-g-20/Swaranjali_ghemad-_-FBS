##Write a program to check if person is eligible to marry or not (male age >=21 and
##female age>=18)
male_age = int(input("Enter the male's age: "))
female_age = int(input("Enter the female's age: "))
if male_age >= 21 and female_age >= 18:
    print("The person is eligible to marry.")   
else:
    print("The person is not eligible to marry.")