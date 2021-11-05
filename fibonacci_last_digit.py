# Iterative version
def FibonacciLastDigit(n):
    if n == 0 or n == 1:
        return n
    F = [None] * n
    F[0] = 0
    F[1] = 1
    for i in range(2,n):
        F[i] = (F[i-1] + F[i-2]) % 10
    return (F[n-1] + F[n-2]) % 10

n = int(input())
print(FibonacciLastDigit(n))
