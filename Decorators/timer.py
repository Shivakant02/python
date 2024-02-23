#create a decorator named timer

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper
    
@timer
def test_f(n):
        time.sleep(n)

test_f(2)