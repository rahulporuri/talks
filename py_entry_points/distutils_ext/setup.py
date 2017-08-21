from setuptools import setup


setup(
    name="distutils_ext_pkg",
    entry_points={
        "distutils.commands":[
            "distutils_ext_pkg = distutils_ext_pkg.main:distutils_ext_pkg"
        ]
    }
)
