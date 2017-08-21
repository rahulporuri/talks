from __future__ import print_function
from functools import total_ordering


@total_ordering
class Container(object):
    def __init__(self, arg):
        self.arg = arg
    
    def __eq__(self, other):
        return len(self.arg) == len(other.arg)
    
    def __lt__(self, other):
        return len(self.arg) < len(other.arg)


if __name__ == "__main__":
    one = Container(arg=[1])
    other = Container(arg=[1,2])

    print(other > one)

    one = Container(arg=[1, 3])
    other = Container(arg=[1,2])

    print(other >= one)
