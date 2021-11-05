# Iterative version
def FibonacciList(n):
    if n == 0 or n == 1:
        return n
    F = [None] * n
    F[0] = 0
    F[1] = 1
    for i in range(2,n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1] + F[n-2]

n = int(input("Write the index of the Fibonnaci number you want to know, starting from 0: "))
print(FibonacciList(n))
