def f(s, x):
    if not s:
        return s
    elif s[-1] == x: # last element is equal to x
        return f(s[:-1], x) # call itself with the rest of the list
    else:
        return f(s[:-1], x) + [s[-1] * x] # call itself with the rest of the list and add the last element multiplied by x

print(f([1, 2,6,8], 5))