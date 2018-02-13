from setuptools import setup

setup(name='forline',
    version='1.0',
    packages=['forline'],
    entry_points = {
        'console_scripts': ['forline=forline.forline:main'],
    },
    zip_safe=False
)