#fib 
def fib(n):
    p = 1
    c = 0 
    for i in range(n):
        pi = c
        c = c + p
        p = pi
    return c