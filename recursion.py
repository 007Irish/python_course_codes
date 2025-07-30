''' fibonacci series
    fib(0) = 0
    fib(1) = 1
    fib(2) = fib(0) + fib(1)
    fib(3) = fib(1) + fib(2)
    fib(4) = fib(2) + fib(3)

'''
def fib(n):
    if(n==0 or n==1):
        return n
    a = fib(n-2) + fib(n-1)
    return a
b = fib(13)
print(b)

# fib(4) + fib(5)
# fib(2) + fib(3) + fib(5)
# fib(0) + fib(1) + fib(3) + fib(5)
# 0 + 1+ fib(1) + fib(2) + fib(3) + fib(4)
# 0+ 1+ 1 + fib(0) + fib(1) + fib(1) + fib(2)+ fib(4)
# 0+ 1+ 1+ 0 + 1+ 1 + fib(0) + fib(1) + fib(2) + fib(3)
# 0+ 1+ 1+ 0+ 1+ 1+ 0 + 1 + fib(0) + fib(1) + fib(3)
# 0+ 1+ 1+ 0+ 1+ 1+ 0+ 1+ 0 + 1+ fib(1) + fib(2)