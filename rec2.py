def fun(n):
    if n==0:
        return n
    return n+fun(n-1)
print(fun(4))