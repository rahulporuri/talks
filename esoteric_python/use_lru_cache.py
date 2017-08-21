from functools import lru_cache


def fib_wo_cache(n):
    if n in set([0, 1]):
        return n
    return fib_wo_cache(n-1) + fib_wo_cache(n-2)


@lru_cache()
def fib_wt_cache(n):
    if n in set([0, 1]):
        return n
    return fib_wt_cache(n-1) + fib_wt_cache(n-2)


if __name__ == "__main__":
    from using_decorators import time_

    time_(fib_wo_cache)(30)
    time_(fib_wt_cache)(30)
