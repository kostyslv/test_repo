from time import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.time
        hard_func(*args, **kwargs)
        finish = time.time
        result = finish - start
        return result
    return inner

@timer
def hard_func():
    c = 1
    c += 1
    print(c)
    return [x ** 2 ** x for x in range(40)]

print(hard_func())