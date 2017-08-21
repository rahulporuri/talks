from __future__ import print_function
from distutils.core import Command


class distutils_ext_pkg(Command):
    user_options = [('default-arg=', 'd',
                      'default argument')
                    ]

    def initialize_options(self):
        """abstract method on baseclass that needs to be overwritten"""
        self.default_arg = None

    def finalize_options(self):
        """abstract method on baseclass that needs to be overwritten"""
        self.default_arg = "What?"

    def run(self):
        """abstract method on baseclass that needs to be overwritten"""
        print("Beep Boop Beep {}".format(self.default_arg))
