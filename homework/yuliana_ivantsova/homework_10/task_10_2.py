def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            func(*args)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


def repeat_me(count):
    def decorator(func):
        def wrapper(*args):
            list(map(lambda _: func(*args), range(count)))
        return wrapper
    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
