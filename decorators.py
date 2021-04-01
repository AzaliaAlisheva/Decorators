import functools

user = {
    'name': 'Azalia',
    'password': 'admin'
}


def check_password(password):
    def decorator (func) :
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if password == user['password']:
                return func(*args, **kwargs)
            return 'В доступе отказано'
        return wrapper
    return decorator


@check_password('admin')
def get_secure_information(text):
    if text == 'Hello':
        return 'Hello my dear friend!'
    if text == 'Qest':
        return 'How are you?'
    return "Choose between 'Hello' and 'Quest'"


print(get_secure_information('Hello'))