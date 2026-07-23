##Write a program to check if given number is Armstrong number or not.
num = int(input("Enter a number: "))
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** len(str(num))
    temp //= 10

if sum_of_powers == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")