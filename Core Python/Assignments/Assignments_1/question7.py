##Program to Find the Roots of a Quadratic Equation
import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Find the two roots
root1 = (-b - cmath.sqrt(d)) / (2*a)
root2 = (-b + cmath.sqrt(d)) / (2*a)
print("The roots are {0} and {1}".format(root1, root2))