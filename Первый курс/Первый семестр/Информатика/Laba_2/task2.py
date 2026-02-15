def f(n, k):
    if n == 0 and k == 0 or k == 0 and n == 1:
        return True
    elif n == 0 and k > 0 or k == 0:
        return False
    if n == 1:
        return True
    if n % k == 0:
        return f(n // k, k)
    else:
        return False

print(f(9, 3))


