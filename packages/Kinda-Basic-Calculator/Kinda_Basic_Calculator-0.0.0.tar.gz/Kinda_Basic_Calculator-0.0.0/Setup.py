from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Prodution/Stable',
    'Indended Audience :: Anyone',
    'OS :: Microsoft Windows 10,11; Mac os ventura, linux',
    'Licence :: OSI Approved :: MIT Licence'
    'Programing Language :: Python 3.11',
    'Uses :: Calculating basic sums, Pi, and for fun'
]

setup(
    Name = 'Calc',
    Version = '0.0.1',
    Description = "It is a simple calcualator which can do basic aritmetic and give pi's value.",
    Full_Description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    Source_code = 'https://github.com/IEYT',
    Author = 'IE',
    Licence = 'MIT',
    Keywords = 'CalcBasic, Calc, Calculator',
    Package = find_packages(),
    Install_requires = ['math']
)
import math