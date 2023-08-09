from setuptools import setup

from what_time_is_it import __version__

setup(
    name='what-time-is-it',
    version=__version__,

    url='https://github.com/blacksmithop/what-time-is-it',
    author='Abhinav KM',
    author_email='angstycoder101@gmail.com',

    py_modules=['what-time-is-it'],
    install_requires=[
        'pytest>=4',
        'pytest-cov>=2'
    ],
    extras_require={
    'extra': [
        'tabulate',
    ],
    },
    entry_points={
    'console_scripts': [
        'add=what_time_is_it.math:cmd_add',
    ],
},
)