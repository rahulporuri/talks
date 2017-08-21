virtualenv venv
source venv/bin/activate
pip install -e .

- will create a virtualenv which will contain pip, setuptools and wheel;
and the `distutils_ext_pkg`. At the moment, the package doesn't contribute
anything, loading the extension point simply prints a dummy string.

- [ ] figure out how to add a new keyword argument -`python setup.py <>`.
The wheel package, which contributes the `bdist_wheel` command
