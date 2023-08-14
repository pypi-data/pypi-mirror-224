from setuptools import setup, find_packages

setup(
    name='aggin',
    version='0.3.1',
    description='My Custom Programming Language',
    author='Aman',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'aggin = aggin:main'
        ]
    }
)