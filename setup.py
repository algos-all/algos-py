from distutils.core import setup

with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name='algos-py',
    version='0.4.0',
    license='MIT',
    author='Aleksandr Lisianoi',
    author_email='all3fox@gmail.com',
    url='https://github.com/all3fox/algos-py',
    packages=[
        'src', 'src.sort', 'src.graph', 'src.sset',
        'tests', 'tests.test_graph', 'tests.test_sort', 'tests.test_sset'
    ],
    description="Classic computer science algorithms in Python",
    long_description=long_description,
    platforms=['linux']
)
