def F(n):
    if n <= 1:
        return n
    else:
        fib = F(n - 1) + F(n - 2)
        print(fib)
        return fib
    

print("Answer to this is : ", F(10))