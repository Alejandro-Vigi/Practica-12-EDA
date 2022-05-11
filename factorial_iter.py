def factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact


print(factorial(5))
print(factorial(1))
print(factorial(2))
print(factorial(3))