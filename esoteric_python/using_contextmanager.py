from __future__ import print_function
from contextlib import contextmanager


@contextmanager
def a_ctxt_mgr():
    print("Before the context manager")
    try:
        yield
    finally:
        print("After the context manager")


def main():
    with a_ctxt_mgr():
        print("Inside the context manager")


if __name__ == "__main__":
    main()
