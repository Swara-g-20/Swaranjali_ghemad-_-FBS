##Write a program to input any alphabet and check whether it is vowel or consonant.
alphabet = input("Enter an alphabet: ")
if alphabet in 'aeiouAEIOU':
    print("The alphabet is a vowel.")
else:
    print("The alphabet is a consonant.")   