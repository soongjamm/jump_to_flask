
# -*- coding: utf-8 -*-

import time


def decorate(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(args, kwargs)
        original_func(*args, **kwargs)
        end = time.time()
        print("time : %f sec" % (end - start))

    return wrapper


@decorate
def myfunc(msg, **kwargs):
    print("%s func exec" % msg)


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result


def print_kwargs(**kwargs):
    print(kwargs)


# decorated_myfunc = decorate(myfunc)
# decorated_myfunc()
myfunc("You need python", a=1, b=2, c=3)

print(add_many(1, 2, 3))
print_kwargs(name="foo", age=3)
