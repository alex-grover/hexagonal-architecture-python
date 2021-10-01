from setuptools import setup

setup(
    name='hex',
    version='0.0.0',
    packages=['hex'],
    url='https://github.com/alex-grover/hexagonal-architecture-python',
    license='gpl-3.0',
    author='Alex Grover',
    author_email='hello@alexgrover.me',
    description='Hexagonal Architecture in Python using Flask and SqlAlchemy',
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        hex=hex.cli:cli
    ''',
)
