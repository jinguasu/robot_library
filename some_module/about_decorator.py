def log_level(level):
    def log_func_name(func):
        def wrapper(*args):
            if level == 1:
                print(func.__name__)
            else:
                print(func.__name__,func.__name__)
            return func(*args)
        return wrapper
    return log_func_name

class Foo(object):
    def __init__(self,func):
        self.__func = func
    def __call__(self,*args):
        print('class decorator is running')
        self.__func(*args)
        print('class decorator ending')


@log_level(1)
def foo(name,age=None,height=None):
    print('i am fool %s %s %s' % (name,age,height))

#foo('jin',45)

@Foo
def foo(name,age=None,height=None):
    print('i am fool %s %s %s' % (name,age,height))

foo('jin',45)