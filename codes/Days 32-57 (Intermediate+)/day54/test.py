import time
def decorator(func):
    time.sleep(2)
    return func

@decorator
def test():
    print("test")

test()