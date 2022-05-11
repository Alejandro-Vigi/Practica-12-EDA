def fibonacci_iter(n):
    a = 1
    b = 1
    for i in range (1, n):
        a, b = b, a + b
    return b

def fibonacci_rec(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci_rec (n - 1) + fibonacci_rec (n - 2)

memoria = {0:1, 1:1, 2:2}
def fibonacci_mem(n):
    if n in memoria:
        return memoria [n]
    memoria [n] = fibonacci_mem (n - 1) + fibonacci_mem (n - 2)
    return memoria [n]

print (fibonacci_mem(0))
print (fibonacci_mem(1))
print (fibonacci_mem(2))
#print (fibonacci_mem(3))
#print (fibonacci_mem(4))
print (fibonacci_mem(5))
print (fibonacci_mem(8))

print(memoria)
