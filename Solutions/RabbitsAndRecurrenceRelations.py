def fib(n, k=1, a=1, b=1):
    if n > 2:
        b = fib(n-1, k, b, k * a + b)
    return b


print(fib(5, 3))  # 19
print(fib(34, 4))  # 18788331166609