from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='rotating_proxy',
   version='1.0',
   description='A module to automatically fetch rotating proxy ips.',
   license="MIT",
   long_description=long_description,
   author='Man Foo',
   author_email='stamas01@gmail.com',
   url="http://www.foopackage.com/",
   packages=['rotating_proxy'],
   install_requires=['beautifulsoup4'],
)