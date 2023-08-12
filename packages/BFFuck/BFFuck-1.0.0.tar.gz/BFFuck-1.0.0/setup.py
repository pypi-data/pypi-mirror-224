from setuptools import *
setup(
    name='BFFuck',
    version='1.0.0',
    url='https://github.com/none-None1/BFFuck',
    packages=['bffuck'],
    description='Makes Brainfucking Easier!',
    long_description=open("README.md").read(),
    entrypoints={'console_scripts':['bffuck=bffuck:_cli']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Code Generators'
    ]
)
