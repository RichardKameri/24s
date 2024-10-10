def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function and printing the result
print("Factorial of 5:", factorial(5))