class store_results:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        with open("results.txt", "a") as file:
            result = self._func(*args)
            file.write(f"Function '{self._func.__name__}' was called. Result: {result}\n")


def store_result(func):
    def wrapper(*args):
        with open("results.txt", "a") as file:
            result = func(*args)
            file.write(f"Function '{func.__name__}' was called. Result: {result}\n")
            return result
    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
