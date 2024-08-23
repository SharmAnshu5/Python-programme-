def fact(n):
    if n == 1:
        return n
    else:
        return n *fact(n-1)

A = int(input("Enter a number: "))

if A < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif A == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", A, "is", fact(A))