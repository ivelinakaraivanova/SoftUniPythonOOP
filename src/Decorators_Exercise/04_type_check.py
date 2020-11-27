def type_check(t):
    def decorator(function):
        def wrapper(param):
            if isinstance(param, t):
                return function(param)
            return "Bad Type"
        return wrapper
    return decorator


class type_check_cls:
    def __init__(self, t):
        self._t = t

    def __call__(self, function):
        def wrapper(param):
            if isinstance(param, self._t):
                return function(param)
            return "Bad Type"
        return wrapper


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
