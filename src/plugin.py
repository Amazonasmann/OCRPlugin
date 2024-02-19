from .hooks import hookspec

@hookspec.implement()
def some_hook(arg1, arg2):
    # Plugin's implementation of the first hook
    print(f"Plugin executing some_hook with {arg1} and {arg2}")
    return arg1 + arg2

@hookspec.implement()
def another_hook(data):
    # Plugin's implementation of the second hook
    print(f"Plugin processing data in another_hook: {data}")
    return data * 2
