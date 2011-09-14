import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "YAS",
    version = "0.1.0",
    author = 'Proteus Technologies',
    author_email = 'team@proteus-tech.com',
    description = ("Yet Another Stub for Python (can be used with roles library for doing DCI)"),
        url='http://proteus-tech.com',
    packages = ['yas',],
    long_description = read('README.markdown'),
)

