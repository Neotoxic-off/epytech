from setuptools import setup, find_packages
 
setup( 
        name             = 'epitech.py',
        version          = '0.1',
        url              = 'https://github.com/Neotoxic-off/epitech.py',
        license          = 'MIT',
        author           = 'Neo',
        author_email     = 'paul.gardien@epitech.eu',
        description      = 'Just a simple begin of the epitech api in python3',
        packages         = find_packages(exclude = ['tests']),
        long_description = open('README.md').read(),
        zip_safe         = False
    )