from __future__ import print_function
from functools import partial


if __name__ == "__main__":
    custom_print = partial(print, sep='-', end='\n*******\n')
    custom_print(1, 2, 3, 4)
