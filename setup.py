from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

s = setup(
    name = "epytech",
    version = "0.7",
    license = "MIT",
    long_description = long_description,
    long_description_content_type = 'text/markdown',  # This is important!
    description = "The python's api for epitech's intra",
    url = "https://github.com/Neotoxic-off/epytch",
    packages = ['epytech'],
    install_requires = [],
    python_requires = ">= 3.4",
    author = "Neo",
    author_email = "paul.gardien@epitech.eu",
    )
