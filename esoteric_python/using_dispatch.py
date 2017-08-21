"""
$ edm envs create --version 3.6 dispatch_env
$ edm run -e dispatch_env -- python using_dispatch.py
"""
from __future__ import print_function
from functools import singledispatch


@singledispatch
def main_func(*args, **kwargs):
    return None


@main_func.register(int)
def _(*args, **kwargs):
    print("the function got an integer input - {}".format(*args, **kwargs))


@main_func.register(str)
def _(*args, **kwargs):
    print("the function got an string input - {}".format(*args, **kwargs))


if __name__ == "__main__":
    main_func('str')
