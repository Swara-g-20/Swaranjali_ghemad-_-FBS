##WAP to print Fibonacci series upto n.
n = int(input("Enter a number: "))
a, b = 0, 1 
print(a, b, end=' ')
for _ in range(2, n):
    a, b = b, a + b
    print(b, end=' ')   
    