from __future__ import print_function
from functools import wraps
import logging
from time import time


def print_before(func):
    @wraps(func)
    def run_func(*args, **kwargs):
        print("Before running func")
        func(*args, **kwargs)
        print("After running func")
    return run_func


def log_before(func):
    @wraps(func)
    def run_func(*args, **kwargs):
        logging.log(10, "Before running func")
        func(*args, **kwargs)
        logging.log(10, "After running func")
    return run_func


def time_(func):
    @wraps(func)
    def run_func(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        print("the {} took {}".format(func, time()-start))
    return run_func


if __name__ == "__main__":
    time_(print)("The actual print function")
