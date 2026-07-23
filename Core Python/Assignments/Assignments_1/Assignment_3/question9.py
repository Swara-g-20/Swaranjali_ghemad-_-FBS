##Input 5 subject marks from user and display grade(eg.First class,Second class ..)
marks1 = float(input("Enter the marks for subject 1: "))
marks2 = float(input("Enter the marks for subject 2: "))
marks3 = float(input("Enter the marks for subject 3: "))
marks4 = float(input("Enter the marks for subject 4: "))
marks5 = float(input("Enter the marks for subject 5: "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
average_marks = total_marks / 5

if average_marks >= 80:
    print("Grade: First Class")
elif average_marks >= 60:
    print("Grade: Second Class")
elif average_marks >= 40:
    print("Grade: Third Class")
else:
    print("Grade: Fail")