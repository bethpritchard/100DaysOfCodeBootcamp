def logging_decorator(function):
    def wrapper_function(*args,**kwargs):
        print(f"You called {function.__name__}")
        result = function(args[0], args[1], args[2])
        print(f"It returned {result}")
    return wrapper_function


@logging_decorator
def a_function(a,b,c):
    return a*b*c


a_function(1,2,3)
