from setuptools import setup

setup(
    name='forline',
    version='1.0',
    license='MIT'
    packages=['forline'],
    url = 'https://github.com/GillesArcas/forline',
    author = 'Gilles Arcas',
    author_email = 'gilles.arcas@gmail.com',
    entry_points = {
        'console_scripts': ['forline=forline.forline:main'],
    },
    zip_safe=False
)