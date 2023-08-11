from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Meu primeiro pacote'
LONG_DESCRIPTION = 'Meu primeiro projeto em Python com uma descrição um pouco mais longa'

setup(
        name = 'operatorsMelissa',
        version = VERSION,
        author = 'Melissa',
        author_email = 'msnmelissaoa15@hotmail.com',
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        packages = ['operatorsMelissa'],

        classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ]
)