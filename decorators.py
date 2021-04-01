import functools

user = {
    'name': 'Azalia',
    'password': 'admin'
}


def decorator_maker(password):
    def check_password(func):
        if password != user['password']:
            return lambda x: "В доступе отказано"
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return check_password


ans = {}


# def cached(func):
#     def wrapper(*args, **kwargs):
#         got = ans.get(tuple(*args, **kwargs))
#         if got is None:
#             ret = func(*args, **kwargs)
#             ans[tuple(*args, **kwargs)] = ret
#             return ret
#         return got
#     return wrapper


def cached(func):
    def wrapper(i):
        got = ans.get(i)
        if got is None:
            ret = func(i)
            ans[i] = ret
            return ret
        return got
    return wrapper


@cached
@decorator_maker('admin')
def F(i):
    if i < 3:
        return 1
    return F(i-1)+F(i-2)

print(F(12))