from __future__ import print_function
from functools import partial


if __name__ == "__main__":
    range = partial(range, 10)
    print(range(20))
