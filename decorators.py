def big_letters(func):
    def decorator(s):
        return func(s.upper())
    return decorator


print = big_letters(print)
print("hey")