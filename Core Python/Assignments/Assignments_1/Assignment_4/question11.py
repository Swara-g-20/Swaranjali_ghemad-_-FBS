##WAP to check if given number Strong Number.
num = int(input("Enter a number: "))
sum_of_factorials = 0
temp = num

while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_of_factorials += factorial
    temp //= 10

if sum_of_factorials == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")