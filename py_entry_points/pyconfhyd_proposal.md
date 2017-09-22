Entering the world of `entry_points`
==================================


Abstract
--------

Your scripts will eventually grow into a package. Your package needs to be user-friendly to get more people to use it. Your package might grow big in order to address everyone's needs. `entry_points` make your package more accessible. `entry_points` help you add functionality without adding _almost_ any extra code.

After this talk, you will be able to make your package accessible from the command line and extend your package's functionality using `entry_points`. You'll also have an understanding of how `entry_points` work.

This talk is intended for audience with a basic understanding of functions and packages in Python.

Outline
-------

A lot of popular Python packages use entry points to make it easier to use them and to make it easier to extend their functionality. A very popular examples is pip.

Broadly speaking, entry points can be used to make your package easily accessible and extensible. Specifically, `entry_points` is a keyword argument to the `setup` function, the one in every `setup.py` file.

The `console_scripts` and `gui_scripts` entry points can be used to make your package accessible from the command line. Popular packages that makes use of this are `pip` and `flask`.

You can define your own entry point which others can contribute functionality to. A popular example is `sphinx.html_themes`, which the `Sphinx` package listens to. The entry point allows the `Sphinx` maintainers to prevent the number of default themes from blowing up while still allowing the community to contribute themes.

Finally, I will talk about how entry points are discovered and used. We'll look at the files in `*.egg-info` and how the `pkg_resources` package lets you use entry points.

Slides
------
https://github.com/rahulporuri/talks/blob/master/py_entry_points/py_entry_points.pdf

Links
-----
https://github.com/rahulporuri/talks/tree/master/py_entry_points - contains an initial draft of the presentation and code related to the presentation.
Slides from other talks/workshops I organised can be found at - https://github.com/rahulporuri/talks

Speaker bio
-----------
I am a Scientific Software Developer at Enthought India. I graduated from IIT Madras with a B.S. & M.S. in Physics.

I have been involved with the Python community in Pune over the last year, during which I gave talks on Using Cython and on Using virtualenvs. I conducted two workshops at SciPy India 2016 on Using Git & GitHub and on Automated testing using the unittest and mock libraries. Finally, I was invited to IIT Madras, my almamater, to give a conduct a workshop on Scientific Computing using the Numpy, Pandas and Cython libraries.

I hope that answers both the question of whether or not I am competent in Python and it's ecosystem of packages and the question of whether or not I am good at public speaking.
