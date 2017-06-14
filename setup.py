from setuptools import setup, find_packages

with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name='algos-py',
    version='0.4.3',
    license='MIT',
    author='Aleksandr Lisianoi',
    author_email='all3fox@gmail.com',
    url='https://github.com/all3fox/algos-py',
    packages=find_packages(),
    description="Classic computer science algorithms in Python",
    long_description=long_description,
    platforms=['linux', 'windows', 'macos'],
)
