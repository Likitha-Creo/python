def fib(n):
    a, b = 0, 1
    result = []
    while(a < n):
        result.append(a)
        a, b = b, a+b
    return result

ans=fib(100)
print(ans)
