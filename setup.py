from distutils.core import setup

setup(
    name='algos-py',
    version='0.2.1',
    license='MIT',
    author='Aleksandr Lisianoi',
    author_email='all3fox@gmail.com',
    url='https://github.com/all3fox/algos-py',
    packages=[
        'src', 'src.sort', 'src.graph', 'src.sset',
        'tests', 'tests.test_graph', 'tests.test_sort', 'tests.test_sset'
    ],
    description="Classic computer science algorithms in Python",
    long_description="Classic computer science algorithms in Python",
    platforms=['linux']
)
